import random
import sqlite3
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")
    # db.execute("drop table if exists menu")
    db.execute("CREATE TABLE IF NOT EXISTS menu( "
               "photo TEXT,"
               "name VARCHAR(50) PRIMARY KEY,"
               "description TEXT, "
               "cost REAL)"
               )
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO menu VALUES "
                       "(?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM menu").fetchall()
    random_user = random.choice(result)
    await bot.send_photo(message.from_user.id, random_user[0],
                         caption=f"Name: {random_user[1]}\n"
                                 f"Description: {random_user[2]}\n\n"
                                 f"Cost: {random_user[3]}\n\n")


async def sql_command_all():
    return cursor.execute("SELECT * FROM menu").fetchall()


async def sql_command_delete(name):
    cursor.execute("DELETE FROM menu WHERE name == ?", (name, ))
    db.commit()


async def sql_commands_get_all_id():
    return cursor.execute("SELECT id FROM menu").fetchall()