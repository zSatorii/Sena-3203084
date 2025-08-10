# Validador de contraseñas

contraseña = "Python2023]!"

# Verificar requisitos
longitud_minima = len(contraseña) >= 8
tiene_mayuscula = any(c.isupper() for c in contraseña)
tiene_minuscula = any(c.islower() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)
tiene_especial = any(not c.isalnum() for c in contraseña)

# Evaluar la fortaleza
if longitud_minima and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
    fortaleza = "Fuerte"
elif longitud_minima and (tiene_mayuscula or tiene_minuscula) and (tiene_numero or tiene_especial):
    fortaleza = "Media"
else:
    fortaleza = "Débil"

print(f"La fortaleza de la contraseña es: {fortaleza}")
