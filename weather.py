import requests
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        data = response.json()
        current = data["current_condition"][0]
        temp = current["temp_C"]
        weather = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]
        print(f"📍 City: {city}")
        print(f"🌡️ Temperature: {temp} °C")
        print(f"🌥️ Condition: {weather}")
        print(f"💧 Humidity: {humidity}%")
    except Exception as e:
        print("❌ Failed to retrieve weather data.")
        print("Error:", e)

city_name = input("Enter city name: ")
get_weather(city_name)
