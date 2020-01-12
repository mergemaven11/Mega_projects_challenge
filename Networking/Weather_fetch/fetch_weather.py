import os
import requests
import json
# Get the current weather for a given zip/postal code.

baseURL = 'http://api.openweathermap.org/data/2.5/weather?'
APIkey = os.environ.get('owAPI')
# Ask user to enter zipcode
def main():
    zip_code = input('Enter your zip: ')
    country_code = input('Enter two digit country code i.e "us": ')

    URLcomplete = baseURL + "appid=" + APIkey + '&' + \
    "zip=" + zip_code + "," + country_code

    # Get and return weather data
    response = requests.get(URLcomplete)

    x = response.json()
    
    for kv in x.items():
        print(kv)


if __name__ == "__main__":
    main()
