"""
Докажите, что выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат.

Вывод: единственное значение типа bool (True либо False)
"""

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            print(x and y or z)