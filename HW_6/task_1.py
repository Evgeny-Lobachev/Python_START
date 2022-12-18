"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""
def calk(pstr):
    if "+" in  pstr:
        part1, part2 = pstr.split("+", 1)
        result = float(calk(part1)) + float(calk(part2)) 
    elif "-" in  pstr:
        part1, part2 = pstr.split("-", 1)
        result = float(calk(part1)) - float(calk(part2))
    elif "*" in  pstr:
        part1, part2 = pstr.split("*", 1)
        result = float(calk(part1)) * float(calk(part2))
    elif "/" in  pstr:
        part1, part2 = pstr.split("/", 1)
        result = float(calk(part1)) / float(calk(part2))
    else:
        result = float(pstr)
    return result 

string = input("Введите математическое выражение:  ")
string = ''.join(string.split())
string_ = string
while "(" in string_:
    a= string_.split('(', 1)[1]
    while a.find('(') != -1 and a.find('(') < a.find(')'):
        a = a.split('(', 1)[1]
    a = a.split(')')[0]
    string_ = string_.replace('('+a+')', str(calk(a)))
print(f'{string} = {calk(string_)}')