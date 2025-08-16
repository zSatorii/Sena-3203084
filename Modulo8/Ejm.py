try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Error: Debes introducir un número válido")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
except:
    print("Ha ocurrido un error inesperado")
