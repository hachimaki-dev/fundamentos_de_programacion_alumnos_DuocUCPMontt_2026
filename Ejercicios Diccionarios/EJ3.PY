estudiantes = [
    {"nombre": "Bastian Mansilla", "edad": 15, "notas": [6.0, 5.5, 5.0]},
    {"nombre": "Carlos Almonacid", "edad": 13, "notas": [5.3, 5.1, 4.2]},
    {"nombre": "Mauricio Arellano", "edad": 14, "notas": [4.1, 4.3, 3.3]}
]

for estudiante in estudiantes:
    print(estudiante["nombre"])

    suma = 0

    for nota in estudiante["notas"]:
        suma += nota

    promedio = suma / len(estudiante["notas"])
    print("Promedio:", promedio)

    if promedio >= 4.0:
        print("Aprobado")
    else:
        print("Reprobado")

    print("--------------------")


while True:
    alumno_existente = input("Escriba el nombre del alumno o 'salir': ")

    if alumno_existente == "salir":
        break

    encontrado = False

    for estudiante in estudiantes:
        if alumno_existente.lower() == estudiante["nombre"].lower():
            print("Estudiante encontrado:")
            print("Nombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])
            print("Notas:", estudiante["notas"])

            suma = 0
            for nota in estudiante["notas"]:
                suma += nota

            promedio = suma / len(estudiante["notas"])
            print("Promedio:", promedio)

            encontrado = True

    if encontrado == False:
        print("Estudiante no registrado")