import requests
from datetime import datetime

def fetch_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data:", response.text)
        return None

def fetch_forecast_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching forecast data:", response.text)
        return None

def display_current_weather(weather_data):
    if weather_data:
        print("\nCurrent Weather Conditions:")
        print("----------------------------")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Visibility: {weather_data['visibility']} meters")
        print(f"Cloudiness: {weather_data['clouds']['all']}%")
        print(f"Sunrise: {datetime.utcfromtimestamp(weather_data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Sunset: {datetime.utcfromtimestamp(weather_data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')}")

def display_forecast(forecast_data):
    if forecast_data:
        print("\nForecast for the next 5 days:")
        print("----------------------------")
        for forecast in forecast_data['list']:
            date = datetime.utcfromtimestamp(forecast['dt']).strftime('%Y-%m-%d %H:%M:%S')
            temperature = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            print(f"Date: {date}, Temperature: {temperature}°C, Weather: {description}")

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    print("Fetching current weather data...")
    current_weather_data = fetch_weather_data(api_key, city)
    display_current_weather(current_weather_data)

    print("\nFetching forecast data...")
    forecast_data = fetch_forecast_data(api_key, city)
    display_forecast(forecast_data)

if __name__ == "__main__":
    main()
