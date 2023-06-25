"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""
import random
n = int(input())
list = [random.randint(- n, n) for r in range(n)]
index_l = []
product = 1
with open('HW_2\indexes.txt', encoding='UTF-8') as data:
    for index in data:
        index_l.append(int(index))
for i in range(-n, n):
    if i in index_l:
        product *= list[i]
print(product)