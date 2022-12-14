# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов многочлена и записать в файл многочлен степени k.
# Коэффициенты должны быть случайными числами в диапазоне от 1 до 100
# Пример:
# - k=2 => 6*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0
# Усложнение: Коэффициенты в полиноме могут быть нулевыми.
# Примечание Создать три функции:
# 1) Функция формирования полинома. аргумент: степень полинома; возвращает полином. Коэффициенты вычисляются случайными.
# Полином удобно представить как словарь или как список коэффициентов. (на ваш выбор)
# В словаре степени будут ключами, в списке - индексами.
# Например k=3 => 6*x^3 + 4*x + 5. Словарь будет такой: {3:6, 2:0, 1:4, 0:5}. А список такой [5,4,0,6]
# 2) Функция формирование строки-полинома. Аргумент: полином (в вид словаря или списка).
# Возвращает строку вида '6*x^3 + 4*x + 5'
# Примечание: Обратите внимание на запись первой и нулевой степени, а также учет нулевого коэффициента.
# Для формирования строки удобно использовать join
# 3) Функция записи строки-полинома в файл. Аргументы: имя файла и строка-полином.

import random


def write_file(st):
    with open('task4.5.txt', 'w') as data:
        data.write(st)


def create_mn(k):
    lst = [random.randint(0, 101) for i in range(k+1)]
    return lst


def polynom(lst):
    result = ''
    if len(lst) < 1:
        result = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                result += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    result += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                result += f'{lst[i]}x'
                if lst[i+1] != 0:
                    result += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                result += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                result += ' = 0'
            elif i != len(lst) - 1 and lst[i] == 0:
                result += ' + '
    return result


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(polynom(koef))
