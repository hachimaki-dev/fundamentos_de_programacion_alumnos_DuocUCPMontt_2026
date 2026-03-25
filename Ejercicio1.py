#Instruccioenes crear diagrama de flujos del algoritmo solicitado solo cuando mi diagrama de flujos haya sido validado crear codigo
#1 crear un algoritmo que obligue al usuario a adivinar un numero secreto previamente determinado por el sistema (del 1 al 10) si falla indicarle que fallo y que vuelva a intentarlo y si lo logra felicitarlo
numero_secreto = 3
numero_elegido = 0
while numero_secreto != numero_elegido:
     numero_elegido = int(input ("elige un numero del 1 al 10"))
if numero_elegido != numero_secreto:
    print("Fallaste")

print("Ganaste")
     



