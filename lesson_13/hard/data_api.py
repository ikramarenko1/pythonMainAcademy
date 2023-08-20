# Обробка даних з API:
# Напишіть програму, яка отримує дані з публічного API, наприклад, з веб-сервісу,
# який надає інформацію про погоду. Врахуйте можливість виникнення помилок під час
# з'єднання з API або некоректної відповіді. Обробте ці помилки та виведіть відповідні повідомлення.
import requests
import time
import json

API_TOKEN = 'f1ec8e17f146dc54a599b2e9ecc8530a'


def get_weather_data(city):
    try:
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_TOKEN}&units=metric&lang=ua')

        # Код нижче розробляв для телеграм бота з погодою
        if response.status_code == 200:
            data = json.loads(response.text)

            result = f'На поточний момент у населеному пункті {data["name"]}:\n\n'

            weather_main = data['weather'][0]['main']
            if weather_main == 'Clear':
                result += '☀️ '
            elif weather_main == 'Clouds':
                result += '☁️ '
            elif weather_main == 'Rain':
                result += '🌧 '
            elif weather_main == 'Drizzle':
                result += '💧 '
            elif weather_main == 'Thunderstorm':
                result += '⛈ '
            elif weather_main == 'Snow':
                result += '❄️ '
            elif weather_main == 'Mist' or weather_main == 'Smoke':
                result += '😶‍🌫 '

            result += f'{data["weather"][0]["description"].capitalize()}\n'

            temperature = int(data["main"]["temp"])
            feels_like = int(data["main"]["feels_like"])
            result += f'🌡️ Температура повітря - {temperature} °C\n'

            if feels_like > 20:
                result += '🥵 '
            elif 0 <= feels_like <= 20:
                result += '🙂 '
            else:
                result += '🥶 '

            result += f'На вулиці відчувається як {feels_like} °C\n'

            result += f'🌬 Швидкість вітру - {data["wind"]["speed"]} м/с\n'

            sunrise_unix = data['sys']['sunrise']
            sunset_unix = data['sys']['sunset']
            sunrise_time = time.strftime("%H:%M", time.localtime(sunrise_unix))
            sunset_time = time.strftime("%H:%M", time.localtime(sunset_unix))

            result += f'🌅 Час сходу сонця: {sunrise_time}\n'
            result += f'🌇 Час заходу сонця: {sunset_time}\n'

            return result

        else:
            raise Exception('Виникла помилка при зборі інформації. Повторіть спробу.')

    except requests.ConnectionError:
        return "Помилка з'єднання до API."
    except requests.Timeout:
        return "Виникла помилка через перевищення часу очікування."
    except requests.RequestException as e:
        return f"Запит завершився з помилкою: {e}"
    except Exception as e:
        return e


city = input('Введiть назву населеного пункту: ')
print(get_weather_data(city))
