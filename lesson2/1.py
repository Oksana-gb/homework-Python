# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44

# num=str(input('введите число ')).replace('.', '')
# sum=0
# for i in num:
#     sum+=int(i)
# print(sum)

# или

users_num = input('Укажите вещественное число: ')

nums_sum = 0

for num in users_num:
    if num.isdigit(): nums_sum += int(num)

print(nums_sum)