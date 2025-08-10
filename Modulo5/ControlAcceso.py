usuario_logueado = True
rol_usuario = "admin"

if usuario_logueado:
    print("Usuario autenticado.")
    if rol_usuario == "admin":
        print("Acceso total al panel de administración.")
    elif rol_usuario == "editor":
        print("Acceso a edición de contenido.")
    else:
        print("Acceso limitado a funcionalidades básicas.")
else:
    print("Por favor, inicia sesión para acceder.")
