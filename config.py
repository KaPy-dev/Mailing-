import sqlite3, os, pathlib
from dotenv import load_dotenv

load_dotenv()  # Загружает переменные из .env в os.environ

global DIR
DIR = pathlib.Path(__file__).parent.resolve()
os.chdir(DIR)


with sqlite3.connect('base.db') as conn:
    cur = conn.cursor()
    cur.execute("SELECT TokenBots FROM System ")
    TOKEN_test =  cur.fetchall()
    if len(TOKEN_test) >0:
        TOKEN = TOKEN_test[0][0]



config = (os.getenv("config"))  # "localhost"






   

    


