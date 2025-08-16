def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("¡División por cero!")
    else:
        print("El resultado es", result)
    finally:
        print("Ejecutando la cláusula finally")

# Caso 1: División normal
divide(2, 1)
# Imprime:
# El resultado es 2.0
# Ejecutando la cláusula finally

# Caso 2: División por cero
divide(2, 0)
# Imprime:
# ¡División por cero!
# Ejecutando la cláusula finally

# Caso 3: Error de tipo
divide("2", "1")
# Imprime:
# Ejecutando la cláusula finally
# Luego lanza TypeError
