#Hacer un algoritmo en diagrama de flujos y luego de que lo valide mi compañero, crear el codigo


#Adivinar un numero determinado entre numero 1 y 10. Si el usuario se equivoca, volver a preguntar. Si el usuario acierta, entonces felicitarlos
NumeroAlmacenado =  6
NumeroSecreto = 0

while True:

    NumeroIngresado = int(input("ADIVINE EL NUMERO SECRETO \n Introduce un numero del 1 al 10: "))


    if NumeroIngresado != NumeroAlmacenado:
        print ("Intente de nuevo")
    else:
        break

print("Correcto")

