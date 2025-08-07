from sympy import symbols, diff, sin, exp

x = symbols('x')
expr2 = sin(x) * exp(x)
derivada2 = diff(expr2, x)

print(f"Derivada de {expr2} con respecto a x: {derivada2}")
# Salida: Derivada de sin(x)*exp(x) con respecto a x: exp(x)*sin(x) + exp(x)*cos(x)
