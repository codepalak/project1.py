import requests

def kelvin_to_celsius_convertor(temp):
    data = temp - 273.15
    fn = "{:.2f}".format(data)
    return fn

def fetch_weatherdata_using_apikey():
    api_key = "9ecd9bf86b545691ad770bbbc2aa05b3"
    print("----------------------------------------------------------")
    cityName = input("Please enter a valid city name: ")
    params = {'q': cityName, 'appid': api_key}
    url = 'http://api.openweathermap.org/data/2.5/weather'  # Corrected API URL
    weatherdata = requests.get(url, params=params)
    
    if weatherdata.status_code == 200:
        temp = weatherdata.json()
        temperature = temp["main"]["temp"]
        print("Result:")
        print("    The temperature of city", cityName, "is", kelvin_to_celsius_convertor(temperature), "°C")
        print("----------------------------------------------------------")
    else:
        print("Server error!", weatherdata.status_code)

fetch_weatherdata_using_apikey()