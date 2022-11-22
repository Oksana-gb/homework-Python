# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x=1
y=2
z=3
if not(x or y or z)==-x and -y and -z: print(True)
else: print(False) 