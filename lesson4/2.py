# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Написать функцию, которая принимает аргумент - целое число и возвращает список его простых множителей.
# Пример:
# simple_number(147420) => [2, 3, 5, 7, 13];
# simple_number(374220) => [2, 3, 5, 7, 11];

def simple_number(num):
    result=[]
    while num>1:
        for i in range(2,50):
            if num%i==0:
                result.append(i)
                num/=i

    for i in result:
        if i!=2 and i!=3 and (i%2==0 or i%3==0):
            result.remove(i)
        
    return result


num=147420
print(simple_number(num))