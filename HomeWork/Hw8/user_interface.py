from database_control import id_get, database_init, data_load, export
from exceptions import *


def data_input(table_id):
    if table_id == 1:
        subject = input("Введите название предмета: ")
        if id_get('classes', 'Class_ID') == 0:
            class_ID = 0
        else:
            data_export(4)
            class_ID = enter(int_define, 'Номер класса из таблицы классов: ', True, 1, id_get('classes', 'Class_ID'))
        if id_get('teachers', 'Teacher_ID') == 0:
            teacher_ID = 0
        else:
            data_export(3)
            teacher_ID = enter(int_define, 'Номер учителя из таблицы учителей: ', True, 1,
                               id_get('teachers', 'Teacher_ID'))
        lesson_start = time_enter('Введите время начала урока: ')
        lesson_end = time_enter('Введите время конца урока: ')
        lesson_notes = input('Введите заметки к уроку или - если их нет:\n')
        data_load(input_lessons, (subject, class_ID, teacher_ID, lesson_start, lesson_end, lesson_notes))
    elif table_id == 2:
        first_name = input("Введите имя ученика")
        family_name = input('Введите фамилию ученика')
        middle_name = input('Введите отчество ученика')
        sex = input('Введите пол ученика одной буквой (М или Ж)')
        if id_get('classes', 'Class_ID') == 0:
            class_ID = 0
        else:
            data_export(4)
            class_ID = enter(int_define, 'Номер класса из таблицы классов: ', True, 1, id_get('classes', 'Class_ID'))
        birth_date = date_enter("Введите дату рождения ученика:")
        medial_grades = enter(float_define, 'Введите средние оценки учащегося', True, 2, 5)
        disciplanional_marks = input('Введите заметки по поведению ученика')
        data_load(input_scholars, (first_name, family_name, middle_name, sex, class_ID,
                                   birth_date, medial_grades, disciplanional_marks))
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
        data_load(input_teachers, (first_name, family_name, middle_name, sex, subject, passport_ser, passport_num, \
                                   birth_date, date_of_employment, additional_job))
    elif table_id == 4:
        educational_year = enter(int_define, 'Введите год обучения: ', True, 1, 11)
        class_letter = input('Введите букву класса: ')
        data_load(input_classes, (educational_year, class_letter))


def data_export(table_id):
    if table_id == 1:
        subj_num = enter(int_define, '1: Математика\n'
                                     '2: Русский язык\n'
                                     '3: Физика\n'
                                     '4: География\n'
                                     '5: Информатика\n'
                                     'Введите номер предмета изучаемого на уроке: ', True, 1, 5)

        data = export(
            f'SELECT Subject, (SELECT Educational_year FROM classes WHERE classes.Class_ID == lessons.Class_ID),'
            f'(SELECT Class_Letter FROM classes WHERE classes.Class_ID == lessons.Class_ID), '
            f'(SELECT Family_name FROM teachers WHERE teachers.Teacher_ID == lessons.Teacher_ID), '
            f'(SELECT First_name FROM teachers WHERE teachers.Teacher_ID == lessons.Teacher_ID), '
            f'(SELECT Middle_name FROM teachers WHERE teachers.Teacher_ID == lessons.Teacher_ID),'
            f' Lesson_start, Lesson_end, Lesson_notes FROM lessons WHERE Subject == "{subj_dikt[subj_num]}";')
        data.field_names = ['Предмет', 'Год обучения', 'Буква класса', 'Фамилия учителя', 'Имя учителя',
                            'Отчество учителя', 'Начало урока', 'Конец урока', 'Заметки к уроку']
        data.sortby = "Год обучения"
        print(data)
    if table_id == 2:
        year_num = enter(int_define, 'Введите год обучения ученика: ', True, 1, 11)
        letter = input("Ввведите букву класса ученика: ").upper()
        data = export(
            f'SELECT Family_name, First_name,  Middle_name, Sex, '
            f'(SELECT Educational_year FROM classes WHERE classes.Class_ID == scholars.Class_ID),'
            f'(SELECT Class_Letter FROM classes WHERE classes.Class_ID == scholars.Class_ID), '
            f'Birth_date, Medial_grades, Disciplanional_marks FROM scholars WHERE Class_ID == '
            f'(SELECT Class_ID FROM classes WHERE Class_Letter == "{letter}" AND Educational_year == "{year_num}");')
        data.field_names = ['Фамилия', 'Имя', 'Отчество', 'Пол', 'Год обучения', 'Буква класса', 'Дата рождения',
                            'Сред. оценки', 'Отметки о поведении']
        data.sortby = "Фамилия"
        print(data)
    if table_id == 3:
        data = export("SELECT Teacher_ID, Family_name,First_name, Middle_name, Sex, Subject,Passport_ser,"
                      "Passport_num, Birth_date, Date_of_employment, Additional_job FROM teachers")
        data.field_names = ['ID учителя', 'Фамилия', 'Имя', 'Отчество', 'Пол', 'Предмет обучения', 'Серия паспорта', 'Номер паспорта',
                            'Дата рождения', 'Дата трудоустройства', 'Доп. должность']

        data.sortby = "Фамилия"
        print(data)
    if table_id == 4:
        data = export("SELECT * FROM classes")
        data.field_names = ['ID класса', 'Год обучения', 'Буква класса']
        data.sortby = 'Год обучения'
        print(data)

def main():
    while True:
        menu = enter(int_define, '1 - Получить данные из базы данных\n'
                                 '2 - Загрузить данные в базу данных\n'
                                 '3 - Изменить данные в базе данных\n'
                                 '4 - Выйти из программы\n'
                                 'Введите номер пункта меню: ', True, 1, 4)
        if menu == 1:
            menu_temp = enter(int_define, '1 - Таблица уроков\n'
                                     '2 - Таблица учеников\n'
                                     '3 - Таблица учителей\n'
                                     '4 - Таблица классов\n'
                                     '5 - Назад\n'

                                     'Введите номер пункта меню: ', True, 1, 5)
            if menu_temp != 5:
                data_export(menu_temp)
            menu_temp = 0

        if menu == 2:
            menu_temp = enter(int_define, '1 - Таблица уроков\n'
                                     '2 - Таблица учеников\n'
                                     '3 - Таблица учителей\n'
                                     '4 - Таблица классов\n'
                                     '5 - Назад\n'

                                     'Введите номер пункта меню: ', True, 1, 5)
            if menu_temp !=5:
                data_input(menu_temp)
                menu_temp = 0
        if menu == 3:
            print('Еще не реализовано')
        if menu == 4:
            exit()


subj_dikt = {1: 'Математика', 2: 'Русский язык', 3: 'Физика', 4: 'География', 5: 'Информатика'}

input_lessons = "INSERT OR IGNORE INTO lessons (Subject, Class_ID, Teacher_ID," \
                " Lesson_start, Lesson_end, Lesson_notes) VALUES(?, ?, ?, ?, ?, ?);"
input_scholars = "INSERT OR IGNORE INTO scholars (First_name, Family_name, Middle_name, Sex, Class_ID, Birth_date," \
                 " Medial_grades, Disciplanional_marks) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
input_teachers = "INSERT OR IGNORE INTO teachers (First_name, Family_name,Middle_name, Sex, Subject,Passport_ser," \
                 "Passport_num, Birth_date, Date_of_employment, Additional_job) " \
                 " VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
input_classes = "INSERT OR IGNORE INTO classes (Educational_year, Class_Letter) VALUES(?, ?);"
database_init()