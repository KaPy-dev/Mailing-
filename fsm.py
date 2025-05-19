from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup

class StartGroupe(StatesGroup):
    mainPanels = State()


class SettingUsers(StatesGroup):
    chooseSetting = State()



class AddUsers(StartGroupe):
    ApiId = State()
    ApiHash = State()
    NumberPhone = State()
    NameUsers = State()