#!/usr/bin/env python3

import requests

GET_TACO_LINK = 'http://taco-randomizer.herokuapp.com/random/'
GET_WEATHER_LINK = 'https://www.metaweather.com/api/location/2367105/'

POST_TWEET_LINK = "http://darrienglasser.com/posttweet"

ID_NUMBER = 5

def celsiusToFarenheit(celsius):
    return celsius * 9.0/5.0 + 32

taco = requests.get(GET_TACO_LINK)
taco_json = taco.json()

taco_seasoning = taco_json["seasoning"]["name"]
taco_condiment = taco_json["condiment"]["name"]
taco_mixin = taco_json["mixin"]["name"]
taco_base_layer = taco_json["base_layer"]["name"]
taco_shell = taco_json["shell"]["name"]

taco_of_the_day = "Taco of the day! {} {} {} with {} in a {}".format(taco_seasoning, taco_condiment, taco_mixin, taco_base_layer, taco_shell)

weather = requests.get(GET_WEATHER_LINK)
weather_json = weather.json()

current_temp = celsiusToFarenheit(weather_json["consolidated_weather"][0]["the_temp"])
predictability = weather_json["consolidated_weather"][0]["predictability"]
weather_state = weather_json["consolidated_weather"][0]["weather_state_name"]

weather_string = "The temperature is {}°F with a {}% chance of {}".format(str(current_temp), str(predictability), weather_state)


status = taco_of_the_day + "\n\n" + weather_string ++ "\n\nVisit BradleyGlasser.com"
tweet_data = {"number":ID_NUMBER, "tweetText":status}
requests.post(POST_TWEET_LINK, data=tweet_data)

print("TWEET POSTED 🙏")

