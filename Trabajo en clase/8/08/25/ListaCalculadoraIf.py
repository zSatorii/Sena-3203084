r = (input("Seleccione el tipo de operación (+, -, *, /) "))
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

lista=[r,n1,n2]

if lista[r] == "+":
    print(lista[1]+lista[2])
else:
    if lista[r] == "-":
        print(lista[1]-lista[2])
    else:
        if lista[r] == "*":
            print(lista[1]*lista[2])
        else:
            if lista[r] == "/":
                print(lista[1]/lista[2])
