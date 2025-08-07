# Definir información del estudiante
nombre = "Ana García"
curso = "Python Básico"
nivel = "Intermedio"

# Crear encabezado con repetición
linea = "=" * 30
encabezado = linea + "\n" + "REPORTE DE PROGRESO" + "\n" + linea

# Crear cuerpo con concatenación
cuerpo = "Estudiante: " + nombre + "\n"
cuerpo += "Curso: " + curso + "\n"
cuerpo += "Nivel: " + nivel

# Mostrar reporte completo
reporte = encabezado + "\n\n" + cuerpo
print(reporte)
