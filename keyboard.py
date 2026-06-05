from aiogram.types import KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import callback_data
from aiogram.types import message

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Мои проекты', callback_data = "my_projekt"), InlineKeyboardButton(text="Сделать заказ", callback_data = "place_order"), InlineKeyboardButton(text="Вступить в мою команду", callback_data = "join_team")]
    ]
)

projekt = ReplyKeyboardMarkup(
    keyboard =[
        [KeyboardButton(text="Telegramm боты"), KeyboardButton(text="Telegramm игры"), KeyboardButton(text="Сайты"),],
        [KeyboardButton(text="Мой профиль в GitHub"), KeyboardButton(text="Приложения"), KeyboardButton(text="Игры")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)