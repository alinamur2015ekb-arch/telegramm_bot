from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboard import main, projekt
from basadata import get_orders
from dotenv import load_dotenv
import os
from anket import Keyn
from aiogram.fsm.context import FSMContext

router = Router()

orders_list = []  
authorized_users = set()  

load_dotenv()
chat_id = os.getenv("ID")
Key = os.getenv("key")

@router.message(CommandStart()) 
async def start_handler(message: Message): 
    await message.reply(
        "Привет! Это <b>Магазин проектов</b> ",
        reply_markup=main,
        parse_mode="HTML"
    )

@router.message(F.text == "Telegramm боты")
async def telegram_bots_handler(message: Message): 
    await message.reply(
        "Магазин проектов: @shop_programmist_bot",
        parse_mode="HTML"
    )


@router.message(F.text == "my_projekt")
async def telegram_bots_handler(message: Message): 
    await message.reply(
        "Мои проекты",
        reply_markup=projekt,
        parse_mode="HTML"
    )


@router.message(F.text == "Telegramm игры")
async def telegram_games_handler(message: Message): 
    await message.reply(
        "Пока нету ",
        reply_markup=main,
        parse_mode="HTML"
    )

@router.message(F.text == "Сайты")
async def websites_handler(message: Message): 
    await message.reply(
        "Пока нету ",
        reply_markup=main,
        parse_mode="HTML"
    )

@router.message(F.text == "Приложения")
async def apps_handler(message: Message): 
    await message.reply(
        "Пока нету ",
        reply_markup=main,
        parse_mode="HTML"
    )

@router.message(F.text == "Игры")
async def games_handler(message: Message): 
    await message.reply(
        "Пока нету",
        reply_markup=main,
        parse_mode="HTML"
    )

@router.message(F.text == "Мой профиль в GitHub")
async def github_profile_handler(message: Message):  
    await message.reply(
        "Ссылка <a href='https://github.com/alinamur2015ekb-arch'>Мой GitHub</a>",  
        reply_markup=main,
        parse_mode="HTML"
    )

@router.message(Command("order"))
async def orders(message: Message):
    global orders_list
    orders_list = await get_orders()

    if not orders_list:
        await message.answer("Заказов нет")
        return
    text = "Заказы:\n\n"
    for order_id, order_description, budget, term in orders_list: 
        text += f"{order_id}. {order_description}\n<code>{budget}</code>\n{term}\n\n"  
    await message.answer(text, parse_mode="HTML")


@router.message(Command("Admin"))
async def admin_auth(message: Message, state: FSMContext):

    if str(message.from_user.id) == chat_id:
        await message.answer("Введите секретный ключ:")
        await state.set_state(Keyn.parol_key)
    else:
        await message.answer("У вас нет прав для этой команды")

@router.message(Keyn.parol_key, F.text)
async def check_key(message: Message, state: FSMContext):
    user_input = message.text.strip()
    
    if user_input == os.getenv("key"): 
        authorized_users.add(message.from_user.id) 
        await message.reply("Ключ принят. Уведомления запущены.")
    else:
        await message.reply("Неверный ключ. Доступ запрещен.")
    
    await state.clear()
