""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. """

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

""" s = str(input('Введите текст для шифровки ')) """
with open('source.txt', 'r') as file:  # Считываем с файла sourse.txt текст который нужно зашифровать.
    s = file.readlines()
print(f'Исходный текст: {s}')
print(f'Кодированный текст: {coding(*s)}') #Выводим кодированный код на экран

with open('decodeFile.txt', 'w') as data:  # Записываем в файл decodeFile кодированный текст
    data.write(coding(*s))








