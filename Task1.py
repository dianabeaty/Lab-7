import requests

def get_weather(city):
    api_key = 'f974fbd78c6453f86a260ba929639605'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        country = data['sys']['country']
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        
        print(f"Город: {city}, {country}")
        print(f"Погода в городе {city}: {weather}")
        print(f"Температура: {temperature}°C")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} гПа")
        print(f"Скорость ветра: {wind_speed} м/с")
    else:
        print("Город не найден или произошла ошибка.")

if __name__ == '__main__':
    city_name = "Череповец"
    get_weather(city_name)