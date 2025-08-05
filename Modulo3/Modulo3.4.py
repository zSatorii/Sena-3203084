#aca hay 3 de sort



# Ordena los elementos de la lista en su lugar de menor a mayor
numeros_desordenados = [5, 2, 8, 1, 9]
numeros_desordenados.sort()
print(f"Después de sort() (ascendente): {numeros_desordenados}")
# Resultado: Después de sort() (ascendente): [1, 2, 5, 8, 9]


# Ordena los elementos en orden inverso (descendente)
nombres = ["Carlos", "Ana", "David", "Beatriz"]
nombres.sort(reverse=True)
print(f"Orden descendente: {nombres}")
# Resultado: Orden descendente: ['David', 'Carlos', 'Beatriz', 'Ana']


# Simplemente invierte el orden actual de la lista (no ordena)
secuencia = [1, 2, 3, 4, 5]
secuencia.reverse()
print(f"Después de reverse(): {secuencia}")
# Resultado: Después de reverse(): [5, 4, 3, 2, 1]
