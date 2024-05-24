from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.types import Message

import requests
import datetime
#
#
#
#
class Form(StatesGroup):
    city = State()


class weathersend(Form):
 def __init__(self, token, weather_token, uk):
        self.token = token
        self.weather_token = weather_token
        self.uk = uk


async def send_weather(self, message: Message, state: FSMContext) -> None:
        await state.set_state(self.Form.city)
        await message.reply("введіть локацію : ")

async def get_weather(self, message: Message, state: FSMContext) -> None:
    await state.update_data(city=message.text)
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={self.weather_token}&units=metric&lang={self.uk}')
        data = r.json()

        city_name = data['name']
        cur_weather = data['main']['temp']
        feels_like = data['main']['feels_like']
        sky = data['weather'][0]['description']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_day = sunset_timestamp - sunrise_timestamp

        await message.reply(f"согодні в : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                                f"Сьогодні: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                f'Погода в місті: {city_name}\n'
                f'Температура: {cur_weather}°C\n'
                f'Відчувається як: {feels_like}°C\n'
                f'Небо: {sky}\n'
                f'Вологість: {humidity}%\n'
                f'Тиск: {pressure} мм\n'
                f'Швидкість вітру: {wind} м/сек\n'
                f'Схід сонця: {sunrise_timestamp.strftime("%H:%M:%S")}\n'
                f'Захід сонця: {sunset_timestamp.strftime("%H:%M:%S")}\n'
                f'Довжина дня: {length_of_day}\n'
                                )
    except Exception as e:
        await message.reply(f"Я не знаю міст {message.text} ️")

    await state.clear()

