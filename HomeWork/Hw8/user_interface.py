from database_control import id_get, database_init
from enter import *


def tuple_create(table_id):
    if table_id == 1:
        subject = input("Введите название предмета: ")
        if id_get('classes', 'Class_ID') == 0:
            class_ID = 0
        else:
            class_ID = enter(int_define, 'Номер класса из таблицы классов: ', True, 1, id_get('classes', 'Class_ID'))
        if id_get('teachers', 'Teacher_ID') == 0:
            teacher_ID = 0
        else:
            teacher_ID = enter(int_define, 'Номер учителя из таблицы учителей: ', True, 1,
                               id_get('teachers', 'Teacher_ID'))
        lesson_start = time_enter('Введите время начала урока: ')
        lesson_end = time_enter('Введите время конца урока: ')
        lesson_notes = input('Введите заметки к уроку или - если их нет:\n')
        return subject, class_ID, teacher_ID, lesson_start, lesson_end, lesson_notes
    elif table_id == 2:
        first_name = input("Введите имя ученика")
        family_name = input('Введите фамилию ученика')
        middle_name = input('Введите отчество ученика')
        sex = input('Введите пол ученика одной буквой (М или Ж)')
        if id_get('classes', 'Class_ID') == 0:
            class_ID = 0
        else:
            class_ID = enter(int_define, 'Номер класса из таблицы классов: ', True, 1, id_get('classes', 'Class_ID'))
        birth_date = date_enter("Введите дату рождения ученика:")
        medial_grades = enter(float_define, 'Введите средние оценки учащегося', True, 2, 5)
        disciplanional_marks = input('Введите заметки по поведению ученика')
        return first_name, family_name, middle_name, sex, class_ID, birth_date, medial_grades, disciplanional_marks
    elif table_id == 3:
        first_name = input("Введите имя учителя")
        family_name = input('Введите фамилию учителя')
        middle_name = input('Введите отчество учителя')
        sex = input('Введите пол учителя одной буквой (М или Ж)')
        subject = input('Введите преподаваемый предмет: ')
        passport_ser = enter(int_define, 'Введите серию паспорта: ', True, 1000, 9999)
        passport_num = enter(int_define, 'Введите номер паспорта: ', True, 100000, 999999)
        birth_date = date_enter('Введите дату рождения учителя: ')
        date_of_employment = date_enter('Введите дату устройства на работу учителя: ')
        additional_job = input("Введите дополнительную должность (Директор, секретарь и т.д.): ")
        return first_name, family_name, middle_name, sex, subject, passport_ser, passport_num, \
               birth_date, date_of_employment, additional_job
    elif table_id == 4:
        educational_year = enter(int_define, 'Введите год обучения: ', True, 1, 11)
        class_letter = input('Введите букву класса: ')
        return educational_year,class_letter


database_init()
print(tuple_create(enter(int_define, 'Номер таблицы: ', True, 1, 2)))
# input_lessons = "INSERT OR IGNORE INTO lessons (Subject, Class_ID, Teacher_ID," \
#                 " Lesson_start, Lesson_end, Lesson_notes) VALUES(?, ?, ?, ?, ?, ?);"
# input_scholars = "INSERT OR IGNORE INTO scholars (First_name, Family_name, Middle_name, Sex, Class_ID, Birth_date," \
#                  " Medial_grades, Disciplanional_marks) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
# input_teachers = "INSERT OR IGNORE INTO teachers (First_name, Family_name,Middle_name, Sex, Subject,Passport_ser," \
#                  "Passport_num, Birth_date, Date_of_employment, Additional_job) " \
#                  " VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
# input_classes = "INSERT OR IGNORE INTO classes (Educational_year, Class_Letter) VALUES(?, ?);"
