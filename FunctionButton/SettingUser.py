
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
from skills import router


from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

import os
DIR = pathlib.Path(__file__).parent.resolve()
os.chdir(DIR)

async def StartSettingUser(SSU:Message, state:FSMContext):
    await main.insert_bot.send_message(SSU.from_user.id,"⚙️Настройки пользователей👥", reply_markup=panels.settingUsers)
    await state.set_state(fsm.SettingUsers.chooseSetting)
    @router.message(fsm.SettingUsers.chooseSetting)
    async def SettingUsersChoose(SUC:Message, state:FSMContext):
        if SUC.text == "➕":
            from FunctionButton.UsersSetting.AddUsers import AddUsersFunction
            await AddUsersFunction(SUC, state)

        if SUC.text == "✏️":
            pass

        if SUC.text == "🗑":
            pass
        
        if SUC.text == "👥Загрузить базу пользователей🔝":
            pass
        
        if SUC.text == "⚙️Настройки⚙️":
            pass
        
        if SUC.text == "◀️":
            from skills import StartMaling
            await StartMaling(SUC, state)
