import json  # библиотека для работы с json форматом
import requests  # библиотека для выполнения HTTP-запросов


def get_weather_data(city_name):
    api_key = "fc27212dd5eadaf13d9b6f2ca842de17"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")

        return None

def display_weather_info(weather_data):
    if weather_data:
        city_name = weather_data["name"]
        weather = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        pressure = weather_data["main"]["pressure"]
        wind_speed = weather_data["wind"]["speed"]

        print(f"Погода в городе {city_name}:")
        print(f"- Описание: {weather}")
        print(f"- Температура: {temperature}°C")
        print(f"- Влажность: {humidity}%")
        print(f"- Давление: {pressure} гПа")
        print(f"- Скорость ветра: {wind_speed} м/с")
    else:
        print("Не удалось получить информацию о погоде.")

def main():
    city_name = input("Введите город: ")
    weather_data = get_weather_data(city_name)
    display_weather_info(weather_data)

main()