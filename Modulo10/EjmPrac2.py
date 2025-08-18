class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

class Hexagono(Forma):
    def __init__(self, lado):
        super().__init__("Hexágono")
        self.lado = lado

    def area(self):
        return (3 * sqrt(3) * self.lado ** 2) / 2

# Usar las clases
cuadrado = Cuadrado(5)
circulo = Circulo(3)
triangulo = Triangulo(4, 6)
hexagono = Hexagono(2)

print(cuadrado)   # Cuadrado con área: 25
print(circulo)    # Círculo con área: 28.27...
print(triangulo)  # Triángulo con área: 12
print(hexagono)   # Hexágono con área: 10.39...
