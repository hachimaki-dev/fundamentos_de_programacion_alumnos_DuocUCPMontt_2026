# --- FUNCIONES DE VALIDACIÓN Y UTILERÍA ---

def solicitar_entero_positivo(mensaje):
    """
    Usa un bucle while para asegurar que el usuario ingrese un número entero mayor a 0.
    """
    while True:
        entrada = input(mensaje)
        # Verificamos si la entrada contiene solo dígitos usando un bucle for
        es_digito = True
        if not entrada: # Si presiona enter sin escribir nada
            es_digito = False
        else:
            for caracter in entrada:
                if caracter < '0' or caracter > '9':
                    es_digito = False
                    break
        
        if es_digito:
            numero = int(entrada)
            if numero > 0:
                return numero
        
        print("Valor inválido. Debes ingresar un número entero mayor a 0.")

def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")


# --- FUNCIONES PRINCIPALES DEL SISTEMA ---

def consultar_disponibles(disponibles):
    print(f"Actualmente hay {disponibles} habitaciones disponibles.")

def realizar_check_in(disponibles, historial):
    cantidad = solicitar_entero_positivo("¿Cuántas habitaciones deseas reservar? ")
    
    if cantidad > disponibles:
        print(f"No hay suficientes habitaciones disponibles. Solo quedan {disponibles}.")
        return disponibles, historial
    else:
        disponibles -= cantidad
        historial += cantidad
        print(f"Check-in realizado. Se reservaron {cantidad} habitaciones.")
        print(f"Habitaciones disponibles ahora: {disponibles}.")
        return disponibles, historial

def realizar_check_out(disponibles, historial, capacidad_maxima):
    cantidad = solicitar_entero_positivo("¿Cuántas habitaciones deseas liberar? ")
    
    # Validamos que al liberar habitaciones no superemos las 50 totales del hotel
    if disponibles + cantidad > capacidad_maxima:
        print(f"No puedes liberar esa cantidad. Superarías la capacidad máxima del hotel ({capacidad_maxima} habitaciones).")
        return disponibles, historial
    else:
        disponibles += cantidad
        historial -= cantidad
        print(f"Check-out realizado. Se liberaron {cantidad} habitaciones.")
        print(f"Habitaciones disponibles ahora: {disponibles}.")
        return disponibles, historial

def consultar_historial(historial):
    print(f"Historial neto de ocupaciones en esta sesión: {historial} habitaciones.")


# --- FLUJO PRINCIPAL DEL PROGRAMA ---

def iniciar_programa():
    # Variables de estado inicial
    CAPACIDAD_MAXIMA = 50
    habitaciones_disponibles = 50
    historial_neto = 0
    
    print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
    
    # Bucle principal interactivo
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            consultar_disponibles(habitaciones_disponibles)
        
        elif opcion == "2":
            # Las funciones modifican las variables y las devuelven actualizadas
            habitaciones_disponibles, historial_neto = realizar_check_in(
                habitaciones_disponibles, historial_neto
            )
            
        elif opcion == "3":
            habitaciones_disponibles, historial_neto = realizar_check_out(
                habitaciones_disponibles, historial_neto, CAPACIDAD_MAXIMA
            )
            
        elif opcion == "4":
            consultar_historial(historial_neto)
            
        elif opcion == "5":
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break # Rompe el bucle 'while' para cerrar el programa
            
        else:
            print("Opción no válida. Por favor selecciona una opción del 1 al 5.")

# Ejecución de la aplicación
iniciar_programa()