import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, exp, diff

# Modelo de crecimiento exponencial:
# N(t) = N0 * e^(k*t)
# N0: población inicial
# k: tasa de crecimiento

# Parámetros
N0 = 1000           # población inicial
k = 0.5             # tasa de crecimiento

# Tiempo (horas)
t_valores = np.linspace(0, 10, 100)

# Población en cada tiempo
N_valores = N0 * np.exp(k * t_valores)

# Cálculo simbólico de la tasa de crecimiento
t = symbols('t')
N = N0 * exp(k * t)
dN_dt = diff(N, t)

print(f"Tasa de crecimiento simbólica: dN/dt = {dN_dt}")

# Graficar
plt.plot(t_valores, N_valores)
plt.xlabel("Tiempo (horas)")
plt.ylabel("Población")
plt.title("Crecimiento exponencial de la población")
plt.show()
