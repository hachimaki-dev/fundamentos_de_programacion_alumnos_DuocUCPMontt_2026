#crear diagrama de flujos del algoritmo solicitado, 
#solo cuando mi diagrama ha sido validado.
#entonces crear codigo:

#crear un algortimo que oblige al usuario a adivinar un numero secreto previamente
#determinado por el sistema. si falla, indicarle que fallo y solicitarlo denuevo. si
#cierta, lo felicitamos y termina el programa.

#del 1 al 10

numero_secreto = 7
numero_adivinado = 0

while numero_secreto != numero_adivinado :
    numero_adivinado = int (input("escoja un numero entre el 1 y el 10 = "))
    print("fallaste")

print("ganaste")

#teraea

#crear un diagrama de flujos y programarlo sobre un cachipun de juego local, el juego se termina cuando uno de los dos jugadores llega a 3 victorias