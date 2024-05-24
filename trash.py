# import requests
# import datetime
#
# import kb
#
# import asyncio
# import logging
# import sys
# from os import getenv
#
#
# from aiogram.filters import Command, CommandStart
# from aiogram import Bot, Dispatcher, Router, types
# from aiogram.enums import ParseMode
# from aiogram.types import Message
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
#
# from comands import  set_comands
#
#
#
# WEATHER_TOKEN = 'eb103106740f3650d6302877bce1b8bc'
# uk= 'uk'
# TOKEN = getenv("BOT_TOKEN")
#
#
# dp = Dispatcher()
#
#
#
# form_router = Router()
#
#
# class Form(StatesGroup):
#     city = State()
#
#                  # команда старт
#
# @form_router.message(CommandStart())
# async def command_start_handler(message: Message):
#
#     await message.reply("Цей телеграм-бот призначений для отримання погоди у певному місті.\n Щоб розпочати напишіть команду /weather ",)
#
#
#                  # команда погода
#
# @form_router.message(Command("weather"))
# async def send_weather(message: Message, state: FSMContext) -> None:
#     await state.set_state(Form.city)
#     await message.reply("введіть локацію : ")
#
#
#                 # вивелення погоди
# @form_router.message(Form.city)
# async def get_weather(message: Message, state: FSMContext) -> None:
#     await state.update_data(city=message.text)
#
#     try:
#         r = requests.get(
#             f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={WEATHER_TOKEN}&units=metric&lang={uk}')
#         data = r.json()
#
#         citys = data['name']
#         cur_weather = data['main']['temp']
#         feels_like = data['main']['feels_like']
#         sky = data['weather'][0]['description']
#         humidity = data['main']['humidity']
#         pressure = data['main']['pressure']
#         wind = data['wind']['speed']
#
#         sunrise_timestamp = datetime.datetime.fromtimestamp(
#             data["sys"]["sunrise"])
#         sunset_timestamp = datetime.datetime.fromtimestamp(
#             data["sys"]["sunset"])
#
#         lenght_of_day = datetime.datetime.fromtimestamp(
#             data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
#             data["sys"]["sunrise"])
#         await message.reply(f"согодні в : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
#                             f'погода в місті {citys}\n'
#                             f'температура: {cur_weather}°C\n'
#                             f'відчувається, як: {feels_like}°C\n'
#                             f'небо: {sky}\n'
#                             f'вологість: {humidity}%\n'
#                             f'тиск: {pressure}мм\n'
#                             f'швидкість вітру: {wind}м/сек\n'
#                             # f'Sunrise at {sunrise_timestamp}\n'
#                             # f'Sunset at {sunset_timestamp}\n'
#                             f'довжина дня:{lenght_of_day}'
#                             )
#     except Exception as e:
#         await message.reply(f"Я не знаю міст {message.text} ️")
#
#     await state.clear()
#
#     #
#
# async def main() -> None:
#     bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
#     dp = Dispatcher()
#     dp.include_router(form_router)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())
#
#
