
from aiogram import types, Router, Bot,Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,Message,ReplyKeyboardRemove, ReplyKeyboardMarkup
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


startPanels = ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='⚙️Настройки пользователей👥'),
        ],
        [
            types.KeyboardButton(text='📨Рассылка📩'),
            ],
        [
            types.KeyboardButton(text='👥Настройки чатов📝'),

        ]
    ],resize_keyboard=True
)

settingUsers = ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text=' ➕'),
            types.KeyboardButton(text=' ✏️'),
            types.KeyboardButton(text=' 🗑'),
        ],
        [
            types.KeyboardButton(text=' 👥Загрузить базу пользователей🔝')
        ],
        [
            types.KeyboardButton(text='⚙️Настройки⚙️')
        ],
        [
            types.KeyboardButton(text='◀️')
        ]
    ], resize_keyboard=True
) 

