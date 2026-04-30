aprobados = 0
alumnos = [
        { "Nombre": "Pepito",   "Nota": 6.2 },
        { "Nombre": "María",    "Nota": 6.6 },
        { "Nombre": "Juanito",  "Nota": 3.0 },
        { "Nombre": "Carlitos", "Nota": 3.8 },
        { "Nombre": "José",     "Nota": 4.0 }
]

for i in alumnos:
    if i["Nota"] >= 4.0:
        aprobados = aprobados + 1
    else:
        continue

print(aprobados)
