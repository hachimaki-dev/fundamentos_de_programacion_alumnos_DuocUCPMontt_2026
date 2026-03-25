#crear diagrama de flujos del algoritmo solicita
#solo cuando mi diagram de flujos ha sido validado, entonces , crear codigo

#crear un algoritmo que obligue al usuario a adivinar un numero secreto previamente determinado por el sistema. si falla indicarle que fallo y solicitarle que vuelva a intertarlo si acierta los felicitamos y termina el programa

print ("juguemos un juego")
print ("ganas si adivinas que numero elegi")

numero_s = 7
numero_a = 0

while numero_s != numero_a :
    numero_a = int(input ("elige un numero del 1-10 "))
    if numero_s != numero_a :
         print ("te equivocaste intentalo de nuevo")

         
print ("adivinaste, tu ganaste")

