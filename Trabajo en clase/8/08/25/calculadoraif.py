r = (input("Seleccione el tipo de operación (+, -, *, /) "))

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

if r == "+":
    print(n1+n2)
else:
    if r == "-":
        print(n1-n2)
    else:
        if r == "*":
            print(n1*n2)
        else:
            if r == "/":
                print(n1/n2)
