"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""

from random import randint
n = int(input())
list_1 = [randint(0,n) for i in range(n)]
print(list_1)
list_2 = []
for number in list_1:
    if not list_1.count(number) > 1:
        list_2.append(number)
print(list_2) 