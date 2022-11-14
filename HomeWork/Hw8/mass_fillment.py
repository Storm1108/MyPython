# def create_tuple_list()
#     names =
from random import randint, sample, uniform

from database_control import *


def data_gen():
    dates = []
    for i in range(400):
        day = randint(1, 31)
        if day < 10:
            day = '0' + str(day)
        month = randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        dates.append(f'{randint(2004, 2015)}-{month}-{day}')
    return dates

def data_gen_old():
    dates = []
    for i in range(400):
        day = randint(1, 31)
        if day < 10:
            day = '0' + str(day)
        month = randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        dates.append(f'{randint(1940, 1997)}-{month}-{day}')
    return dates

def time_gen():
    starts = []
    ends = []
    for i in range(100):
        minute = randint(0, 60)
        if minute < 10:
            minute = '0' + str(minute)
        hour = randint(10, 15)
        if hour < 10:
            hour = '0' + str(hour)
        hour = str(hour)
        starts.append(f'{hour}:{minute}')
        ends.append(f'{hour[:1]}{int(hour[1:]) + 1}:{minute}')
    return starts, ends


classes_num = []
classes_lit = []
for i in range(1, 12):
    for j in ["А", "Б"]:
        classes_num.append(i)
        classes_lit.append(j)
starts, ends = time_gen()

with open('FIO.txt', 'r') as data:
    array = data.readlines()
array = list(map(lambda a: tuple(a.strip('\n').split()), array))
surnames, names, fathnames = zip(*array)


sexes = [''.join(sample(('М', 'Ж'), 1)) for i in range(400)]
medials = [round(uniform(2, 5), 2) for i in range(400)]
class_ids = [randint(1, 22) for i in range(400)]

teacher_ids = [randint(1, 20) for i in range(150)]
subjects = [''.join(sample(['Математика', 'Русский язык', 'Физика', 'География', 'Информатика'], 1)) for i in range(100)]
passport_ser = [randint(1000, 9999) for i in range(20)]
passport_num = [randint(100000, 999999) for i in range(20)]
notes = ['-' for i in range(400)]
dates = data_gen()
dates_teachers = data_gen_old()
fathnames = list(map(lambda a: str(a), fathnames))

classes_mas = list(zip(classes_num, classes_lit))
multi_data_load(input_classes, classes_mas)

scholers_mas = list(zip(names, surnames, fathnames, sexes, class_ids, dates, medials, notes))
multi_data_load(input_scholars, scholers_mas)

teachers_mas = list(zip(names, surnames, fathnames, sexes, subjects, passport_ser, passport_num, dates_teachers, dates, notes))
multi_data_load(input_teachers, teachers_mas)


lessons_mas = list(zip(subjects, class_ids, teacher_ids, starts, ends, notes))
multi_data_load(input_lessons, lessons_mas)

print('Done')

input_lessons = "INSERT OR IGNORE INTO lessons (Subject, Class_ID, Teacher_ID," \
                " Lesson_start, Lesson_end, Lesson_notes) VALUES(?, ?, ?, ?, ?, ?);"
input_scholars = "INSERT OR IGNORE INTO scholars (First_name, Family_name, Middle_name, Sex, Class_ID, Birth_date," \
                 " Medial_grades, Disciplanional_marks) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
input_teachers = "INSERT OR IGNORE INTO teachers (First_name, Family_name,Middle_name, Sex, Subject,Passport_ser," \
                 "Passport_num, Birth_date, Date_of_employment, Additional_job) " \
                 " VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
input_classes = "INSERT OR IGNORE INTO classes (Educational_year, Class_Letter) VALUES(?, ?);"
