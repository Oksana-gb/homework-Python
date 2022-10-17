# Реализуйте алгоритм перемешивания элементов списка. Без функции shuffle из модуля random, другие методы использовать можно.

import random

list=[i for i in range(1,11)]
print(list)
print(random.sample(list,list[-1]))