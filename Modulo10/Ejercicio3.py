class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.curso}."

    def mostrar_detalles(self):
        return f"{self.presentarse()} Estoy en el curso de {self.curso}."

# Prueba
e = Estudiante("Carlos Martínez", 20, "Programación Python")
print(e.presentarse())
print(e.estudiar())
print(e.mostrar_detalles())
