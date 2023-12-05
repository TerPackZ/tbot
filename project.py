import telebot
import requests

bot = telebot.TeleBot('6908018721:AAGPMgXJPmnD96M198kzRtTt_UHvHPD4RG4')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, text=f'Привет, {message.from_user.first_name}\nВведи название города:', parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def weather(message):
  city = message.text
  url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
  weather_data = requests.get(url).json()
  print(weather_data)

  temperature = round(weather_data['main']['temp'])
  temperature_feels = round(weather_data['main']['feels_like'])
  humidity = round(weather_data['main']['humidity'])
  wind_speed = round(weather_data['wind']['speed'])
  main_temp = round(weather_data['main']['temp'])


  if main_temp < 0:
      w_now = '❄️ *Температура:* ' + str(temperature) + ' °C'
      w_feels = '⛄️ *По ощущению:* ' + str(temperature_feels) + ' °C'

  elif main_temp > 0:
      w_now = '☀️ *Сейчас в городе:* ' + city + ' ' + str(temperature) + ' °C'
      w_feels = '🫠 *Ощущается как:* ' + str(temperature_feels) + ' °C'

  if wind_speed < 5:
      rec = '✅ Погода хорошая, ветра почти нет'
  elif wind_speed < 10:
      rec = '🤔 На улице ветрено, оденьтесь чуть теплее'
  elif wind_speed < 20:
      rec = '❗️ Ветер очень сильный, будьте осторожны, выходя из дома'
  else:
      rec = '❌ На улице шторм, на улицу лучше не выходить'

  w_hum = '💧 *Влажность воздуха:* ' + str(humidity) + ' %'
  speed = '💨 *Скорость ветра:* ' +str(wind_speed) + ' м/с'
  bot.send_message(message.from_user.id, f'{w_now}\n\n{w_feels}\n\n{w_hum}\n\n{speed}\n\n{rec}', parse_mode='Markdown')

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print('Сработало исключение!')