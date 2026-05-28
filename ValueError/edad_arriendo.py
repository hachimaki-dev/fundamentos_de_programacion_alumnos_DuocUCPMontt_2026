# Edad de un conductor para arriendo de autos
# Una empresa de arriendo de vehículos solicita la edad del conductor. Debe ser un entero positivo (nadie tiene -3 años ni 0 años).

# El programa debe pedir la edad repetidamente hasta recibir un valor válido. Luego muestra:
try:
    edad_conductor = int(input("Ingrese la edad del conductor :"))
    if edad_conductor < 0:
        print("Debe ser un numero positivo")
    else:
        print(f"edad registrada : {edad_conductor} años")
except ValueError:
    print("Dato invalido. Debe ser un numero positivo ")