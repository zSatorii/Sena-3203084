# Añade todos los elementos de otro iterable
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(f"Después de extend: {lista1}")
# Resultado: Después de extend: [1, 2, 3, 4, 5, 6]

# También funciona con tuplas y otros iterables
lista3 = ['a', 'b']
tupla_extra = ('c', 'd')
lista3.extend(tupla_extra)
print(lista3)
# Resultado: ['a', 'b', 'c', 'd']
