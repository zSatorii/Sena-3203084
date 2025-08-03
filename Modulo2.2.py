def convertir_temperatura():
    print("CONVERSOR DE TEMPERATURA")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Fahrenheit a Celsius")
    print("4. Fahrenheit a Kelvin")
    print("5. Kelvin a Celsius")
    print("6. Kelvin a Fahrenheit")
    try:
        opcion = int(input("Seleccione una opción (1-6): "))
        if opcion < 1 or opcion > 6:
            print("Opción inválida")
            return
        temp = float(input("Ingrese la temperatura: "))
        if opcion == 1:
            resultado = temp * 9/5 + 32
            print(f"{temp}°C = {resultado:.2f}°F")
        elif opcion == 2:
            resultado = temp + 273.15
            print(f"{temp}°C = {resultado:.2f}K")
        elif opcion == 3:
            resultado = (temp - 32) * 5/9
            print(f"{temp}°F = {resultado:.2f}°C")
        # ... (otras conversiones)
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

convertir_temperatura()
