import requests
from datetime import datetime

def fetch_weather(key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = {
        "datetime": datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
        "temperature": data['main']['temp'],
        "perceived_temperature": data['main']['feels_like'],
        "humidity": data['main']['humidity'],
        "wind speed": data['wind']['speed'],
        "city": data['name']
    }
    return weather
