#Instrucciones 
#Crear un diagrama de flujos del algoritmo solictidado
#Solo cuando mi diagrama de flujos ha sido validado, entonces, crear codigo
#Crear un algoritmo que obligue al usuario a adivinar un numero secreto previamente determinado por el sistema (del 1 al 10), Si falla, indicarle que fallo y solicitarle que vuelva a intentarlo.So acierta, lo felictimaos y termina el programa

numero_secreto = 6
numero_usuario = 0
while numero_usuario != numero_secreto :
    numero_usuario = int(input("eliga su numero de 1 al 10"))
    if numero_secreto == numero_usuario : 
        print("Has Acertado, Felicidades :)")
        break
    print("Has fallado,intentelo denuevo")


print("****FIN DEL PROGRAMA****")
    


     




   
  


