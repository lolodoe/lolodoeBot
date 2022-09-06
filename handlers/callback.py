from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, dp


# @dp.callback_query_handler(lambda call: call.data == "button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("NEXT", callback_data='button_2')
    markup.add(button_2)

    question = "Кто самый красивый в GeekTech?"
    answers = ['Аблай', 'Байдоолот', 'Эсен', 'Марлен', 'Вова', 'Исмет']
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Учитель",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_3 = InlineKeyboardButton("NEXT", callback_data='button_3')
    markup.add(button_3)

    question = "На каком языке программирования написан этот код?"
    answers = ['Swift', 'HTML', 'Python', 'PascalABC', 'JavaScript', 'C++']

    photo = open("media\\cppphoto.png", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="Сосиска",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_2')