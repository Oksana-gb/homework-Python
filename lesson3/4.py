# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> '101101'
# 3 -> '11'
# 2 -> '10'
# Примечание: Результат вернуть в виде строки. Не использовать функции преобразования типов: bin

num = int(input('введите число '))
result = []
while num > 0:
    result.append(str(num % 2))
    num = int(num/2)
result.reverse()
print(''.join(result))
