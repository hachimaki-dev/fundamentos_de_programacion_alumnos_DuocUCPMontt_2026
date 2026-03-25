#intrucciones
#crear diagrama de flujos del algoritmo solicitado
#solo cuad validado,entonces, crear codigo

#1 crear un algoritmo que obligue al usuario a adivinar un numero secreto previamente determinado por el sistema (del 1 al 10). si falla, indicarle que falloi silicitarle que vuelva a intentarlo, su acuerto
#lo felecitamos y termino el programa

n_secreto = 8
n_usuario = 0
while n_secreto != n_usuario:
 print("-------------BIENVENIDO------------")
 print("adivine el numero entre 1 y 10")
 n_usuario = int(input("coloque aqui su numero: "))
 if n_secreto != n_usuario:
          print("EQUIVOCADO")
print("------GANASTE------")