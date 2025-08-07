# Inicializar puntuación
puntos = 0
print(f"Puntuación inicial: {puntos}")

# Ganar 100 puntos
puntos += 100
print(f"Después de ganar nivel 1: {puntos}")

# Ganar bonus (multiplicar por 2)
puntos *= 2
print(f"Después de conseguir bonus: {puntos}")

# Perder 50 puntos
puntos -= 50
print(f"Después de perder una vida: {puntos}")

# Dividir puntos entre jugadores (2 jugadores)
puntos //= 2  # División entera
print(f"Puntos por jugador (2 jugadores): {puntos}")
