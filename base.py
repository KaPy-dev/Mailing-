import sqlite3, os, pathlib
global DIR
DIR = pathlib.Path(__file__).parent.resolve()
os.chdir(DIR)
with sqlite3.connect('base.db') as conn:
    cur = conn.cursor()


    cur.execute("""CREATE TABLE IF NOT EXISTS User(
    KEY INT PRIMARY KEY, 
    ApiID INT,
    ApiHash BIGINT,
    PhoneNumber BIGINT,
    NameUser TEXT
    )""")


    cur.execute("""CREATE TABLE IF NOT EXISTS Mailing(
    IdMailing INT PRIMARY KEY,
    idChats TEXT,
    TextMailig TEXT,
    TimerMinuts INT,
    idUsersSent TEXT
    )""")


    cur.execute("""CREATE TABLE IF NOT EXISTS Chats(
        IDChats BIGINT,
        IDUsersSent TEXT
    )""")


    cur.execute("""CREATE TABLE IF NOT EXISTS System(
        OwnerId BIGINT,
        TokenBots TEXT
    )""")



   

    


