import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import logging, sqlite3,os, pathlib
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import skills
from aiogram.client.bot import DefaultBotProperties
import multiprocessing
from config import *
import time

# 


# global insert_bot,insert_dp

insert_bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
insert_dp =  Dispatcher(storage=MemoryStorage())

async def main():
   bot = insert_bot
   dp =  Dispatcher(storage=MemoryStorage())
   dp.include_router(skills.router)
   
   await bot.delete_webhook(drop_pending_updates=True)
   await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
   # time_checking_ = multiprocessing.Process(target=time_resert)
   # time_checking_.start()
   # if not time_checking_.is_alive():
   #    # id_dec = []
   #    print("Error: Bot is not started, please check your token and try again. Exiting... ")
   logging.basicConfig(
      level=logging.INFO,
      format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
      handlers=[logging.StreamHandler()]  # Вывод в консоль
   )
   logger = logging.getLogger(__name__)
   logging.basicConfig(level=logging.INFO)
   asyncio.run(main())


