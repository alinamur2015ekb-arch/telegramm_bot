from aiogram.fsm.context import FSMContext
from aiogram import F
from hendlers import router
from anket import Join
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from basadate import create_join


@router.message(Command("cansel"))
async def cansel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета удалена")


@router.callback_query(lambda c: c.data == 'join_team')
async def my_projekt(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Заполните анкету. Чтобы удалить воспользуйтесь командой /cansel")
    await callback.message.answer("Введите ваше имя")
    await state.set_state(Join.name)
    await callback.answer()


@router.message(Join.name, F.text)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer("Введите ваш возраст")
    await state.set_state(Join.age)


@router.message(Join.age, F.text)
async def age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Возраст должен быть в формате числа")
        return
    elif int(message.text) > 100 or int(message.text) < 3:
        await message.answer("Возраст должен быть от 3 до 100 лет")
        return
    
    await state.update_data(age=int(message.text))

    await message.answer("Введите ваш стэк")
    await state.set_state(Join.stack)


@router.message(Join.stack, F.text)
async def stack(message: Message, state: FSMContext):
    await state.update_data(stack=message.text)

    await message.answer("Скиньте ссылку на ваше портфолио")
    await state.set_state(Join.portfolio)


@router.message(Join.portfolio, F.text)
async def portfolio(message: Message, state: FSMContext):
    await state.update_data(portfolio=message.text)

    join_anket = await state.get_data()

    await create_join(
        name = join_anket.get("name"),
        age = join_anket.get("age"),
        stack = join_anket.get("stack"),
        portfolio = join_anket.get("portfolio")
    )

    await state.clear()
    await message.reply("Анкета сохранена! Вам скоро ответят")
