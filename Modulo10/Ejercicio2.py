class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def incrementar_salida(self, porcentaje):
        """Incrementa el salario del empleado según un porcentaje."""
        incremento = self.salario * (porcentaje / 100)
        self.salario += incremento
        return self.salario

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario: ${self.salario:.2f}"

# Prueba
e1 = Empleado("Ana García", 30000)
print(e1)                # Empleado: Ana García, Salario: $30000.00
e1.incrementar_salida(10)
print(e1)                # Empleado: Ana García, Salario: $33000.00
