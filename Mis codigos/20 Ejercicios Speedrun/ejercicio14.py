# Ejercicio 14: Lista de Diccionarios
# Tienes una lista llamada alumnos.
# Cada elemento de esa lista es un diccionario con estas claves:
# 'nombre'
# 'nota'
# Debes contar cuántos alumnos tienen una nota mayor o igual a 4.0.
# Guarda el resultado en la variable aprobados.

alumnos = [{"nombre": "Ana", "nota": 1.0}, {"nombre": "Luis", "nota": 3.5}, {"nombre": "Marta", "nota": 7.0}, {"nombre": "Juan", "nota": 4.0}]
aprobados = 0

for alumno in alumnos:
    if alumno["nota"] >= 4.0:
        aprobados += 1

print(aprobados)