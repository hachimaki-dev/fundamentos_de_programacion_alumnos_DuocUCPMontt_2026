#Crear diagrama de flujo del algoritmo solicitado 
#Solo cuando mi diagrama de flujo ha sido validado crear codigo
#Crear un algoritmo que obligue al usuario a adivinar un numero secreto previamente 
#determinado por el sistema(del 1 al 10), si falla indicarle que fallo y solicitarle que vuelva a intentarlo.
#Si acierta lo felicitamos y termina el programa

numero_secreto = 6
numero_adivinado = 0
while numero_secreto != numero_adivinado :
    numero_adivinado = int(input("Por favor ingrese un número del 1 al 10: "))
    if numero_secreto != numero_adivinado :
        print("FALLASTE! Intentalo denuevo...")
print("ACERTASTE!!!!")





