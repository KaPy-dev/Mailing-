
from aiogram import types, Router, Bot,Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,Message
from aiogram.fsm.context import FSMContext
import fsm, panels, random, main,time
from aiogram.types import FSInputFile
from datetime import date
import datetime
from config import *
import mysql.connector
# from PIL import Image
# import PIL,requests
import pathlib 



from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

import os
DIR = pathlib.Path(__file__).parent.resolve()
os.chdir(DIR)


global router
router = Router()



@router.message(Command("start"))
async def StartMaling(SM:Message, state:FSMContext):
    await main.insert_bot.send_message(SM.from_user.id, f"Привет,  <a href= 'tg://user?id={SM.from_user.id}'>{SM.from_user.first_name}</a>\n\n <i>Бот куплет в магазине @PyCraft_shop_bot</i> ", reply_markup= panels.startPanels)
    await state.set_state(fsm.StartGroupe.mainPanels)
    @router.message(fsm.StartGroupe.mainPanels)
    async def Choose(C:Message, state:FSMContext):
        if C.text =="⚙️Настройки пользователей👥":
            from FunctionButton.SettingUser import StartSettingUser
            await StartSettingUser(C, state)
            
            print(9)
        if C.text =="📨Рассылка📩":
            pass

        if C.text =="👥Настройки чатов📝":
            pass

