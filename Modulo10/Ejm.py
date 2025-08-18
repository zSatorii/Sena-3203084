small = 2
regular = 5
big = 6
user_budget = int(input('¿Presupuesto? '))

if user_budget >= big:
    print('Puede comprar café grande')
    print('Su cambio: ', user_budget - big)
elif user_budget >= regular:
    print('Puede comprar café mediano')
    print('Su cambio: ', user_budget - regular)
elif user_budget >= small:
    print('Puede comprar café pequeño')
    print('Su cambio: ', user_budget - small)
else:
    print('Presupuesto insuficiente')
