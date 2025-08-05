# Inserta un elemento en una posición específica
numeros = [1, 2, 4, 5]
numeros.insert(2, 3)  # Inserta 3 en índice 2
print(f"Después de insert(2, 3): {numeros}")
# Resultado:
# Después de insert(2, 3): [1, 2, 3, 4, 5]

# Insertar al principio
numeros.insert(0, 0)  # Inserta 0 al inicio
print(f"Después de insert(0, 0): {numeros}")
# Resultado:
# Después de insert(0, 0): [0, 1, 2, 3, 4, 5]
