# from aiogram.types import (
#     ReplyKeyboardMarkup,
#     KeyboardButton,
#     InlineKeyboardMarkup,
#     InlineKeyboardButton
# )
# main_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="/weather"),
#             KeyboardButton(text="/start"),
#         ],
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=True,
#     input_field_placeholder="виберіть дію з меню",
#     selective=True,
#
# )
# # links_kb = InlineKeyboardMarkup(
# #     inline_keyboard=[
# #         [
# #            InlineKeyboardButton(text="погода сьогодні", callback_data="weather_today"),
# #            InlineKeyboardButton(text="погода заватра", callback_data="weather_tomorrow")
# #
# #
# #         ]
# #     ]
# #
# # )


# class WeatherBot():
#
#
#     def __init__(self, token, weather_token, uk, ):
#         self.token = token
#         self.weather_token = weather_token
#         self.uk = uk
#         self.bot = Bot(token=self.token, parse_mode=ParseMode.HTML)
#         self.dp = Dispatcher()
#         self.router = Router()
#
#
#         # Register command handlers
#
#
#
#         self.router.message.register(self.command_start_handler, CommandStart())
#         self.router.message.register(self.send_weather, Command("weather"))
#         self.router.message.register(self.get_weather, )
#
#         self.dp.include_router(self.router)
#
#     async def command_start_handler(self, message: Message,bot:Bot):
#         # await set_comands(bot)
#         await message.reply(
#             "Цей телеграм-бот призначений для отримання погоди у певному місті.\nЩоб розпочати, напишіть команду /weather",
#         )
#
#     async def send_weather(self, message: Message, state: FSMContext):
#         await state.set_state(Form.city)
#         await message.reply("Введіть локацію:")
#
#
#     async def get_weather(self, message: Message, state: FSMContext):
#         city = message.text
#         await state.update_data(city=city)
#         try:
#             r = requests.get(
#                 f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_token}&units=metric&lang={self.uk}'
#             )
#             data = r.json()
#
#             city_name = data['name']
#             cur_weather = data['main']['temp']
#             feels_like = data['main']['feels_like']
#             sky = data['weather'][0]['description']
#             humidity = data['main']['humidity']
#             pressure = data['main']['pressure']
#             wind = data['wind']['speed']
#
#             sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
#             sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
#             length_of_day = sunset_timestamp - sunrise_timestamp
#
#             await message.reply(
#                 f"Сьогодні: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
#                 f'Погода в місті: {city_name}\n'
#                 f'Температура: {cur_weather}°C\n'
#                 f'Відчувається як: {feels_like}°C\n'
#                 f'Небо: {sky}\n'
#                 f'Вологість: {humidity}%\n'
#                 f'Тиск: {pressure} мм\n'
#                 f'Швидкість вітру: {wind} м/сек\n'
#                 f'Схід сонця: {sunrise_timestamp.strftime("%H:%M:%S")}\n'
#                 f'Захід сонця: {sunset_timestamp.strftime("%H:%M:%S")}\n'
#                 f'Довжина дня: {length_of_day}\n'
#             )
#         except Exception as e:
#             await message.reply(f"Я не знаю місто {city} ️")
#
#         await state.clear()
#
#     async def start(self):
#         await self.dp.start_polling(self.bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     WEATHER_TOKEN = getenv("WEATHER_TOKEN") or 'eb103106740f3650d6302877bce1b8bc'
#     TOKEN = getenv("BOT_TOKEN")
#     uk = 'uk'
#     form_router = Router()
#     dp=Dispatcher()
#
#
#     bot = WeatherBot(TOKEN, WEATHER_TOKEN, uk)
#     asyncio.run(bot.start())


#__________________

## class Form(StatesGroup):
#         city = State()
# async def send_weather(self, message: Message, state: FSMContext):
#     await state.set_state(Form.city)
#     await message.reply("Введіть локацію:")
#
# async def get_weather(self, message: Message, state: FSMContext):
#         city = message.text
#         await state.update_data(city=city)
#         try:
#             r = requests.get(
#                 f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_token}&units=metric&lang={self.uk}'
#             )
#             data = r.json()
#
#             city_name = data['name']
#             cur_weather = data['main']['temp']
#             feels_like = data['main']['feels_like']
#             sky = data['weather'][0]['description']
#             humidity = data['main']['humidity']
#             pressure = data['main']['pressure']
#             wind = data['wind']['speed']
#
#             sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
#             sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
#             length_of_day = sunset_timestamp - sunrise_timestamp
#
#             await message.reply(
#                 f"Сьогодні: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
#                 f'Погода в місті: {city_name}\n'
#                 f'Температура: {cur_weather}°C\n'
#                 f'Відчувається як: {feels_like}°C\n'
#                 f'Небо: {sky}\n'
#                 f'Вологість: {humidity}%\n'
#                 f'Тиск: {pressure} мм\n'
#                 f'Швидкість вітру: {wind} м/сек\n'
#                 f'Схід сонця: {sunrise_timestamp.strftime("%H:%M:%S")}\n'
#                 f'Захід сонця: {sunset_timestamp.strftime("%H:%M:%S")}\n'
#                 f'Довжина дня: {length_of_day}\n'
#             )
#         except Exception as e:
#             await message.reply(f"Я не знаю місто {city} ️")
#
#         await state.clear()
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     WEATHER_TOKEN = getenv("WEATHER_TOKEN") or 'eb103106740f3650d6302877bce1b8bc'
#     TOKEN = getenv("BOT_TOKEN")
#     uk = 'uk'
#
#     bot = WeatherBot(TOKEN, WEATHER_TOKEN, uk)
#     asyncio.run(bot.start())