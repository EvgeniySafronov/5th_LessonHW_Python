# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

""" txt = str(input('Введите текст ')) """
txt = 'Абрикосы абвесели весели набв на ветке абв, а старыабв фермер копал абвокоп колодец'
def abc_delete(txt):
    txt = list(filter(lambda x: 'абв' not in x, txt.split()))
    return " ".join(txt)

new_text = abc_delete(txt)
print(new_text)