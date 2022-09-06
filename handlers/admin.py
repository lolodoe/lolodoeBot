from aiogram import types, Dispatcher
from config import ADMIN, bot, dp
from database.bot_db import sql_commands_get_all_id


async def reklama(message: types.Message):
    if message.from_user.id in ADMIN:
        result = await sql_commands_get_all_id()
        for id in result:
            await bot.send_message(id[0], message.text[3:])
    else:
        await message.answer("Ты не мой БОСС!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(reklama, commands=['reklama'])