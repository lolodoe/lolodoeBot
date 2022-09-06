from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import decouple

storage = MemoryStorage()

TOKEN = decouple.config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = [5319788233]
