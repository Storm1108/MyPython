def _export():
    with open('file.csv', 'r') as data:
        n = int(input("Введите количество строк которые желаете прочитать: "))
        array = data.readlines()
        for index in range(n):
            if index < len(array):
                print(array[index])


def _import():
    with open('file.csv', 'a') as data:
        data.write(input("Введите данные в формате: Фамилия;Имя;Телефон;Описание") + '\n')


_import()
_export()
