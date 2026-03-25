#Instrucciones

#1Crear un algoritmo que obligue al usuario a adivinar un numero secreto previamente determinado por el sistema. Si falla indicarle que fallo y solicitarle que vuelva a intentarlo, si acierta lo felictamos y termina el programa

numero_secreto = 7 
numero_ingresado = 0
while numero_secreto != numero_ingresado : 
    numero_ingresado = int(input("Escoge un numero entre 1 y 10: "))
    if numero_ingresado != numero_secreto :
        print("FALLASTE!")

    
print("GANASTE!!")