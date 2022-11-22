# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01, 12.00] => 0.19
# Примечание:
# Обратите внимание на элемент 5 и и 12.0. Они не участвуют в процессе т.к. дробная часть ноль.
# В списке могут быть как числа float, так и числа int.
# Посмотрите на методы числа float, возможно пригодятся.
from random import uniform, randint
import math

num_list = [1.1, 1.2, 3.1, 5, 10.01, 12.00]
result_list = []
for i in num_list:
    if math.fmod(i, int(i)) > 0:
        result_list.append(round(math.fmod(i, int(i)), 2))
result_list.sort()
print(result_list[-1]-result_list[0])

# или

lst = [round(uniform(0, 20), 2) for i in range(randint(5, 10))]
print(lst)
result_lst = [round(i % 1, 2) for i in lst]
print(max(result_list - min(result_list)))
