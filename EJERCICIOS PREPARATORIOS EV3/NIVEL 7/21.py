# Ejercicio 21 — Sistema de gestión de mesas en un restaurante
# Un restaurante tiene 20 mesas disponibles.

# 
# Reglas:

# No puedes asignar más mesas de las disponibles
# No puedes liberar más mesas de las que están ocupadas (pista: mesas_ocupadas = capacidad - disponibles)
# Historial refleja ocupación actual (sube con asignación, baja con liberación)
# Al salir: "Servicio finalizado. Buenas noches."
# Este ejercicio es el más cercano a lo que verás en la evaluación. Resuélvelo sin mirar los anteriores.

capacidad_max= 20
ocupadas = 0

menu = ["1", "2", "3", "4", "5"]


while True:
    print("""\n=== SISTEMA DE MESAS - RESTAURANTE EL FARO ===
1. Ver mesas disponibles
2. Asignar mesa(s)
3. Liberar mesa(s)
4. Mesas ocupadas actualmente
5. Salir""")
    
    while True:
        opcion = input("Ingresa la acción a realizar: ")
        if opcion in menu:
            break
        else:
            print("Error: Ingresa una opción válida")
    
    if opcion == "5":
        print("\nServicio finalizado. Buenas noches.")
        break

    elif opcion == "1":
        mesas_disponibles = capacidad_max - ocupadas
        print(f"Hay {mesas_disponibles} mesas disponibles")

    elif opcion == "2":
        while True:
            try:
                asignar = int(input("\nCantidad de mesas a asignar:"))
                if asignar <= 0:
                    print("Error: La asignación debe ser mayor a 0.")
                elif (asignar + ocupadas) > capacidad_max:
                    print("Error: Se supera la capacidad máxima de mesas.")
                else:
                    ocupadas += asignar
                    if ocupadas == capacidad_max:
                        print("Se han ocupado todas la mesas.")
                    print(f"Asignaste {asignar} mesas.")
                    break
            except ValueError:
                print("Error: La asignación de mesas es en formato numérico")

    elif opcion == "3":
        while True:
            try:
                liberar = int(input("\nCantidad de mesas a liberar: "))
                if liberar <= 0:
                    print("Error: La liberación de mesas debe ser mayor a 0.")
                elif liberar > ocupadas:
                    print("Error: No puedes liberar más mesas de las que están ocupadas.")
                else:
                    ocupadas -= liberar
                    print(f"Liberaste {liberar} mesas")
                    break
            except ValueError:
                print("Error: La liberación de mesas debe ser en formato numérico.")

    elif opcion == "4":
        print(f"\nHay {ocupadas} mesas ocupadas")