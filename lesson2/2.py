# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)




# n=int(input('введите число '))
# r=1
# i=1
# while i<n+1:
#     r*=i
#     print (r, end = " ")
#     i+=1


# или


import math

n=int(input('введите число '))
i=1
while i<n+1:
   print(math.factorial(i), end = " ")
   i+=1