import numpy as np

matriz_a = np.array([[1, 2], 
                     [3, 4]])

matriz_b = np.array([[5, 6], 
                     [7, 8]])

# Multiplicación matricial usando np.dot()
resultado_dot = np.dot(matriz_a, matriz_b)
print("Multiplicación (np.dot):\n", resultado_dot)
# Salida:
# Multiplicación (np.dot):
# [[19 22]
#  [43 50]]

# Multiplicación matricial usando el operador @ (Python 3.5+)
resultado_at = matriz_a @ matriz_b
print("Multiplicación (operador @):\n", resultado_at)
# Salida:
# Multiplicación (operador @):
# [[19 22]
#  [43 50]]
