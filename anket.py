from aiogram.fsm.state import StatesGroup, State


class Order(StatesGroup):
    text = State()
    budget = State()
    term = State()

class Join(StatesGroup):
    name = State()
    age = State()
    stack = State()
    portfolio = State()


class Keyn(StatesGroup):
    parol_key = State()