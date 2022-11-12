import sqlite3


def database_init():
    global connection, cursor
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS scholars(
    Scholer_ID INT PRIMARY KEY,
    First_name TEXT,
    Family_name TEXT,
    Middle_name TEXT,
    Sex TEXT,
    Birth_date TEXT,
    Medial_grades REAL,
    Disciplanional_marks TEXT,
    Class_ID INT);
""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS lessons(
    Lesson_ID INT PRIMARY KEY,
    Lesson_Notes Text,
    Teacher_ID Int,
    Lesson_start Text,
    Lesson_end Text,
    Class_ID Int,
    Subject	Text);
""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS teachers(
    Teacher_ID	INT PRIMARY KEY,
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
    Class_ID INT PRIMARY KEY,
    Educational_year Int,
    Class_Letter Text
    )""")


database_init()


scholar = [('0001', 'Alex', 'Smith', 'Evgenivich', 'M', '2003-06-19', '4.5', '', '11')]
lesson = [('0001', '-', '0001', '10:40', '11:25', '001', 'Математика')]
input_lessons = "INSERT OR IGNORE INTO lessons VALUES(?, ?, ?, ?, ?, ?, ?);"
input_scholars = "INSERT OR IGNORE INTO scholars VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);"
input_teachers = "INSERT OR IGNORE INTO teachers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
input_classes = "INSERT OR IGNORE INTO classes VALUES(?, ?, ?);"
cursor.executemany(input_lessons, lesson)
cursor.executemany(input_scholars, scholar)
connection.commit()
cursor.execute("SELECT * FROM scholars;")
one_result = cursor.fetchall()
print(one_result)
cursor.execute("SELECT * FROM lessons;")
one_result = cursor.fetchone()
print(one_result)
