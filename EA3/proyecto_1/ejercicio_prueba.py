#Ejercicio 22 — Sistema completo de gestión de una clínica veterinaria
#Parte A (similar al Ejercicio 1 de evaluación):

#Una clínica veterinaria registra a los animales que ingresan. El sistema debe:

#Preguntar cuántos animales se registrarán (entero positivo, validado)
#Para cada animal:
#ID del animal: mínimo 6 caracteres, sin espacios (ej: GATO01, PERR7X, CONEJO2)
#Peso en kg: entero positivo, validado
#Clasificar:
#Peso > 25 kg → Paciente Grande
#Peso ≤ 25 kg → Paciente Pequeño
#Al finalizar:
#"La clínica ha registrado 3 pacientes grandes y 8 pacientes pequeños. ¡Bienvenidos!"
#Parte B (similar al Ejercicio 2 de evaluación):

#La misma clínica gestiona sus horas de atención (stock inicial: 30 horas disponibles al día).

#=== AGENDA CLÍNICA VETERINARIA PATITAS ===
#1. Ver horas disponibles
#2. Reservar hora(s)
#3. Cancelar hora(s)
#4. Ver historial de reservas
#5. Salir
#Implementa todas las reglas de validación correspondientes.

#Referencia Rápida de Patrones
#Patrón 1: Validar un entero positivo
#while True:
    #try:
        #valor = int(input("Ingresa un valor: "))
        #if valor > 0:
            #break
        #else:
            #print("Error: debe ser mayor que cero.")
    #except ValueError:
        #print("Error: debe ser un número entero.")
#Patrón 2: Validar un string (largo mínimo, sin espacios)
#while True:
    #nombre = input("Ingresa el nombre: ")
    #if len(nombre) >= 6 and " " not in nombre:
        #break
    #else:
        #print("Inválido: mínimo 6 caracteres, sin espacios.")
#Patrón 3: Bucle for con N validado
# Primero validar N
#while True:
    #try:
        #n = int(input("¿Cuántos registros? "))
        #if n > 0:
            #break
        #print("Debe ser mayor que cero.")
    #except ValueError:
        #print("Solo enteros positivos.")

# Luego iterar
#for i in range(n):
    # validar cada campo adentro del for
    #pass
#Patrón 4: Menú con while
#while True:
    #print("1. Opción A")
    #print("2. Opción B")
    #print("3. Salir")
    #opcion = input("Elige: ")
    
    #if opcion == "1":
        #pass  # lógica opción 1
    #elif opcion == "2":
        #pass  # lógica opción 2
    #elif opcion == "3":
        #print("Hasta pronto.")
        #break
    #else:
        #print("Opción inválida.")
#Patrón 5: Gestión de stock con historial
stock = 100        # unidades disponibles
capacidad = 100    # máximo posible
historial = 0      # unidades actualmente en uso/prestadas (NO es conteo de operaciones)

# ¿Qué significa historial?
# historial acumula UNIDADES, no operaciones.
# Ejemplo: si se prestan 10 y luego 5, historial = 15 (no 2).
# Si luego se devuelven 3, historial = 12.

# Operación de "entrada/reserva" (disminuye stock):
# - validar que cantidad > 0
# - validar que cantidad <= stock
# stock -= cantidad
# historial += cantidad

# Operación de "salida/devolución" (aumenta stock):
# - validar que cantidad > 0
# - validar que cantidad <= historial  ← no puedes devolver más de lo prestado
# stock += cantidad
# historial -= cantidad

#datos iniciales
stock_horas = 30
historial_reservas = 0
reservas = [] #  Lista para almacenar detalles de cada reserva (opcional, para mostrar historial detallado)

# Parte A: registro de animales
while True:
    try:
        num_animales = int(input("¿Cuantos animales se registraran? "))
        if num_animales > 0:
            break
        else:
            print("Error: debe ser un numero entero positivo.")
    except ValueError:
        print("Error: debe ser un numero entero positivo.")

# Contadores para clasificar animales
contador_grandes = 0
contador_pequeños = 0

for i in range(num_animales):
    while True:
        id_animal = input(f"ID del animal #{i+1}: ")
        if len(id_animal) >= 6 and " " not in id_animal:
            break
        else:
            print("Invalido: minimo 6 caracteres, sin espacios.")
    
    while True:
        try:
            peso = int(input(f"peso en kg del animal #{i+1}: "))
            if peso > 0:
                break
            else:
                print("Error: debe ser un numero entero positivo.")
        except ValueError:
            print("Error: debe ser un numero entero positivo.")
    
    if peso > 25:
        contador_grandes += 1
    else:
        contador_pequeños += 1

print(f"La clinica ha registrado {contador_grandes} pacientes grandes y {contador_pequeños} pacientes pequeños. ¡Bienvenidos!")

# Parte B: sistema de gestion de horas
while True:
    print("=== AGENDA CLINICA VETERINARIA PATITAS ===")
    print("1. Ver horas disponibles")
    print("2. Reservar hora(s)")
    print("3. Cancelar hora(s)")
    print("4. Ver historial de reservas")
    print("5. Salir")
    opcion = input("elige: ")
    
    if opcion == "1":
        print(f"Horas disponibles: {stock_horas}")
    elif opcion == "2":
        while True:
            try:
                horas_reservar = int(input("¿Cuantas horas desea reservar? "))
                if horas_reservar > 0 and horas_reservar <= stock_horas:
                    stock_horas -= horas_reservar
                    historial_reservas += horas_reservar
                    reservas.append(horas_reservar)
                    print(f"Reserva exitosa. Horas restantes: {stock_horas}")
                    break
                else:
                    print("Error: debe ser un numero entero positivo y no puede exceder las horas disponibles.")
            except ValueError:
                print("Error: debe ser un numero entero positivo.")
    elif opcion == "3":
        while True:
            try:
                horas_cancelar = int(input("¿Cuantas horas desea cancelar? "))
                if horas_cancelar > 0 and horas_cancelar <= historial_reservas:
                    stock_horas += horas_cancelar
                    historial_reservas -= horas_cancelar
                    print(f"Cancelacion exitosa. Horas disponibles: {stock_horas}")
                    break
                else:
                    print("Error: debe ser un numero entero positivo y no puede exceder las horas reservadas.")
            except ValueError:
                print("Error: debe ser un numero entero positivo.")
    elif opcion == "4":
        print(f"Historial de reservas: {historial_reservas} horas reservadas.")
    elif opcion == "5":
        print("Hasta pronto.")
        break
    else:
        print("Opcion invalida. Por favor elija una opcion del menu.")   
                
