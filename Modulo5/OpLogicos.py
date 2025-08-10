edad = 16
tiene_permiso_padres = True
tiene_licencia = False

if edad >= 18:
    print("Puede conducir legalmente.")
elif edad >= 16 and tiene_permiso_padres and not tiene_licencia:
    print("Puede obtener un permiso de conducir provisional con supervisión.")
else:
    print("No puede conducir todavía.")
