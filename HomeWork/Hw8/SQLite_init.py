import sqlite3


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


database_init()


scholar = [('Alex', 'Smith', 'Evgenivich', 'M', '4018', '816756', '2003-06-19', 'Русский язык', '2014-07-16', '-')]
lesson = [('0001', '-', '0001', '10:40', '11:25', '001', 'Математика')]
input_lessons = "INSERT OR IGNORE INTO lessons VALUES(?, ?, ?, ?, ?, ?, ?);"
input_scholars = "INSERT OR IGNORE INTO scholars VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);"
input_teachers = "INSERT OR IGNORE INTO teachers (First_name, Family_name,Middle_name, Sex, Passport_ser," \
                 "Passport_num, Birth_date, Subject, Date_of_employment, Additional_job) " \
                 " VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
input_classes = "INSERT OR IGNORE INTO classes VALUES(?, ?, ?);"

cursor.executemany(input_lessons, lesson)
cursor.executemany(input_teachers, scholar)
connection.commit()
cursor.execute("SELECT * FROM scholars;")
one_result = cursor.fetchall()
print(one_result)
cursor.execute("SELECT * FROM lessons;")
one_result = cursor.fetchone()
print(one_result)
