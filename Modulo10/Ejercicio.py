class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def __str__(self):
        return f"Rectángulo de {self.base}x{self.altura}"

# Prueba
r1 = Rectangulo(5, 10)
print(f"Área: {r1.calcular_area()}")  # Área: 50
print(r1)  # Rectángulo de 5x10
