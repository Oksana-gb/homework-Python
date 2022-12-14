# 1. Вычислить число pi c заданной точностью d. Число d находится в интервале [1e-1, 1e-10]
# Пример:
# - при d = 0.001, pi = 3.141.
# Примечание:
# Использовать только итерационные алгоритмы вычисления числа pi. Любой на ваш выбор.
# Написать функцию, которая принимает аргумент: точность вычисления числа pi
# Возвращает:
# Вычисленное число pi
# Количество выполненных итераций
# Погрешность вычисления
# Пример вызова функции: - vallis(1e-4) -> (3.141392685883853, 3928, -0.00019996770594010727)


from random import choice


def vallis(d):
    # ряд нилаканта π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...
    pi = 3.00
    num = 2
    count = 0
    for i in range(d):
        pi += 4 / (num * (num+1) * (num+2))
        num += 2
        pi -= 4 / (num * (num+1) * (num+2))
        num += 2
        count += 1

    import math
    print(f"pi c точностью d={d} равно {round(pi,d)}, количество итераций {count}, точность {math.pi - pi} ")


calc_acc = [i for i in range(1, 11)]
d = choice(calc_acc)
vallis(d)
