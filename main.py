from Triangulo import Triangulo

triangulo = Triangulo()

triangulo.hipotenusaAleatoria()
print("Hipotenusa: ", triangulo.obtenerHipotenusa())

triangulo.solicitarLadoA()
triangulo.calcularCateto()
print("Lado B: ", triangulo.obtenerLadoB())