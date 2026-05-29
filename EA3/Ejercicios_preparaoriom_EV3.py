# ------------------Ejercicio 1A ----------------------
# while True:
#     try:
#         numero = int(input("Ingrese un numero(numero entero): "))
#         if numero >= 0:
#             print(f"Número recibido: {numero}")
#             break
#         else:
#             print("Error: eso no es un número entero.")
    
#     except ValueError:
#         print("Error: eso no es un número entero.")



# ------------------Ejercicio 1B ----------------------
# try:
#     pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
#     if pasajeros >= 0:
#         print(f"Número recibido: {pasajeros}")
#     else:
#         print("Error: eso no es un número entero.")

# except ValueError:
#     print("Error: eso no es un número entero.")



# ------------------Ejercicio 2 ----------------------
# try:
#     cantidad_de_unidades_del_medicamento = int(input("Ingrese la cantidad del medicamento: "))
#     if cantidad_de_unidades_del_medicamento > 0:
#         print(f"Stock registrado: {cantidad_de_unidades_del_medicamento} unidades disponibles.")
#     else:
#         print("Dato inválido. Ingresa un entero positivo para el stock.")
# except ValueError:
#     print("Dato inválido. Ingresa un entero positivo para el stock.")



# ------------------Ejercicio 20 ----------------------
stock_inicial = 60
capacidad_maxima = 60
historial = 0
while True:
    print("== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===")
    print("1. Ver equipos disponibles")
    print("2. Prestar equipo(s)")
    print("3. Recibir devolución")
    print("4. Ver historial de préstamos activos")
    print("5. Salir")

    Eleccion_del_usuario = int(input("Seleccione una opción: "))
    if Eleccion_del_usuario == 1:
        print(f"Hay {stock_inicial} equipos disponibles ")
        continue
    elif Eleccion_del_usuario == 2:
        stock_inicial -= 1
        historial +=1
        print(f"Se han prestado {historial} equipos hasta el momento")
        continue
    elif Eleccion_del_usuario == 3:
        print(f"")

