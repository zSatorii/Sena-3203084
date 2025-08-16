def mi_decorador(funcion):
    def wrapper():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

# Llamada a la función decorada
saludar()
