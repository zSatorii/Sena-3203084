r = (input("Seleccione el tipo de operación (+, -, *, /) "))
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

dic={"r":r, "n1":n1, "n2":n2}

if dic["r"] == "+":
    print(dic["n1"]+dic["n2"])
else:
    if dic["r"] == "-":
        print(dic["n1"]-dic["n2"])
    else:
        if dic["r"] == "*":
            print(dic["n1"]*dic["n2"])
        else:
            if dic["r"] == "/":
                print(dic["n1"]/dic["n2"])
