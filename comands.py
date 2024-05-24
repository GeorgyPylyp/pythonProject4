from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_comands(bot:Bot):
    commands=[
        BotCommand(
            command='start',
            description='Запустити бота'
        ),
        BotCommand(
            command='weather',
            description='дізнатись погоду'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault)