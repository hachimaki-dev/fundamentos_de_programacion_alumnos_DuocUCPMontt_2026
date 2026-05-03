# Tienes una lista llamada alumnos.

# Cada elemento de esa lista es un diccionario con estas claves:

#    'nombre'
#    'nota'

# Debes contar cuántos alumnos tienen una nota mayor o igual a 4.0.

# Guarda el resultado en la variable aprobados.

alumnos = [
    {
        "nombre": "Pablo",
        "nota": 5.1
    },
    {
        "nombre": "Maria",
        "nota": 3.2
    },
    {
        "nombre": "Sebastian",
        "nota": 4.1
    },
    {
        "nombre": "Sofia",
        "nota": 4.4
    },
    {
        "nombre": "Rodrigo",
        "nota": 2.5
    }
    ]

aprobados = 0

for alumno in alumnos:
    if alumno.get("nota") >= 4.0:
        aprobados += 1

print(aprobados)