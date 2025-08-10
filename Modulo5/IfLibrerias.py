import matplotlib.pyplot as plt
import numpy as np

# Datos (con un valor negativo)
datos = np.array([10, 5, 8, -5, 12])

# Verificar si hay valores negativos
if np.any(datos < 0):
    # Si hay negativos, usar gráfico de barras
    plt.bar(range(len(datos)), datos)
    plt.title("Gráfico de barras (contiene valores negativos)")
else:
    # Si todos son positivos, usar gráfico de líneas
    plt.plot(datos)
    plt.title("Gráfico de líneas (solo valores positivos)")

plt.show()
