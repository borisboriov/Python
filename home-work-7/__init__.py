import requests

# Задание 1. Получение данных из публичного API
response = requests.get('https://jsonplaceholder.typicode.com/posts/')
if response.status_code == 200:
    data = response.json()
    print(data[0:5])
else:
    print(f'Ошибка: {response.status_code}')

# Задание 2. Работа с параметрами запроса
city = input()
api_key = "8b0da991cc1780b0f1bf9f28f36e5ecb"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Ошибка: {response.status_code}')

# Задание 3. Создание и обработка POST-запросов & Задание 4. Обработка ошибок и работа с данными
url = f"https://jsonplaceholder.typicode.com/posts"
headers = {
    'Content-Type': 'application/json'
}
json_data = {'username': 'user', 'password': '1234'}

try:
    response = requests.post(url, headers=headers, json=json_data)
    response.raise_for_status()  # Raises HTTPError for 4xx and 5xx
    print(f'Success!, response body: {response.text}')
except requests.exceptions.HTTPError as e:
    if 400 <= response.status_code < 500:
        print(f'Client error (4xx): {e}')
    elif 500 <= response.status_code < 600:
        print(f'Server error (5xx): {e}')
