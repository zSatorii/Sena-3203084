def calcular_precio(producto, cantidad=1, descuento=0, impuesto=0.21):
    precio_base = producto * cantidad
    precio_con_descuento = precio_base * (1 - descuento)
    precio_final = precio_con_descuento * (1 + impuesto)
    return precio_final

# Diferentes formas de llamar a la función
precio1 = calcular_precio(100)                     # Solo producto, resto valores predeterminados
precio2 = calcular_precio(100, 2)                  # Producto y cantidad
precio3 = calcular_precio(100, descuento=0.1)      # Producto y descuento por palabra clave
precio4 = calcular_precio(producto=100, impuesto=0.10) # Por palabra clave Producto e impuesto

print(precio1)
print(precio2)
print(precio3)
print(precio4)
