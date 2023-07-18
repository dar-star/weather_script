import requests

def get_weather(city):
    api_key = 'YOU API_KEY'  # Замените на ваш собственный API ключ
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang=ru'
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        print('Город не найден!')
        return

    weather = data['current']['condition']['text']
    temperature = data['current']['temp_c']
    humidity = data['current']['humidity']

    print(f'Погода в городе {city}:')
    print(f'Сейчас {weather}')
    print(f'Температура: {temperature}°C')
    print(f'Влажность: {humidity}%')

city = input('Введите название города: ')
get_weather(city)
