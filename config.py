import sqlite3, os, pathlib
global DIR
DIR = pathlib.Path(__file__).parent.resolve()
os.chdir(DIR)


with sqlite3.connect('base.db') as conn:
    cur = conn.cursor()
    cur.execute("SELECT TokenBots FROM System ")
    TOKEN_test =  cur.fetchall()
    if len(TOKEN_test) >0:
        TOKEN = TOKEN_test[0][0]









   

    


