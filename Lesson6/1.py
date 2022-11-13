# 1. Сформировать список нечетных целых чисел от 0 до N, квадрат которых меньше 200. Использовать comprehensions

from random import randint

lst=[i for i in range(0,randint(0,20)) if i%2!=0 and i**2<200]
print(lst)