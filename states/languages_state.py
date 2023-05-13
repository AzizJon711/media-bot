from aiogram.dispatcher.filters.state import State, StatesGroup

class Language(StatesGroup):
    english=State()
    russian=State()
    uzbek=State()