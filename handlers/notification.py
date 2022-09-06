import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text='Ok')


async def go_to_juma():
    await bot.send_message(chat_id=chat_id, text="ЖУМАААА!")


async def photooo():
    photo = open("media/arang.png", "rb")
    await bot.send_photo(chat_id=chat_id, photo=photo, caption="красапчик")


async def scheduler():
    aioschedule.every().friday.at("00:38").do(go_to_juma)
    aioschedule.every().monday.at("00:56").do(photooo)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(3)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: "бека эс ал" in word.text)