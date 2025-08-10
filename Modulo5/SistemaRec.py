# Sistema de recomendación simple

historial_compras = ["laptop", "smartphone", "auriculares"]
categoria_actual = "electrónica"
hora_del_dia = 20  # 8 PM

# Determinar recomendaciones basadas en múltiples factores
if "laptop" in historial_compras and categoria_actual == "electrónica":
    if hora_del_dia >= 18:  # Noche
        recomendacion = "Ofertas nocturnas: Accesorios para laptop"
    else:  # Día
        recomendacion = "Ratones y teclados inalámbricos"
elif "smartphone" in historial_compras:
    recomendacion = "Fundas y protectores de pantalla"
else:
    recomendacion = "Productos destacados en electrónica"

print(f"Recomendación personalizada: {recomendacion}")
