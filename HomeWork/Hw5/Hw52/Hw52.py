# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

def encode(path_in='in_file.txt', path_out='out_file.txt'):
    file = open(path_in, 'r')
    data_in = file.readlines()
    data_in[-1] += "\n"
    encoded = ['']
    for string in data_in:
        count = 0
        previous = string[0]
        for char in string:
            if char == previous:
                count += 1
                previous = char
            else:
                encoded[-1] += str(count) + previous
                count = 1
                previous = char
        encoded.append('')
        encoded[-2] += "\n"
    file.close()
    with open(path_out, 'w') as out:
        out.writelines(encoded)


def decode(path_in='out_file.txt', path_out='result.txt'):
    file = open(path_in, 'r')
    data_in = file.readlines()
    data_in[-1] += "\n"
    decoded = ['']
    for string in data_in:
        number = 0
        for char in string:
            if char.isdigit():
                number = number * 10 + int(char)
            else:
                decoded[-1] += str(char) * number
                number = 0
        decoded[-1] += "\n"
        decoded.append('')

    file.close()
    with open(path_out, 'w') as out:
        out.writelines(decoded)


print("--------------Зашифровка-------------")
path_in = input("Введите имя входящего файл: ")
path_out = input("Введите имя файла с результатом: ")
encode(path_in, path_out)
print("--------------Расшифрофка-------------")
path_in = input("Введите имя входящего файла: ")
path_out = input("Введите имя файла с результатом: ")
decode(path_in, path_out)
