#instrucciones 
#crear diagrama e flujos de algoritmo del algoritmo solicitado
#solo cuando mi diagrama de flujos ha sido validado entonces, crear mi codiigo

#1crear un algoritmo que obligue al ususario a adivinar un numero secreto previamnete determinado para el sistema(del 1 al 10). si falla. indicarle el fallo y solicitarle que vuelva a itentarlo. si acierta lo felicitamos y terminamos el programa.Respuesta = input(adivine el numero secreto 

numero_adivinado = 0
numero_secreto = 6
while numero_adivinado != numero_secreto : 
    numero_adivinado = int(input("escoja un numero entre el 1 y 10"))
    if numero_secreto != numero_adivinado :
        print("fallaste, vuelve  intentarlo")
print("ganaste")
