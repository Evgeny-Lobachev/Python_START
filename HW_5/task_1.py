"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""
s = input()

print(' ' .join(list(filter(lambda str_: not all(i in str_.lower() for i in 'абв'), s.split()))))
