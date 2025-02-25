# не нашла данные на сайте pochta.ru для 8 варианта, поэтому сделала 7 вариант

import json
import requests


def fetch_holiday_data(api_key, country, year):
    url = f'https://holidayapi.com/v1/holidays?key={api_key}&country={country}&year={year}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка:", response.status_code)
        return None


def display_holidays(holidays, country, year):
    print(f"Праздники в {country} на {year} год:")
    for holiday in holidays:
        print(f"Название: {holiday.get('name')}")
        print(f"Дата: {holiday.get('date')}")
        print(f"Длительность: {holiday.get('lasting', 'Не указано')}")
        print(f"Тип: {holiday.get('type')}")
        print(f"Регион: {holiday.get('region', 'Не указано')}")
        print(f"Описание: {holiday.get('description', 'Не указано')}")
        print("")  # для разделения праздников


def main():
    api_key = "d776cc69-bd3d-4384-bd85-d5dd33b2f58c"
    country = input("Введите код страны: ")  # доступно только: RU
    year = int(input("Введите год: "))  # доступно только: 2024

    holidays_data = fetch_holiday_data(api_key, country, year)

    if holidays_data:
        holidays = holidays_data.get('holidays', [])  # список праздников
        display_holidays(holidays, country, year)

main()
