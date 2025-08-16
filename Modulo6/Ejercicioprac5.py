print("Tabla de multiplicar del 1 al 10:")
print("-" * 40)

for i in range(1, 11):
    for j in range(1, 11):
        # Formateamos para alinear correctamente
        print(f"{i * j:4}", end="")
    # Salto de línea al terminar cada fila
    print()
