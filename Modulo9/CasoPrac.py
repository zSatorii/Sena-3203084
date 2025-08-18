import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Cargar datos
datos = pd.read_csv('datos_ventas.csv')
print(datos.head())

# Análisis exploratorio
print(f"Estadísticas descriptivas:\n{datos.describe()}")
print(f"Ventas por región:\n{datos.groupby('region')['ventas'].sum()}")

# Visualización
plt.figure(figsize=(10, 6))
datos.groupby('mes')['ventas'].sum().plot(kind='bar')
plt.title('Ventas Totales por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.savefig('ventas_por_mes.png')

# Modelo simple
X = datos[['publicidad']].values
y = datos['ventas'].values
modelo = LinearRegression()
modelo.fit(X, y)

# Predicciones
nuevos_valores = np.array([[2000], , ])
predicciones = modelo.predict(nuevos_valores)
print(f"Predicciones de ventas: {predicciones}")
