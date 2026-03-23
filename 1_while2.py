# el ciclo while te funciona para este tipo de cosas, rompe la cadena con una interaccion o cambio de variable que vuelva la afirmacion falsa
opcion = int(input("ingrese un numero"))
contador = 0
while opcion == 1:
    print(f"hola mundo {contador}")
    contador += 1
    opcion = int(input("ingrese un numero"))



###se escribe:
#while true:
#    hago cosas