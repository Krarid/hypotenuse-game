import random

hipotenusa = random.randint(5,15)

print("Hipotenusa: ", hipotenusa)

catetoA = 0

while catetoA <= 0 or catetoA >= hipotenusa:
    catetoA = int(input(f"Ingresa un numero mayor que 0 menor que la hipotenusa [0 < X < {hipotenusa}]: "))

catetoB = pow((hipotenusa ** 2) - (catetoA ** 2), 1/2)

print("Cateto B: ", catetoB)