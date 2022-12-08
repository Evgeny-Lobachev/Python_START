"""
Выведите список простых множителей натурального числа N.

Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""
n = int(input())
new_list = [] 
i = 2
while i <= n:
    if n % i == 0:
        new_list.append(i) 
        n = n // i
    else:
        i+= 1
print(new_list)