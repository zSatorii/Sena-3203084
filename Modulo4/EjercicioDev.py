from sympy import symbols, diff

# Definir variable simbólica
x = symbols('x')

# Función de costo: C(x) = 2x² - 8x + 10
costo = 2*x**2 - 8*x + 10

# Calcular la derivada (función de costo marginal)
costo_marginal = diff(costo, x)

print(f"Función de costo: C(x) = {costo}")
print(f"Función de costo marginal: C'(x) = {costo_marginal}")

# Evaluar el costo marginal en x = 3
x_valor = 3
costo_marginal_en_3 = costo_marginal.subs(x, x_valor)
print(f"Costo marginal en x = {x_valor}: {costo_marginal_en_3}")
