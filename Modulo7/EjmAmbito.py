x = 10  # Variable global

def mi_funcion():
    y = 5  # Variable local
    print(f"Variable local y: {y}")
    print(f"Variable global x: {x}")

mi_funcion()

print(f"Variable global x: {x}")
# print(f"Variable local y: {y}")  # Esto generaría un error
