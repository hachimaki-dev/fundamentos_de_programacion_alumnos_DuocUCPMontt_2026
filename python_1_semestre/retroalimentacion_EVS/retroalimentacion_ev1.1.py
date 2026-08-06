# Ejercicio 2 (59 puntos)
# Desarrolle un programa en Python que permita gestionar y 
# analizar actividades diarias, calculando el tiempo total dedicado a ellas.

# El programa debe operar mediante un menú de opciones 
# que se repite continuamente hasta que el usuario decida salir.

# Paso 1: Inicio

# Mostrar el siguiente mensaje:
# “Registro de actividades diarias”

# Paso 2: Menú de opciones

# El programa debe presentar el siguiente menú:

# Registrar actividades
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

# Al finalizar el registro, el programa debe volver automáticamente 
# al menú principal.

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
# Uso de estructuras de repetición (por ejemplo, while o for).
# Uso de estructuras de decisión (if, elif, else).
# Mensajes claros, ordenados y comprensibles para el usuario.




contador = 0
tiempo_total = 0

while True:
    print("")
    print(" Registro de actividades diarias ")
    print("")
    print("Menú de opciones")
    print(" 1.Registrar Actividades")
    print(" 2.Mostrar Analisis del tiempo")
    print(" 3.Salir")

    menu_de_opciones = int(input("seleciona una opcion : "))
    if menu_de_opciones == 1:

        while True:
            actividades_registro = int(input("ingresa la cantidad de actividades a registrar : "))
            if actividades_registro >= 3:
                contador = 0
                tiempo_total = 0

                while contador <= actividades_registro:
                    nombre_actividad = input(f"ingresa el nombre de la actividad {contador + 1} : ")
                    contador +=1
                    
                    tiempo_actividad = int(input("cuanto tiempo toma la actividad en minutos? : "))
                    tiempo_total += tiempo_actividad
                    if contador == actividades_registro:
                        break
                break
            else:
                print("la cantidad de actividades a registrar tiene que ser mayor o igual que 3")

    elif menu_de_opciones == 2:
        print(f"el tiempo total acumulado de las actividades registradas es : {tiempo_total}")
        if tiempo_total > 180:
            print("Tiempo diario excesivo")
        else:
            print("Tiempo diario adecuado")

    elif menu_de_opciones == 3:
        print("Fin del registro")
        break

    else:
        print("ingresa un numero acorde al menu del 1 al 3")
        print("")




