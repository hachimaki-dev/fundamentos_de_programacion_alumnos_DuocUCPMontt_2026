# Ejercicio 14: Sistema de Grados con Bonificación

print("===========================")
print("Sistema de cálculo de notas")
print("===========================")

nota = 3.6
asistencia = 85

if asistencia >= 80:
    nota = nota + 0.5

if nota >= 4.0:
    print("Aprobado")
elif nota >= 3.5:
    print("Examen")
else:
    print("Reprobado")