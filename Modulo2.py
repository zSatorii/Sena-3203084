numero1 = 5 #Las variables son int
numero2 = 3
suma = numero1 + numero2
print("La suma es:", suma)

nota1 = 3.7 #Las variables son Float
nota2 = 4.2
nota3 = 3.9
promedio = (nota1 + nota2 + nota3) / 3
print("El promedio es:", promedio)


edad = 0  # Se declara edad inicialmente como cero
edad = int(input("Ingresa tu edad: "))  # Aca se convierte en lo que ingresa el usuario
print("Tu edad es", edad)


es_mayor = True
tiene_licencia = False
puede_conducir = es_mayor and tiene_licencia
print(puede_conducir)  # False, porque no tiene licencia
