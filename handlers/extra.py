from aiogram import types, Dispatcher
from config import bot, ADMIN
import random


async def game(message: types.Message):
    if message.text.startswith('game') and message.from_user.id in ADMIN:
        emojis = ['🎯', '🎳', '🎰', '🎲', '⚽', '️🏀']
        rand_game = random.choice(emojis)
        await bot.send_dice(message.chat.id, emoji=rand_game)
    else:
        try:
            k = int(message.text)
            await bot.send_message(message.chat.id, k * k)
        except:
            await bot.send_message(message.chat.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(game)