"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""

n = float (input())
str_n = str (n)
str_n = str_n.replace ('.', '')
lst_n = list (str_n)
lst_num = map (int, lst_n)
s = sum (lst_num)
print (s)