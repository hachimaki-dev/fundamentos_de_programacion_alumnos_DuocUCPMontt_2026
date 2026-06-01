#Ejercicio 3 — Edad de un conductor para arriendo de autos
#Una empresa de arriendo de vehículos solicita la edad del conductor. Debe ser un entero positivo (nadie tiene -3 años ni 0 años).

#El programa debe pedir la edad repetidamente hasta recibir un valor válido. Luego muestra:

#"Edad registrada: 29 años."
#Desafío extra: ¿Qué pasa si el usuario ingresa "veintinueve"? ¿Tu código lo maneja?

while True:
    try:
        edad=int(input("\nIngrese su edad: "))
        if edad<1:
            print("Edad no válida. Por favor, ingrese un número entero positivo.")
        elif edad<18:
            print("Lo siento, no puedes arrendar un vehículo. Debes tener al menos 18 años.")
        elif edad>65:
            print("Lo siento, no puedes arrendar un vehículo. Debes tener menos de 65 años...\nJuvilese, ¿no? :D")
        else:
            print(f"Edad registrada: {edad} años.\n")
            break
    except ValueError:
        print("Formato no válido. Por favor, ingrese un número entero positivo.")