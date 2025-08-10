# Calculadora de IMC
peso = 70       # en kg
altura = 1.75   # en metros

# Cálculo del IMC
imc = peso / (altura ** 2)

# Clasificación según el IMC
if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Tu IMC es {imc:.2f}, categoría: {categoria}")
