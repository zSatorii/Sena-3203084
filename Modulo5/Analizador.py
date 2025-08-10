import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
datos = np.array([15, 23, 45, 37, 18, 29, 33, 42])

# Analizar características
tiene_negativos = np.any(datos < 0)
cantidad_datos = len(datos)
rango = np.max(datos) - np.min(datos)

# Decidir el tipo de gráfico
if tiene_negativos:
    # Si hay negativos, gráfico de barras
    plt.bar(range(cantidad_datos), datos)
    plt.title("Gráfico de barras (contiene valores negativos)")
elif cantidad_datos > 10:
    # Si hay muchos datos, gráfico de líneas
    plt.plot(range(cantidad_datos), datos)
    plt.title("Gráfico de líneas (muchos datos)")
elif rango > 30:
    # Si el rango es amplio, gráfico de dispersión
    plt.scatter(range(cantidad_datos), datos)
    plt.title("Gráfico de dispersión (amplio rango)")
else:
    # Si son pocos datos y rango pequeño, gráfico circular
    plt.pie(datos, labels=[f"Dato {i+1}" for i in range(cantidad_datos)])
    plt.title("Gráfico circular (pocos datos, rango pequeño)")

plt.show()
