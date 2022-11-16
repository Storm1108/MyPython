import sqlite3
from prettytable import from_db_cursor

def database_init():
    global connection, cursor
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS scholars(
    Scholer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name TEXT,
    Family_name TEXT,
    Middle_name TEXT,
    Sex TEXT,
    Birth_date TEXT,
    Medial_grades REAL,
    Disciplanional_marks TEXT,
    Class_ID INTEGER,
    FOREIGN KEY(Class_ID) REFERENCES classes(Class_ID) ON DELETE SET NULL ON UPDATE CASCADE);
""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS lessons(
    Lesson_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Lesson_Notes Text,
    Teacher_ID INTEGER,
    Lesson_start Text,
    Lesson_end Text,
    Class_ID INTEGER,
    Subject	Text,
    FOREIGN KEY(Teacher_ID) REFERENCES teachers(Teacher_ID) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY(Class_ID) REFERENCES classes(Class_ID) ON DELETE SET NULL ON UPDATE CASCADE);
""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS teachers(
    Teacher_ID	INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name	Text,
    Family_name	Text,
    Middle_name	Text,
    Sex	Text,
    Passport_ser	Text,
    Passport_num	Text,
    Birth_date	Text,
    Subject	Text,
    Date_of_employment	Text,
    Additional_job	Text)
""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS classes(
    Class_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Educational_year INTEGER,
    Class_Letter Text)""")


def id_get(table_name, id_name):
    request = f"SELECT {id_name} FROM {table_name};"
    try:
        cursor.execute(request)
        id_list = cursor.fetchall()
        id_max = max(id_list, key=lambda elem: elem[0])
        return int(str(id_max).strip('(').strip(')').strip(','))
    except TypeError:
        print('Непредвиденная ошибка в id_get')
    except ValueError:
        print(f'Пустая таблица {table_name}')
        return int(0)


def data_load(input_message, data):
    database_init()
    cursor.execute(input_message, data)
    connection.commit()


def multi_data_load(input_message, data):
    database_init()
    cursor.executemany(input_message, data)
    connection.commit()


def export(export_message):
    cursor.execute(export_message)
    result = from_db_cursor(cursor)
    return result

database_init()
