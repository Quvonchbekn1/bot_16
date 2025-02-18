from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.numbers import menu_start
from loader import dp,bot
from data.config import ADMINS

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Assalomaleykum xush kemabsiz",reply_markup=menu_start)
