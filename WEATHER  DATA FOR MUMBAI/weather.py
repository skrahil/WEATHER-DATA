import requests
city_name = "mumbai,INDIA"
api_key = "b0a20ef11f8e70164f55a4ba1de83bec"

def get_weather(api_key,city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    print(response)
get_weather(api_key, city_name)
