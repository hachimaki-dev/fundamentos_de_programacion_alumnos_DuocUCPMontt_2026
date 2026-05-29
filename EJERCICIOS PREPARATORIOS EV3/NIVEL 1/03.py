#Ejercicio 3 — Edad de un conductor para arriendo de autos
#Una empresa de arriendo de vehículos solicita la edad del conductor. Debe ser un entero positivo (nadie tiene -3 años ni 0 años).

#El programa debe pedir la edad repetidamente hasta recibir un valor válido. Luego muestra:

#"Edad registrada: 29 años."
#Desafío extra: ¿Qué pasa si el usuario ingresa "veintinueve"? ¿Tu código lo maneja?

while True:
    edad_conductor_ingresada = input("Ingresa tu edad: ")

    try:
        edad_conductor = int(edad_conductor_ingresada)

        if edad_conductor > 0:
            print(f"Edad registrada: {edad_conductor} años.")
            break
        else: 
            print("La edad debe ser un número mayor que 0.")

    except ValueError:
        print("Ingrese la edad en formato numérico.") 