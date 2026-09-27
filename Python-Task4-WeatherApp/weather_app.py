import requests

print("Basic Weather App")

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        humidity = current["humidity"]
        condition = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]

        print("\nWeather Information")
        print("-------------------")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", condition)
        print("Wind Speed:", wind_speed, "km/h")

    else:
        print("Could not get weather information.")

except requests.exceptions.RequestException:
    print("Error: Unable to connect to the weather service.")

except (KeyError, IndexError, ValueError):
    print("Error: Unable to read weather data.")