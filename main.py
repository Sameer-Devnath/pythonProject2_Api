# import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "0cd9590c5606f92e59d74999a6fa2ec7"
CITY = input("Enter the name of the city: ")

def kelvin_to_celsius(kelvin):
    celsius = kelvin-273.15
    return celsius

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)

# print(response)
print("The temperature in",CITY,"is: ",temp_celsius,"℃")

