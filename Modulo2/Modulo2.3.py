from decimal import Decimal, getcontext

def conversor_monedas():
    # Configurar precisión
    getcontext().prec = 10

    # Tasas de cambio (ejemplo)
    tasas = {
        "USD": Decimal('1.0'),
        "EUR": Decimal('0.85'),
        "MXN": Decimal('17.80'),
        "COP": Decimal('3950.25'),
        "ARS": Decimal('880.50')
    }

    print("CONVERSOR DE MONEDAS")
    print("--------------------")
    # Mostrar monedas disponibles
    print("Monedas disponibles:")
    for moneda in tasas:
        print(f"- {moneda}")

    try:
        # Entrada del usuario
        cantidad = Decimal(input("\nIngrese la cantidad: "))
        moneda_origen = input("Moneda de origen: ").upper()
        moneda_destino = input("Moneda de destino: ").upper()

        # Validar monedas
        if moneda_origen not in tasas or moneda_destino not in tasas:
            raise ValueError("Moneda no válida")

        # Realizar conversión
        # Primero a USD, luego a moneda destino
        cantidad_usd = cantidad / tasas[moneda_origen]
        cantidad_convertida = cantidad_usd * tasas[moneda_destino]

        # Formatear resultado con 2 decimales
        resultado = cantidad_convertida.quantize(Decimal('0.01'))
        print(f"\n{cantidad} {moneda_origen} = {resultado} {moneda_destino}")

    except ValueError as e:
        print(f"Error: {e}")
    except KeyError:
        print("Error: Moneda no reconocida")

conversor_monedas()
