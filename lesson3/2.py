# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

num_list = [2, 3, 4, 5, 6]
result = []

for i in range(len(num_list)):
    if i < len(num_list)/2:
        result.append(num_list[i]*num_list[-i-1])
print(result)
