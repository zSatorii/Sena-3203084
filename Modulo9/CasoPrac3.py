import requests
import pandas as pd
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

# Descargar datos
def descargar_datos(url, archivo_destino):
    """Descarga datos de una URL y los guarda en un archivo."""
    respuesta = requests.get(url)
    with open(archivo_destino, 'wb') as f:
        f.write(respuesta.content)
    print(f"Datos descargados en {archivo_destino}")

# Procesar datos
def procesar_datos(archivo_entrada, archivo_salida):
    """Procesa los datos y genera un informe."""
    df = pd.read_csv(archivo_entrada)
    # Realizar algunas transformaciones
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['mes'] = df['fecha'].dt.month
    resumen = df.groupby('mes')['ventas'].sum().reset_index()
    # Guardar resultados
    resumen.to_csv(archivo_salida, index=False)
    print(f"Datos procesados y guardados en {archivo_salida}")
    return resumen
