# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# Если вы не знаете как вычислить квадратный корень, оставьте квадрат расстояния

x1=int(input('Введите x: '))
y1=int(input('Введите y: '))
x2=int(input('Введите x: '))
y2=int(input('Введите y: '))
print(round(pow((pow((x2-x1),2) + pow((y2-y1),2)), 0.5),2))