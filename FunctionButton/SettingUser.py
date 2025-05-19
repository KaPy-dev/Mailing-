
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
            await main.insert_bot.send_message(SUC.from_user.id, "Все денные можно будет изменить после регистрации пользователя \n\n\nВведите ApiId пользователя:",reply_markup=panels.ReplyKeyboardRemove())
            await state.set_state(fsm.AddUsers.ApiId)
            @router.message(fsm.AddUsers.ApiId)
            async def ApiidSent(AIS:Message, state:FSMContext):
                global APIID
                APIID = AIS.text
                await main.insert_bot.send_message(AIS.form_user.id, "Введите AipHash:")
                await state.set_state(fsm.AddUsers.ApiHash)
                @router.message(fsm.AddUsers.ApiHash)
                async def ApiHashSent(AHS:Message, state:FSMContext):
                    APIHASH = AHS.text
                    await main.insert_bot.send_message(AHS.frpm_user.id, "Введите номер телефона пользователя: ")
                    await state.set_state(fsm.AddUsers.NumberPhone)
                    @router.message(fsm.AddUsers.NumberPhone)
                    async def NumberUsersSent(NUS:Message, state:FSMContext):
                        NUMBERPHONE = NUS.text
                        await main.insert_bot.send_message(AHS.from_user.id,"Введите имя пользователя (Пример: Криснова Олеся, Кирилл и тп):")
                        await state.set_state(fsm.AddUsers.NameUsers)
                        @router.message(fsm.AddUsers.NameUsers)
                        async def UsersNamePersonAdd(UNPA:Message, state:FSMContext):
                            NmaeUsers = UNPA.text
                            await main.insert_bot.send_message(UNPA.from_user.id, "Информация о пользователя введена успешно !")
                            

        if SUC.text == "✏️":
            pass
        if SUC.text == "🗑":
            pass
        if SUC.text == "👥Загрузить базу пользователей🔝":
            pass
        if SUC.text == "⚙️Настройки⚙️":
            pass
        if SUC.text == "◀️":
            pass
