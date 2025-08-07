# Lista de productos disponibles
productos_disponibles = ["manzana", "naranja", "plátano", "uva", "pera"]

# Productos que el cliente desea comprar
productos_deseados = ["manzana", "kiwi", "pera"]

# Verificar disponibilidad de cada producto
for producto in productos_deseados:
    disponible = producto in productos_disponibles
    if disponible:
        estado = "disponible"
    else:
        estado = "no disponible"
    print(f"El producto '{producto}' está {estado}")
