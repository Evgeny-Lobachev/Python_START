"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
в этой четверти (x и y).

Ввод: значение типа <int>
Вывод: значение типа <str>

Пример:

3
x < 0, y < 0
"""
quarter = int (input("Введите номер четверти:"))
if quarter == 1:
    print ("x > 0, y > 0")
else:
    if quarter == 2:
        print ("x < 0, y > 0")
    else:
        if quarter == 3:
            print ("x < 0, y < 0")
        else:
            if quarter == 4:
                print ("x > 0, y < 0")
            else:
                print ("Ошибка")