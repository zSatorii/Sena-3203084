import numpy as np

# Matriz de notas [estudiantes x asignaturas]
# Filas: estudiantes, Columnas: asignaturas
notas = np.array([
    [85, 90, 78, 92],  # Estudiante 1
    [76, 88, 95, 87],  # Estudiante 2
    [91, 82, 89, 90]   # Estudiante 3
])

# Calcular promedio por estudiante (promedio de filas)
promedio_estudiantes = np.mean(notas, axis=1)

# Calcular promedio por asignatura (promedio de columnas)
promedio_asignaturas = np.mean(notas, axis=0)

print("Matriz de notas:\n", notas)
print("\nPromedio por estudiante:", promedio_estudiantes)
print("Promedio por asignatura:", promedio_asignaturas)
