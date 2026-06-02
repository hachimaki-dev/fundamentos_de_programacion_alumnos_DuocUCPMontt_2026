# Ejercicio 20 — Sistema de préstamos de equipos en una universidad
# La biblioteca de equipos tecnológicos de una universidad tiene 60 dispositivos disponibles (tablets, notebooks, etc.).

# Implementa:

# Stock inicial: 60 (equipos disponibles)
# Capacidad máxima: 60
# Préstamo reduce stock e incrementa historial (préstamos activos)
# Devolución aumenta stock y reduce historial
# Validar que préstamo no supere stock disponible
# Validar que devolución no supere los préstamos activos (es decir: devolución <= historial). No se puede devolver más equipos de los que están prestados.
# Todos los valores deben ser enteros positivos
# Menú se repite hasta seleccionar salir
# Al salir: "Gracias por utilizar el sistema. Hasta pronto."
# Aclaración: historial en este contexto representa la cantidad de equipos actualmente prestados (no un conteo de operaciones). Si se prestan 10 y luego se devuelven 3, historial = 7.

stock_inicial = 60
capacidad_max = 60
historial = 0

menu = ["1", "2", "3", "4", "5"]

while True:
    print("""\n=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===
    1. Ver equipos disponibles
    2. Prestar equipo(s)
    3. Recibir devolución
    4. Ver historial de préstamos activos
    5. Salir""")

    while True:
        opcion = input(":")
        if opcion in menu:
            break
        else:
            print("Error: ingrese una opción válida")

    if opcion == "5":
        print("\nGracias por utilizar el sistema. Hasta pronto.")
        break

    elif opcion == "1":
        equipos_disponibles = stock_inicial
        print(f"\nHay {equipos_disponibles} equipos disponibles.")

    elif opcion == "2":
        while True:
            try:
                prestamo = int(input("\nCantidad de equipos prestados: "))
                if prestamo <= 0:
                    print("Error: la cantidad debe ser mayor a 0.")
                elif prestamo > stock_inicial:
                    print("Error: No se pueden prestar más equipos de los disponibles.")
                else:
                    historial += prestamo
                    stock_inicial -= prestamo
                    print(f"Se prestaron {prestamo} equipo(s)")
                    break
            except ValueError:
                print("Error: El prestamo se ingresa en formato numérico.")

    elif opcion == "3":
        while True:
            try:
                devolucion = int(input("\nCantidad devolución de equipos: "))
                if devolucion <= 0:
                    print("Error: La cantidad no puede ser menor a 0.")
                elif devolucion > historial:
                    print("Error: No se puede devolver más equipos de los que están prestados.")
                else:
                    historial -= devolucion
                    stock_inicial += devolucion
                    print(f"Hubo una devolución de {devolucion} equipo(s).")
                    break
            except ValueError:
                print("Error: Las devoluciones se ingresan en formato numérico")

    elif opcion == "4":
        print(f"\nPréstamos activos: {historial} equipo(s)")