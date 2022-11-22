# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# https://ru.wikipedia.org/wiki/Кодированиедлинсерий
# Создать функцию сжатия строки и функцию восстановления строки.
# Пример:
# ABCABCABCDDDFFFFFF ->1A1B1C1A1B1C1A1B1C3D6F -> ABCABCABCDDDFFFFFF
# WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR

a='ABCABCABCDDDFFFFFF'
lst=[el for el in a]
print(lst)
# res=''
# k=0
# for i in range(len(lst)):
#     if i!=f:
#         res+=f'1{a[i]}'
#         # k-=1
#     elif a[i]==f:
#         k+=1
#         if a[i+1]!=a[i+2]:
#             res+=f'{k}{a[i]}'
#             k=1

for i in range(len(lst)):
    print(len(lst[i]), lst[i])