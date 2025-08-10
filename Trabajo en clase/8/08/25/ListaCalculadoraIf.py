
lista=["suma", "resta", "multiplicar", "dividir"]
ingresar = (int(input("ingrese el numero (1=suma 2=resta 3=multiplicar 4=dividir ")))
n1 =(int(input("ingrese el primer numero ")))
n2 =(int(input("ingrese el segundo numero ")))

if ingresar == 1:
    print(lista[0])
    print(n1+n2)
else:
    if ingresar == 2:
        print(lista[1])
        print(n1-n2)
    else:
        if ingresar == 3:
            print(lista[2])
            print(n1*n2)
        else:
            if ingresar == 4:
                print(lista[3])
                print(n1/n2)