from sqlite3 import *


def ddatabase_init():
    global cursor, conn
    conn = connect('user_database')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS game_datas(
    user_id INT PRIMARY KEY,
    user_name NUMERIC,
    data_0 NUMERIC,
    data_1 NUMERIC,
    data_2 NUMERIC,
    data_3 NUMERIC,
    data_4 NUMERIC,
    data_5 NUMERIC,
    data_6 NUMERIC,
    data_7 NUMERIC,
    data_8 NUMERIC,
    data_9 NUMERIC,
    data_10 NUMERIC,
    data_11 NUMERIC)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS datas(
    user_id INT PRIMARY KEY,
    user_name TEXT,
    value TEXT)""")


ddatabase_init()


def export_game(user_id):
    cursor.execute(f'SELECT data_0, data_1, data_2,data_3 ,data_4, data_5,'
                   f'data_6,data_7,data_8,data_9,data_10, data_11 FROM game_datas WHERE user_id == {user_id}')
    gamedata = list(cursor.fetchone())
    return gamedata


def data_change_game(user_id, user_name, gamedata):
    gamedata = list(gamedata)
    gamedata.insert(0, user_name)
    gamedata.insert(0, user_id)
    gamedata = tuple(gamedata)
    cursor.execute(f'REPLACE INTO game_datas VALUES {gamedata}')
    conn.commit()


def export_calc(user_id):
    cursor.execute(f'SELECT value FROM datas WHERE user_id == {user_id}')
    value = ''.join(cursor.fetchone())
    print(value)
    return value


def data_change_calc(user_id, user_name, value):
    lst = []
    lst.append(value)
    lst.insert(0, user_name)
    lst.insert(0, user_id)
    lst = tuple(lst)
    cursor.execute(f'REPLACE INTO datas VALUES {lst}')
    conn.commit()
