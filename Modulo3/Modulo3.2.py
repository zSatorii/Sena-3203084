# Elimina un elemento por su índice y lo devuelve
tareas = ["Estudiar", "Comprar", "Cocinar", "Limpiar"]
tarea_urgente = tareas.pop(1)  # Elimina "Comprar"
print(f"Tarea eliminada: {tarea_urgente}")
print(f"Lista después: {tareas}")
# Resultado:
# Tarea eliminada: Comprar
# Lista después: ['Estudiar', 'Cocinar', 'Limpiar']

# Sin argumentos, elimina el último elemento
ultima_tarea = tareas.pop()  # Elimina "Limpiar"
print(f"Última tarea: {ultima_tarea}")
print(f"Lista final: {tareas}")
# Resultado:
# Última tarea: Limpiar
# Lista final: ['Estudiar', 'Cocinar']
