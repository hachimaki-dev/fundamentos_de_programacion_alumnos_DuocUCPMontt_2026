""" NIVEL 5 — Menú con while + operaciones sobre stock
Habilidad que desarrollas: Menú interactivo que no cierra hasta que el usuario decida salir, con operaciones que modifican variables de estado.**

Ejercicio 14 — Sistema de caja de una cafetería
Una cafetería comienza con $0 en caja. El cajero trabaja con el siguiente menú:

=== SISTEMA DE CAJA CAFETERÍA CAMPUS ===
1. Ver saldo en caja
2. Registrar venta (ingresa monto)
3. Registrar gasto (ingresa monto)
4. Salir
Reglas:

Las ventas suman al saldo
Los gastos restan, pero no se puede gastar más de lo que hay en caja
Monto siempre es entero positivo (validar)
El menú se repite hasta que se elija salir
Al salir: "Cierre de caja: $45.300 en caja. Hasta mañana." """
saldo_caja = 0
gasto = 0
total = 0
while True:
    try:
        opcion_usuario = int(input("=== SISTEMA DE CAJA CAFETERÍA CAMPUS ===\n 1.ver saldo en caja\n 2.registrar venta\n 3.Registrar gasto\n 4.salir"))
        
        if opcion_usuario == 1:
            print(f"saldo de caja : {total}")
        
        elif opcion_usuario == 2:
            saldo_caja = int(input("ingresa el monto de venta: "))
            if saldo_caja > 0:
                total += saldo_caja 
            else:
                print("el monto de la venta debe ser en numero positivos")

        elif opcion_usuario == 3:
            gasto = int(input("ingresa el monto de gasto: "))
            if gasto < 0:
                print("no puedes poner un gasto negativo")
            elif gasto > total:
                print("el gasto no puede exceder el total de la caja")
            else :
                 total -= gasto
                 
        
        elif opcion_usuario == 4:
            print(f"Cierre de caja: {total}  en caja. Hasta mañana.")
            break
        
        else:
            print("ingresa una opcion valida del 1 al 4 no mas")
    
    except ValueError:
        print("por favor ingresa numero reales ")

    