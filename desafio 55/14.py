nota = 3.6
asistencia = 85

# Aplicar bono de asistencia
if asistencia >= 80:
    nota += 0.5

# Definir estado
if nota >= 4.0:
    estado = 'Aprobado'
elif 3.5 <= nota <= 3.9:
    estado = 'Examen'
else:
    estado = 'Reprobado'

print(estado)
