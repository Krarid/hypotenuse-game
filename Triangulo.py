import random

class Triangulo:

    def __init__(self):
        self.hipotenusa = 0
        self.ladoA = 0
        self.ladoB = 0

    def calcularCateto(self):
        self.ladoB = pow((self.hipotenusa ** 2) - (self.ladoA ** 2), 1/2)

    def hipotenusaAleatoria(self):
        self.hipotenusa = random.randint(5,15)

    def solicitarLadoA(self):
        while self.ladoA <= 0 or self.ladoA >= self.hipotenusa:
            self.ladoA = int(input(f"Ingresa un numero mayor que 0 menor que la hipotenusa [0 < X < {self.hipotenusa}]: "))

    def obtenerHipotenusa(self):
        return self.hipotenusa
    
    def obtenerLadoA(self):
        return self.ladoA
    
    def obtenerLadoB(self):
        return self.ladoB
    
#triangulo = Triangulo()

#triangulo.hipotenusaAleatoria()
#print("Hipotenusa: ", triangulo.obtenerHipotenusa())

#triangulo.solicitarLadoA()
#triangulo.calcularCateto()
#print("Lado B: ", triangulo.obtenerLadoB())