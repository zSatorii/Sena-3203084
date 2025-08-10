import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Producto': ['A', 'B', 'C', 'D'],
    'Ventas': [1200, 850, 1500, 450]
}

df = pd.DataFrame(data)

# Filtrar productos que tienen más de 1000 ventas
for index, row in df.iterrows():
    if row['Ventas'] > 1000:
        print(f"El producto {row['Producto']} ha superado las 1000 ventas.")
