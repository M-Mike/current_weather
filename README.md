# current_weather
Developped with Python, it uses OpenWeatherMap's API to display the current weather

First, this script is under the MIT licence, you can use it, change it, modify it.

That being said, to be able to use this script, you'll need an API key from Openweathermap.org. It's free and opensource, and you'll juste have to copy-paste that key on the line where it says "YOUR API KEY GOES HERE"

The way it works goes like this:
- as state on their webpage https://openweathermap.org/current, we use the link they've given us to retreive current weather data. It's a json file, so we have to extract them
- the way to extract the data uses indexation. The script shows explicitly how they are extracted

To be able to get the sunrise and sunset time, I had to use the datetime() function to convert a UNIX time to a readable time. It uses your current location

You might also notice that there are two (2) ways how I printed the results with some texts.
One of them is to say: print("text", variable_result)
The second one is: print("text {}".format(variable_result)) which will show the content of variable_result inside the {}
They both work as you can see, and it was mainly to show that it's the same result. Although, using the method with {} gives more liberty on what to print
