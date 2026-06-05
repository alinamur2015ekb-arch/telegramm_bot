from aiogram.fsm.context import FSMContext
from aiogram import F
from main.hendlers import router
from forms.anket import Order
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from basadata.basadate import create_orders
import os


chat_id = os.getenv("ID") 


@router.message(Command("cansel"))
async def cansel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета удалена")


@router.callback_query(lambda c: c.data == 'place_order')
async def my_projekt(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Заполните анкету. Чтобы удалить анкету воспользуйтесь командой /cansel")
    await callback.message.answer("Введите ТЗ заказа")
    await state.set_state(Order.text)
    await callback.answer()


@router.message(Order.text, F.text)
async def text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)

    await message.answer("Введите ваш бюджет")
    await state.set_state(Order.budget)


@router.message(Order.budget, F.text)
async def budget(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Бюджет должен быть в формате числа")
        return
    
    await state.update_data(budget=int(message.text))

    await message.answer("Введите сроки")
    await state.set_state(Order.term)


@router.message(Order.term, F.text)
async def term(message: Message, state: FSMContext):
    await state.update_data(term=message.text)
    data = await state.get_data() 

    await message.bot.send_message(
        chat_id=int(chat_id), 
        text=f"📥 *Новый заказ!*\n\n"
             f"👤 Пользователь: @{message.from_user.username}\n"
             f"🆔 ID для связи: {message.from_user.id}\n"
             f"📝 Суть: {data.get('text')}\n"
             f"💰 Бюджет: {data.get('budget')}\n"
             f"📅 Срок: {data.get('term')}",
        parse_mode="Markdown" 
    )

    await create_orders(
        text=data.get("text"), 
        budget=data.get("budget"), 
        term=data.get("term")
    )
 
    await state.clear()
    await message.reply("Анкета сохранена! Вам скоро ответят")

@router.message(Command("send"))
async def send_to_user(message: Message):
    if message.from_user.id != int(chat_id): 
        return

    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.answer("Формат: /send [ID] [сообщение]")
        return
        
    user_id = args[1]
    text_to_send = args[2]  

    try:
        await message.bot.send_message(chat_id=int(user_id), text=text_to_send)
        await message.answer(f"✅ Сообщение отправлено пользователю {user_id}")
    except Exception as e:
        await message.answer(f"❌ Не удалось отправить: {e}")


@router.message(Command("send"))
async def send_to_user(message: Message):
    if message.from_user.id != chat_id:
        return

    args = message.text.split(maxsplit=2)
    
    if len(args) < 3:
        await message.answer("Формат команды: /send [ID] [сообщение]")
        return
        
    user_id = args[1]
    text_to_send = args[2]  

    try:

        await message.bot.send_message(chat_id=user_id, text=text_to_send)
        await message.answer(f"✅ Сообщение успешно отправлено пользователю {user_id}")
    except Exception as e:
        await message.answer(f"❌ Не удалось отправить: {e}")