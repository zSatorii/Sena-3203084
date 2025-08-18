import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Añadir directorio padre al path para importar nuestro paquete
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from matematicas.geometria import area_circulo, area_rectangulo

class AplicacionGeometria:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Geométrica")
        self.root.geometry("400x300")

        # Crear pestañas
        self.notebook = ttk.Notebook(root)
        self.tab_circulo = ttk.Frame(self.notebook)
        self.tab_rectangulo = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_circulo, text="Círculo")
        self.notebook.add(self.tab_rectangulo, text="Rectángulo")
        self.notebook.pack(expand=1, fill="both")

        # Configurar pestaña de círculo
        self.configurar_tab_circulo()
        # Configurar pestaña de rectángulo
        self.configurar_tab_rectangulo()
# En la clase AplicacionGeometria

def configurar_tab_circulo(self):
    # Etiqueta y entrada para radio
    ttk.Label(self.tab_circulo, text="Radio:").grid(column=0, row=0, padx=10, pady=10)
    self.radio_var = tk.DoubleVar()
    ttk.Entry(self.tab_circulo, textvariable=self.radio_var).grid(column=1, row=0, padx=10, pady=10)
    # Botón para calcular
    ttk.Button(self.tab_circulo, text="Calcular área", command=self.calcular_area_circulo).grid(column=0, row=1, padx=10, pady=10, columnspan=2)
    # Etiqueta para mostrar resultado
    self.resultado_circulo = ttk.Label(self.tab_circulo, text="")
    self.resultado_circulo.grid(column=0, row=2, columnspan=2, pady=10)

def configurar_tab_rectangulo(self):
    # Etiquetas y entradas para ancho y alto
    ttk.Label(self.tab_rectangulo, text="Ancho:").grid(column=0, row=0, padx=10, pady=10)
    self.ancho_var = tk.DoubleVar()
    ttk.Entry(self.tab_rectangulo, textvariable=self.ancho_var).grid(column=1, row=0, padx=10, pady=10)
    ttk.Label(self.tab_rectangulo, text="Alto:").grid(column=0, row=1, padx=10, pady=10)
    self.alto_var = tk.DoubleVar()
    ttk.Entry(self.tab_rectangulo, textvariable=self.alto_var).grid(column=1, row=1, padx=10, pady=10)
    # Botón para calcular
    ttk.Button(self.tab_rectangulo, text="Calcular área", command=self.calcular_area_rectangulo).grid(column=0, row=2, padx=10, pady=10, columnspan=2)
    # Etiqueta para mostrar resultado
    self.resultado_rectangulo = ttk.Label(self.tab_rectangulo, text="")
    self.resultado_rectangulo.grid(column=0, row=3, columnspan=2, pady=10)
def calcular_area_circulo(self):
    try:
        radio = self.radio_var.get()
        if radio <= 0:
            raise ValueError("El radio debe ser positivo")
        area = area_circulo(radio)
        self.resultado_circulo.config(text=f"Área del círculo: {area:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")

def calcular_area_rectangulo(self):
    try:
        ancho = self.ancho_var.get()
        alto = self.alto_var.get()
        if ancho <= 0 or alto <= 0:
            raise ValueError("El ancho y el alto deben ser positivos")
        area = area_rectangulo(ancho, alto)
        self.resultado_rectangulo.config(text=f"Área del rectángulo: {area:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")

# Iniciar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGeometria(root)
    root.mainloop()
