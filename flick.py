import requests
import json

API_KEY = "450815454f2c03a5c66a48b4a8a5d3ff"
CITY = "Saint Petersburg"

URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    weather_info = {
        "City": data["name"],
        "Temperature (°C)": data["main"]["temp"],
        "Feels Like (°C)": data["main"]["feels_like"],
        "Min Temperature (°C)": data["main"]["temp_min"],
        "Max Temperature (°C)": data["main"]["temp_max"],
        "Humidity (%)": data["main"]["humidity"],
        "Pressure (hPa)": data["main"]["pressure"],
        "Weather Description": data["weather"][0]["description"]
    }
    print(json.dumps(weather_info, indent=4, ensure_ascii=False))
else:
    print(f"❌ Error {response.status_code}")


