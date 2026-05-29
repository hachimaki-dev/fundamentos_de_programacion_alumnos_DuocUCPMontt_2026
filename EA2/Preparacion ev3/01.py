#1A

#while True:
#    try:
#        numero=int(input("Ingrese un numero:"))
#        break
#    except ValueError:
#        print ('Numero no valido')

#1B
while True:
    try:
        pasajeros= int(input('Ingrese numero de pasajeros: '))
        if pasajeros <= 0:
            raise ValueError
        break
    except ValueError:
        print ('Ingrese un numero entero postivo de pasajeros')
    

print (f"Vuelo registrado con {pasajeros} pasajeros")