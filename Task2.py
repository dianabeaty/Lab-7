import requests
import json

def get_holidays(api_key, country, year):
    url = f'https://holidayapi.com/v1/holidays?key={api_key}&country={country}&year={year}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        holidays_data = response.json()
        
        holidays = holidays_data.get('holidays', [])
        
        print(f"Праздники в {country} на {year} год:")
        for holiday in holidays:
            print(f"Название: {holiday.get('name')}")
            print(f"Дата: {holiday.get('date')}")
            print(f"Тип: {holiday.get('type')}")
            print(f"Регион: {holiday.get('region', 'Не указано')}")
            print(f"Описание: {holiday.get('description', 'Нет описания')}")
            print("-" * 30)
    else:
        print("Ошибка получения данных:", response.status_code)

API_key = '038c1833-3759-4f77-9dc4-45b3b18191f7'
country = 'RU'
year = 2024

get_holidays(API_key, country, year)