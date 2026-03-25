#Crear diagrama de flujos del algoritmo solicitado
#Crear un algoritmo que obligue al usuario a adivinar un numero secreto previamente determinado por el sistema (del 1 al 10). Si falla, indicarle que falló y que tiene que intentarlo de nuevo. SI acierta se felicita y termina el programa
número_correcto = 9
número_usuario = 0
print("Adivina adivinador¿Cuál es el número correcto?")
while número_usuario != número_correcto:
    número_usuario = int(input("Ingrese un número del 1 al 10: "))
    if número_usuario != número_correcto:
        print("fallaste")
    
  
    
print("felicidades has ganado FIN")





