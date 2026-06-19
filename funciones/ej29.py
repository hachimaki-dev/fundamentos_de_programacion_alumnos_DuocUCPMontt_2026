vehiculos = []

# ==================== MENÚ ====================

def mostrarMenu():
    print("=== MENÚ GESTIÓN DE VEHÍCULOS ===")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar estados")
    print("5. Mostrar vehículos")
    print("6. Salir")

def leerOpcion():
    while True:
        try:
            opcion_validada = int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("Ingrese una opción válida.")
    return opcion_validada

# ==================== VALIDACIONES ====================

def validarPatente(patente):
    return patente.strip() != ""

def validarKilometraje(km):
    return isinstance(km, int) and km > 0

def validarCostoReparacion(costo):
    return 10000.0 <= costo <= 500000.0

# ==================== FUNCIONES PRINCIPALES ====================

def pedirDatosVehiculo():
    # Patente
    while True:
        patente = input("Ingrese patente: ")
        if validarPatente(patente):
            break
        print("La patente no puede estar vacía.")

    # Kilometraje
    while True:
        try:
            km = int(input("Ingrese kilometraje: "))
            if validarKilometraje(km):
                break
            print("El kilometraje debe ser mayor que 0.")
        except ValueError:
            print("Ingrese un número entero válido.")

    # Costo reparación
    while True:
        try:
            costo = float(input("Ingrese costo de reparación (10000 - 500000): "))
            if validarCostoReparacion(costo):
                break
            print("El costo debe estar entre 10000.0 y 500000.0.")
        except ValueError:
            print("Ingrese un número válido.")

    reparado = costo <= 100000.0

    vehiculo = {
        "patente": patente.strip().upper(),
        "kilometraje": km,
        "costo_reparacion": costo,
        "reparado": reparado
    }
    return vehiculo

def agregarVehiculo():
    vehiculo = pedirDatosVehiculo()
    vehiculos.append(vehiculo)
    print(f"Vehículo {vehiculo['patente']} agregado correctamente.")

def buscarVehiculo(patente):
    patente = patente.strip().upper()
    for i in range(len(vehiculos)):
        if vehiculos[i]["patente"] == patente:
            return i
    return -1

def ejecutarBusqueda():
    patente = input("Ingrese patente a buscar: ")
    posicion = buscarVehiculo(patente)
    if posicion != -1:
        v = vehiculos[posicion]
        print(f"Vehículo encontrado en posición {posicion}:")
        print(f"  Patente        : {v['patente']}")
        print(f"  Kilometraje    : {v['kilometraje']}")
        print(f"  Costo reparac. : {v['costo_reparacion']}")
        print(f"  Reparado       : {v['reparado']}")
    else:
        print("Vehículo no encontrado.")

def eliminarVehiculo():
    patente = input("Ingrese patente a eliminar: ")
    posicion = buscarVehiculo(patente)
    if posicion != -1:
        vehiculos.pop(posicion)
        print(f"Vehículo {patente.strip().upper()} eliminado correctamente.")
    else:
        print("Vehículo no encontrado.")

def actualizarEstados():
    for i in range(len(vehiculos)):
        if vehiculos[i]["costo_reparacion"] <= 100000.0:
            vehiculos[i]["reparado"] = True
        else:
            vehiculos[i]["reparado"] = False
    print("Estados actualizados correctamente.")

def mostrarVehiculos():
    if len(vehiculos) == 0:
        print("No hay vehículos registrados.")
    else:
        print("=" * 55)
        print(f"{'PATENTE':<12} {'KM':>10} {'COSTO':>14} {'REPARADO':>10}")
        print("=" * 55)
        for v in vehiculos:
            print(f"{v['patente']:<12} {v['kilometraje']:>10} {v['costo_reparacion']:>14.2f} {str(v['reparado']):>10}")
        print("=" * 55)

# ==================== EJECUTAR OPCIÓN ====================

def ejecutarOpcionMenu():
    opcion = leerOpcion()

    if opcion == 1:
        agregarVehiculo()
    elif opcion == 2:
        ejecutarBusqueda()
    elif opcion == 3:
        eliminarVehiculo()
    elif opcion == 4:
        actualizarEstados()
    elif opcion == 5:
        mostrarVehiculos()
    elif opcion == 6:
        print("Saliendo del sistema. ¡Hasta luego!")
    else:
        print("Ingrese una opción válida.")

    return opcion

# ==================== PROGRAMA PRINCIPAL ====================

opcion = 0
while opcion != 6:
    mostrarMenu()
    opcion = ejecutarOpcionMenu()