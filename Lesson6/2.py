# 2. Есть два списка: tutors - имена учеников, groups - названия их классов. Необходимо сформировать список кортежей вида (tutor, group).
# Техническое задание

# Программа должна работать со списками tutors, groups любой длины.
# Длина результирующего списка не должна быть больше длины списка tutors.
# Если в списке groups меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например: ('Станислав', None)
# Если в списке tutors меньше элементов, чем в списке groups, то смотри пункт 2.
# Вы можете использовать в этом задании функции zip и zip_longest, но лучше обойтись без них
# Не меняйте исходные списки tutors и groups и не создавайте промежуточных списков. Только список результат.
# Подтвердите работоспособность(выведите в консоль результаты) для обоих вариантов: groups меньше tutors и tutors меньше groups.
# Сделайте сначала задание через циклы обычным образом, затем оформите решение в "одну строку" в виде comprehensions

tutors = ['Иван', 'Анастасия', 'Петр']
groups = ['9А', '7В', '9Б']
new_lst=[]
if len(tutors)>len(groups):
    # for i in range(len(tutors)-len(groups)):   это вроде лучше потому что лишнего не добавляет?
    #      groups.append(None)
    for i,el in enumerate(tutors):
        groups.append(None)
        new_lst.append((el, groups[i]))
else:
    for i,el in enumerate(tutors):
        new_lst.append((el, groups[i]))


# new_lst=[(el, groups[i]) for i,el in enumerate(tutors) if len(tutors)<len(groups) else (i, None) for i in tutors] 
print(new_lst)