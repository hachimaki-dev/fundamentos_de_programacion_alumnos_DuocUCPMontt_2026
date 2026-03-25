#crear diagrama de flujo del algoritmo solicitado
#solo cuando el diagrama de flujo ha sido validado entonces crear codigo
#1-crear un algoritmo que obligue al usuario a adivinar el un numero secreto del 1 al 10 previamente determinado por el sistema, si falla indicarle que fallo y solicitarle que vuelva a intentarlo, si acierta, felicitar y terminar el programa
numero_secreto=2 
numero_adivinado=int(input("adivina en que numero entre el 1 y el 10 estoy pensando: "))
while numero_secreto!=numero_adivinado:
    numero_adivinado=int(input("Has fallado, ingrese el numero nuevamente "))
print("Ganaste, has adivinado!!!!!")