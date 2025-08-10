edad = 65
es_estudiante = False
es_jubilado = True

if es_estudiante:
    print("Descuento del 20% para estudiantes")
elif es_jubilado or edad >= 65:
    print("Descuento del 15% para jubilados")
elif edad <= 12:
    print("Descuento del 10% para niños")
else:
    print("Sin descuento aplicable")
