# How to use OpenWeatherMap API to get weather data

import pip._vendor.requests
import json
import sys
from datetime import datetime 


# API key
api_key = "a31837462d65dd07773fb28e6ae8416a" # Replace with your API key

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"


try:
    
    # get method of requests module
    response = pip._vendor.requests.get(complete_url)
    # json method of response object
    x = response.json()

    # print the value of x
    # print(x)


    # # print the x more prettier way
    # print(json.dumps(x, indent=4, sort_keys=True))

    current_date = datetime.now().strftime("%b %d | %H:%M:%S %p")

    # Now x contains list of nested dictionaries

    # Check the value of "cod" key is equal to "404", means city is found otherwise, city is not found
    # Check the value of "cod" key is equal to "401", means API key is invalid otherwise, API key is valid

    if x["cod"] == 401:
        print("Invalid API key")
        sys.exit(1) 

    if x["cod"] != "404":
        
            name = x["name"]
            country = x["sys"]["country"]
        
        # store the value of "main" key in variable y
            y = x["main"]

        # store the value corresponding to the "temp" key of y
            current_temperature = y["temp"]
    
        # store the value corresponding to the "feels_like" key of y
            current_feels_like = y["feels_like"]

        # store the vaue corresponding to the "wind speed" key of x
            current_wind_speed = x["wind"]["speed"]

        # store the value corresponding to the "pressure" key of y
            current_pressure = y["pressure"]
    
        # store the value corresponding to the "humidity" key of y
            current_humidity = y["humidity"]

        # store the value corresponding to the "visibility" key of x in KM unit 
            current_visibility = x["visibility"]/1000

        # store the dew point value in variable dew_point
            dew_point = current_temperature - ((100 - current_humidity)/5)
    
        # store the value of "weather" key in variable z
            z = x["weather"]
    
        # store the value corresponding to the "description" key at the 0th index of z
            weather_description = z[0]["description"]
    
        # print following values
            print("\x1b[31m {} \x1b[0m".format(current_date))
            print("\x1b[1m {} \x1b[0m\n".format(name + ", " + country))
            print("  \x1b[1m ☁️ {}°C \x1b[0m".format(" "+ str(current_temperature)))
            print("\x1b[1m Feels Like {}°C.{} \x1b[0m".format(round(current_feels_like),weather_description.capitalize()))         
            print("| \x1b[1m 💨 {} m/s NW   🧭 {} hPa \x1b[0m".format(current_wind_speed,current_pressure))
            print("| \x1b[1m 💧 {}%         Dew Point: {}°C \x1b[0m".format(current_humidity,round(dew_point,2)))
            print("| \x1b[1m Visibility: {} Km \x1b[0m\n".format(round(current_visibility,1)))
    else:
        print(" City Not Found ")

except pip._vendor.requests.exceptions.RequestException as e:
    print("Error: {}".format(e))
    print("Failed to connect to the Weather API server")
    sys.exit(1)


