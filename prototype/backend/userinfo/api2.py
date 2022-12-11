import requests
from django.shortcuts import render
import json

def set_comment(condition):
  if (condition == "Thunderstorm"):
    comment = "If you have to go outside, make sure to stay away from tall objects."
  elif (condition == "Drizzle"):
    comment = "Pitter patter. Pitter patter."
  elif (condition == "Snow"):
    comment = "Woah it's snowing. I love fresh snow"
  elif (condition == "Clouds"):
    comment = "Just another cloudy day."
  elif (condition == "Clear"):
    comment = "The weather's clear. Make sure to gets lots done!"
  else:
    comment = "Woah. Stay safe out there"
  return comment

# Function to handle the request to the OpenWeatherMap API
def get_weather(zip_code):
    api_key = "537275397b9037ad50e8da9814692add"
    # URL for the OpenWeatherMap API
    url = "http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
    # Send the request and get the response
    response = requests.get(url)
    condition = response.json()['weather'][0]['main']
    comment = set_comment(condition)

    weather_data = {
        "location": response.json()['name'],
        "temperature": response.json()['main']['temp'],
        "description": response.json()['weather'][0]['description'],
        "high": response.json()['main']['temp_max'],
        "low": response.json()['main']['temp_min'],
        "comment": comment
    }
    # Return the temperature in Fahrenheit
<<<<<<< HEAD
    return json.dumps(weather_data)


# Function to handle the request to the NewsData.io API
def get_news(language, category):
  api_key = 'pub_13171ec2935c971700ae44d5ab454b14e2bf3'
  url = "https://newsdata.io/api/1/news?apikey={}&language={}&category={}".format(api_key, language, category)
  response = requests.get(url)
  results = response.json()['results']
  comment = set_comment(results)
  news_data = {
    "News 1": (response.json()['results'][0]['title'], response.json()['results'][0]['country'][0], response.json()['results'][0]['description']),
    "News 2": (response.json()['results'][1]['title'], response.json()['results'][1]['country'][0], response.json()['results'][1]['description']),
    "News 3": (response.json()['results'][2]['title'], response.json()['results'][2]['country'][0], response.json()['results'][2]['description']),
    "News 4": (response.json()['results'][3]['title'], response.json()['results'][3]['country'][0], response.json()['results'][3]['description']),
    "News 5": (response.json()['results'][4]['title'], response.json()['results'][4]['country'][0], response.json()['results'][4]['description'])
    }
  
  return json.dumps(news_data)


print (get_weather('02134'))
print (get_news('en', 'world'))
=======
    return weather_data
>>>>>>> b060a4af3adef94b0b15ad65245e840fbaafffed
