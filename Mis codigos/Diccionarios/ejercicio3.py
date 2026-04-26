# Ejercicio 3: Nivel difícil
# Crea un programa que simule un pequeño registro de estudiantes.

# Debes usar:

#     while
#     for
#     if
#     listas
#     diccionarios
#     print()

# El programa debe hacer lo siguiente:

# 1. Tener una lista de estudiantes, donde cada estudiante sea un diccionario con nombre, edad y notas.
# 2. Recorrer la lista y mostrar el nombre de cada estudiante.
# 3. Calcular el promedio de notas de cada estudiante usando un for.
# 4. Si el promedio es mayor o igual a 4.0, mostrar que está aprobado; si no, mostrar que está reprobado.
# 5. Usar un while para repetir una consulta: el usuario escribe el nombre de un estudiante y el programa busca si existe.
# 6. Si lo encuentra, mostrar todos sus datos; si no, indicar que no está registrado.
# 7. El ciclo debe terminar cuando el usuario escriba salir.

numero_estudiante = 1
estudiante_encontrado = False

estudiantes = [
    {"nombre":"juan", "edad": 20, "notas": [5.0, 6.0, 5.5]},
    {"nombre":"ana", "edad": 18, "notas": [6.0, 6.5, 5.5]},
    {"nombre":"pedro", "edad": 25, "notas": [7.0, 6.0, 4.0]}
]

print("Estudiantes:")
for estudiante in estudiantes:
    print(f"{numero_estudiante}. {estudiante["nombre"]}")
    numero_estudiante += 1

for estudiante in estudiantes:
    notas = estudiante["notas"]
    suma = 0
    for nota in notas:
        suma += nota
    estudiante["promedio"] = suma/len(notas)
    if estudiante["promedio"] >= 4.0:
        estudiante["estado_aprobacion"] = "aprobado"
    else:
        estudiante["estado_aprobacion"] = "reprobado"

while True:
    consultar_estudiante = input("Buscar estudiante: ").lower()
    if consultar_estudiante == "salir":
        break
    estudiante_encontrado = False
    for estudiante in estudiantes:
        if consultar_estudiante == estudiante["nombre"]:
            print(estudiante)
            estudiante_encontrado = True
            break
    if not estudiante_encontrado:
        print("Estudiante no encontrado en los registros")








