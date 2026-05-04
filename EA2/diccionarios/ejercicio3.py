'''Crea un programa que simule un pequeño registro de estudiantes.

Debes usar:

    while
    for
    if
    listas
    diccionarios
    print()

El programa debe hacer lo siguiente:

    Tener una lista de estudiantes, donde cada estudiante sea un diccionario con nombre, edad y notas.
    Recorrer la lista y mostrar el nombre de cada estudiante.
    Calcular el promedio de notas de cada estudiante usando un for.
    Si el promedio es mayor o igual a 4.0, mostrar que está aprobado; si no, mostrar que está reprobado.
    Usar un while para repetir una consulta: el usuario escribe el nombre de un estudiante y el programa busca si existe.
    Si lo encuentra, mostrar todos sus datos; si no, indicar que no está registrado.
    El ciclo debe terminar cuando el usuario escriba salir.
'''

estudiantes = [
    {"nombre": "Juan", "edad": 20, "notas": [3.5, 2.8, 4.0]},
    {"nombre": "Sofía", "edad": 22, "notas": [6.2, 5.8, 7.0]},
    {"nombre": "Rodrigo", "edad": 19, "notas": [5.0, 4.2, 6.1]},
    {"nombre": "Ana", "edad": 21, "notas": [4.8, 3.0, 3.9]},
    {"nombre": "Martín", "edad": 23, "notas": [3.5, 4.0, 6.8]}
]

for estudiante in estudiantes:
    promedios = sum(estudiante["notas"]) / len(estudiante["notas"])
    print(f"Nombre del alumno: {estudiante['nombre']}")
    if promedios >= 4.0:
        print(f" -aprobado con un promedio de {promedios:.1f}\n")
    else:
        print(f" -reprobado con un promedio de {promedios:.1f}\n")

while True:
    consulta = input("Ingrese el nombre del estudiante para consultar (o 'salir' para terminar): ")
    if consulta.lower() == "salir":
        print("Programa terminado.")
        break
    
    encontrado = False
    for estudiante in estudiantes:
        promedios = sum(estudiante["notas"]) / len(estudiante["notas"])
        if estudiante["nombre"].lower() == consulta.lower():
            print(f"Datos de {estudiante['nombre']}:\n   -Edad: {estudiante['edad']}\n   -Notas: {estudiante['notas']}\n   -Promedio: {promedios:.1f}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"El estudiante '{consulta}' no está registrado.")