# 4. Задайте список из элементов, заполненных числами из промежутка [-N, N]. Задайте два числа - позиции(индексы) в исходном списке это границы диапазона.
# Найдите произведение элементов списка в указанном диапазоне индексов
# Пример:N = 6
# Пример списка чисел: [-2, -5, 4, 1, 4, 1, 2, -5, -3, 0, -6, -6, 5]
# границы диапазона: 2, 5
# Произведение для [4, 1, 4, 1] равно 16
# Примечание: Границы диапазона вводятся пользователем, надо корректно учесть, что они могут быть некорректными: больше длины списка, меньше нуля, первый больше второго и т.п.

import random


def edge(n, a):
    num = int(input('введите число '))
    if num >= n*2 or num < 0:
        print('данное значение выходит за перделы списка')
        return edge(n, a)
    elif num > num or num < a:
        print('данное значение меньше первой границы ')
        return edge(n, a)
    else:
        return num


n = int(input('введите число '))
print('поочередно введите границы диапазона')
s = edge(n, 0)
e = edge(n, s)

list = [random.randint(-n, n) for _ in range(n*2)]
print(list)
sum = 1
print(list[s:e+1])
for i in list[s:e+1]:
    sum *= int(i)
print(sum)