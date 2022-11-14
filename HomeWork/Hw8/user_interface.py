from database_control import id_get
from enter import *

def tuple_create(table_id):
    if table_id == 1:
        subject = input("Введите название предмета: ")
        class_ID = enter(int_define, 'Номер класса из таблицы классов: ', True, 1, id_get('classes','Class_ID'))
        teacher_ID = enter(int_define, 'Номер учителя из таблицы учителей: ', True, 1, id_get('teachers','Teacher_ID'))
        lesson_start = time_enter('Введите время начала урока: ')
        lesson_end = time_enter('Введите время конца урока: ')
        lesson_notes = input('Введите заметки к уроку или - если их нет:\n')
    if table_id == 2:
        First_name =
        Family_name =
        Middle_name
        Sex
        Class_ID
        Birth_date
        Medial_grades
        Disciplanional_marks






input_lessons = "INSERT OR IGNORE INTO lessons (Subject, Class_ID, Teacher_ID," \
                " Lesson_start, Lesson_end, Lesson_notes) VALUES(?, ?, ?, ?, ?, ?);"
input_scholars = "INSERT OR IGNORE INTO scholars (First_name, Family_name, Middle_name, Sex, Class_ID, Birth_date," \
                 " Medial_grades, Disciplanional_marks) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
input_teachers = "INSERT OR IGNORE INTO teachers (First_name, Family_name,Middle_name, Sex, Subject,Passport_ser," \
                 "Passport_num, Birth_date, Date_of_employment, Additional_job) " \
                 " VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
input_classes = "INSERT OR IGNORE INTO classes (Educational_year, Class_Letter) VALUES(?, ?);"
