from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

menu_start=ReplyKeyboardMarkup(
    keyboard=[
        [        
            KeyboardButton(text="random son"),
            KeyboardButton(text="random/math"),
        ],
        [
            KeyboardButton(text="random/date"),
            KeyboardButton(text="random/year"),
        ],
    ],
    resize_keyboard=True
)