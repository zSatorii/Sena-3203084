from math import pi, sqrt

class Forma:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass

    def __str__(self):
        return f"{self.nombre} con área: {self.area()}"

class Cuadrado(Forma):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2
