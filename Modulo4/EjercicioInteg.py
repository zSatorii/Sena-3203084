from sympy import symbols, integrate

# Definir variable simbólica
p = symbols('p')

# Función de demanda: D(p) = 100 - 2p
demanda = 100 - 2*p

# Calcular el excedente del consumidor
# (área bajo la curva de demanda desde p=30 a p=50)
excedente = integrate(demanda, (p, 30, 50))

print(f"Función de demanda: D(p) = {demanda}")
print(f"Excedente del consumidor entre p=30 y p=50: {excedente}")
