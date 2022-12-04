"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
import random
n = int(input())
my_list = [round(random.uniform(1, 5), 2) for i in range(n)]
second_list = []

for i in range(len(my_list)):
    second_list.append(my_list[i] - int(my_list[i]))
result = max(second_list) - min(second_list)
print(my_list)
print(round(result, 2))