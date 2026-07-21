# Ejercicio 2 (59 puntos)
# Desarrolle un programa en Python que permita gestionar y analizar actividades diarias, calculando el tiempo total dedicado a ellas.

# El programa debe operar mediante un menú de opciones que se repite continuamente hasta que el usuario decida salir.

# Paso 1: Inicio

# Mostrar el siguiente mensaje:
# “Registro de actividades diarias”

# Paso 2: Menú de opciones

# El programa debe presentar el siguiente menú:

# RegiÑstrar actividades
# Mostrar análisis del tiempo
# Salir

# Luego, solicitar al usuario que seleccione una opción.

# Paso 3: Opción 1 – Registrar actividades

# Si el usuario selecciona esta opción, el programa debe:

# Solicitar la cantidad de actividades a registrar:
# Este valor debe ser un número entero mayor o igual a 3.
# Inicializar:
# Un contador para controlar la cantidad de actividades ingresadas.
# Un acumulador para sumar el tiempo total.
# Mientras no se hayan registrado todas las actividades:
# Solicitar el nombre de la actividad.
# Solicitar el tiempo que toma dicha actividad (en minutos).
# Sumar el tiempo ingresado al total acumulado.
# Incrementar el contador.

# Al finalizar el registro, el programa debe volver automáticamente al menú principal.

# Paso 4: Opción 2 – Mostrar análisis del tiempo

# Si el usuario selecciona esta opción, el programa debe:

# Mostrar el tiempo total acumulado de las actividades registradas.
# Evaluar el tiempo total:
# Si el tiempo es mayor a 180 minutos, mostrar:
# “Tiempo diario excesivo”
# En caso contrario, mostrar:
# “Tiempo diario adecuado”

# Al finalizar, el programa debe regresar al menú principal.

# Paso 5: Opción 3 – Salir

# Si el usuario selecciona esta opción, el programa debe:

# Mostrar el mensaje: “Fin del registro”
# Finalizar la ejecución.
# Requisitos obligatorios

# El programa en Python debe incluir:

# Uso de variables.
# Uso de un contador.
# Uso de un acumulador.
# Uso de estructuras de repetición (por ejemplo, while o for)
# Uso de estructuras de decisión (if, elif, else).
# Mensajes claros, ordenados y comprensibles para el usuario.

opcion_usuario = 0
controlador_cantidad_ingresada = 0
acumulador_suma = 0

while True:
    print("Registro de actividades diarias")
    print("1. Registrar actividades")
    print("2. Mostrar análisis del tiempo")
    print("3. Salir")
    opcion_usuario = int(input("Selecione una opción del 1 al 3: "))
    print()
    if opcion_usuario == 1:
        controlador_cantidad_ingresada = 0
        cantidad_ingresada = int(input("¿Cuantas actividades quieres registar?: "))
        if cantidad_ingresada >= 3 :
            while controlador_cantidad_ingresada < cantidad_ingresada:
                nombre_de_la_actividad = input("Cuál nombre de la actividad?: ")
                tiempo_de_la_actividad= int(input("¿Cúanto tiempo demoras en la actividad?: "))
                print()
                acumulador_suma = acumulador_suma + tiempo_de_la_actividad
                controlador_cantidad_ingresada +=1
        else:
            print("Minimo a registrar actividades es 3")
            print()
    elif opcion_usuario ==2:
        print(f"Tiempo total acumulado es {acumulador_suma}")
        if acumulador_suma > 180:
            print("Tiempo diario excesivo")
            print()
        else:
            print("Tiempo diario adecuado")
            print()
    elif opcion_usuario == 3:
        print("Fin del registro")
        break
    else:
        print("Opción no Valida")
        print()
