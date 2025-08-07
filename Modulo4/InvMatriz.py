import numpy as np

# Definir la matriz cuadrada
matriz_cuadrada = np.array([[1, 2],
                            [3, 4]])

# Calcular la inversa
inversa = np.linalg.inv(matriz_cuadrada)

print("Matriz original:\n", matriz_cuadrada)
# Salida:
# Matriz original:
# [[1 2]
#  [3 4]]

print("Matriz inversa:\n", inversa)
# Salida:
# Matriz inversa:
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# Verificación: Producto A × A⁻¹ ≈ Identidad
producto = matriz_cuadrada @ inversa

print("Producto A × A⁻¹:\n", producto)
# Salida aproximada a la matriz identidad:
# [[1. 0.]
#  [0. 1.]]
