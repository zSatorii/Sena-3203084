def proceso_con_multiples_errores():
    excs = []
    for i in range(3):
        try:
            if i == 0:
                raise ValueError("Valor incorrecto")
            elif i == 1:
                raise TypeError("Tipo incorrecto")
            else:
                raise OSError("Error del sistema")
        except Exception as e:
            excs.append(e)
    if excs:
        raise ExceptionGroup("Errores en el proceso", excs)

try:
    proceso_con_multiples_errores()
except* ValueError as e:
    print(f"Manejo de errores de valor: {e}")
except* TypeError as e:
    print(f"Manejo de errores de tipo: {e}")
except* OSError as e:
    print(f"Manejo de errores del sistema: {e}")
