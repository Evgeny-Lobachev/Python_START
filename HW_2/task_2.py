"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""
n = int(input())
total = []
fact = 1
for i in range(1, n+1):
    fact *= i
    total.append(fact)
print(total)
    


    
    