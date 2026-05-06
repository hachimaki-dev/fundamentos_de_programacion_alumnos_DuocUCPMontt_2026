"""
### Ejercicio 3: Nivel difícil

Crea un programa que simule un pequeño registro de estudiantes.

Debes usar:

* `while`
* `for`
* `if`
* listas
* diccionarios
* `print()`

El programa debe hacer lo siguiente:

1. Tener una lista de estudiantes, donde cada estudiante sea un diccionario con `nombre`, `edad` y `notas`.
2. Recorrer la lista y mostrar el nombre de cada estudiante.
3. Calcular el promedio de notas de cada estudiante usando un `for`.
4. Si el promedio es mayor o igual a 4.0, mostrar que está aprobado; si no, 
mostrar que está reprobado.
5. Usar un `while` para repetir una consulta: el usuario escribe el nombre de un 
estudiante y el programa busca si existe.
6. Si lo encuentra, mostrar todos sus datos; si no, indicar que no está registrado.
7. El ciclo debe terminar cuando el usuario escriba `salir`.
"""

# --- DATOS ---
Estudiantes = [
    {
        "Nombre": "Koda", "Edad": 15, "Notas": [5.5, 6.9, 6.3]
    },
    {
        "Nombre": "Shira", "Edad": 16, "Notas": [5.2, 6.1, 6.8]
    },
    {
        "Nombre": "Leonardo", "Edad": 17, "Notas": [5.8, 6.2, 5.0]
    },
    {
        "Nombre": "Yuliana", "Edad": 16, "Notas": [5.6, 6.6, 5.2]
    }
]

# --- FUNCIONES ---

def mostrar_nombres():
    print("Los nombres de los estudiantes son:")
    for estudiante in Estudiantes:
        print(estudiante["Nombre"])

def calcular_promedios():
    print("\n-----------Promedios y Estados-----------")
    for estudiante in Estudiantes:
        nombre = estudiante["Nombre"]
        notas = estudiante["Notas"]
        
        suma = 0
        for nota in notas:
            suma = suma + nota
        
        cantidad = len(notas)
        promedio = suma / cantidad
        
        if promedio >= 4.0:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        
        print(f"\nEstudiante: {nombre} | Promedio: {promedio:.2f} | Estado: {estado}")

def buscar_estudiante(nombre_a_buscar):
    encontrado = False
    for estudiante in Estudiantes:
        # Comparamos usando .lower() para ignorar mayúsculas
        if estudiante['Nombre'].lower() == nombre_a_buscar.lower():
            print("\n--------------Datos encontrados---------------")
            print("\nNombre:", estudiante['Nombre'])
            print("Edad:", estudiante['Edad'])
            print("Notas:", estudiante['Notas'])
            encontrado = True
            break # Salimos del bucle porque ya lo encontramos
    
    if not encontrado:
        print("El estudiante no esta registrado en el sistema")

# --- PROGRAMA PRINCIPAL ---

# 1. Mostramos nombres y promedios una sola vez al inicio
mostrar_nombres()
calcular_promedios()

# 2. Bucle principal de búsqueda
print("\n-----------Sistema de busqueda (Escribe SALIR para terminar)-----------")

while True:
    busqueda = input("Ingresa el nombre del estudiante: ")
    
    # Verificamos si quiere salir
    if busqueda.lower() == "salir":
        print("Cargando...")
        print("Saliendo del programa")
        break
    
    # Llamamos a la función de búsqueda con el nombre que escribió el usuario
    buscar_estudiante(busqueda)


"""
### Preguntas de validación

Responde por escrito:

1. ¿Cuál es la diferencia entre una lista y un diccionario?
2. ¿Qué es una clave?
3. ¿Qué ocurre si intentas acceder a una clave que no existe?
4. ¿Cuándo conviene usar un diccionario en vez de una lista?
5. ¿Por qué `items()` es útil cuando recorres diccionarios?
"""