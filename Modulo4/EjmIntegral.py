from sympy import symbols, integrate

x = symbols('x')
expresion_integral = x**2  # Integral indefinida

integral_indefinida = integrate(expresion_integral, x)
print(f"Integral indefinida de {expresion_integral} con respecto a x: {integral_indefinida}")
# Salida: Integral indefinida de x**2 con respecto a x: x**3/3
