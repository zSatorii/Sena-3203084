import time

def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"La función {funcion.__name__} tardó {fin - inicio:.5f} segundos en ejecutarse")
        return resultado
    return wrapper

@medir_tiempo
def calcular_suma_grande():
    return sum(range(1000000))

# Llamada a la función decorada
resultado = calcular_suma_grande()
