# 3. Get city weather details using an API and display them in CLI.


import requests

API_KEY = "0bfa68b216193eea602d1458fdd4579c"   

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()  
    except requests.RequestException as e:
        print("Network or request error:", e)
        return None

    data = resp.json()
   
    if data.get("cod") != 200:
        print("Error:", data.get("message", "Unknown error"))
        return None

    weather = {
        "city": f"{data.get('name')}, {data['sys'].get('country')}",
        "description": data["weather"][0]["description"].title(),
        "temperature_C": data["main"]["temp"],
        "feels_like_C": data["main"].get("feels_like"),
        "humidity": data["main"].get("humidity"),
        "wind_m_s": data["wind"].get("speed")
    }
    return weather

def main():
    city = input("Enter city name: ").strip()
    if not city:
        print("Please enter a city name.")
        return

    info = get_weather(city)
    if not info:
        return

    print("\nWeather for:", info["city"])
    print("Description :", info["description"])
    print(f"Temperature : {info['temperature_C']} °C (feels like {info['feels_like_C']} °C)")
    print("Humidity    :", f"{info['humidity']}%")
    print("Wind speed  :", f"{info['wind_m_s']} m/s")

if __name__ == "__main__":
    main()
