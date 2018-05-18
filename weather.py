#This script will show the current weather of any city, using the API from Openweathermap
import requests #to get the url and access the datas
import datetime #to convert Unix time to something readable

#we are setting up some parameters
APPID = "YOUR API KEY GOES HERE"
unit = 'metric'
degree = '\xb0' + 'C'

#user input
cityName = input("City Name: ")

#link to get the data
weather_link = "http://api.openweathermap.org/data/2.5/weather?APPID=" + APPID + "&q=" + cityName + '&mode=json&units=' + unit

#variable to understand Json data from OpenWeatherMap
data = requests.get(weather_link).json()

#now, we are just going to get what we want. Mind the indexes
#Sample is here http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22
exact_name = data['name']
country = data['sys']['country']
main = data['weather'][0]['main']
description = data['weather'][0]['description']
temp = data['main']['temp']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']
humidity = data['main']['humidity']
wind = data["wind"]["speed"]
wind_deg = data["wind"]["deg"]
pressure = data["main"]["pressure"]

sunrise_data = data["sys"]["sunrise"]
sunset_data = data["sys"]["sunset"]

#to convert the time, we are using the datetime function inside the datetime library
sunrise = datetime.datetime.fromtimestamp(sunrise_data).strftime('%Y-%m-%d %H:%M:%S')
sunset = datetime.datetime.fromtimestamp(sunset_data).strftime('%Y-%m-%d %H:%M:%S')

#we print everything out
print("\n\nFor " + exact_name, country)
print("Current weather is:")
print('---------------------------------------')
print(main + " | " + description)
print("Temperature: {} \xb0C".format(temp))
print("Maximum at {}\xb0C, and minumum at {} \xb0C".format(temp_max, temp_min))
print("Humidity :",humidity,"%")
print("Wind speed: ", wind, "m/s heading ", wind_deg,"\xb0")
print("Pressure :",pressure,"hpa")
print("Sunrise is at: ", sunrise)
print("Sunset is at : ", sunset)
print('---------------------------------------')
