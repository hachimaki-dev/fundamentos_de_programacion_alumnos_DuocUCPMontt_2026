#Ejercicio 3 — Edad de un conductor para arriendo de autos
#Una empresa de arriendo de vehículos solicita la edad del conductor. Debe ser un entero positivo (nadie tiene -3 años ni 0 años).

#El programa debe pedir la edad repetidamente hasta recibir un valor válido. Luego muestra:

#"Edad registrada: 29 años."
#Desafío extra: ¿Qué pasa si el usuario ingresa "veintinueve"? ¿Tu código lo maneja?

try:
    edad=int(input("\nPor favor ingrese su edad: "))
    if edad>0:
        print(f"Tu edad: {edad}\n")
    else: 
        print("Edad invalida, ingrese nuevamente: ")
except TypeError:
    print("Formato no valido, ingrese nuevamente: ")