
#Inicio
numero_secreto = 777
respuesta_usuario = 0
contadorturnos = 0

print("****Si adivinas eres GOAT****")

while respuesta_usuario != numero_secreto :
    respuesta_usuario = int(input("Escribe un número: "))
    if respuesta_usuario < numero_secreto :
        print("*Una Pista*, El número secreto es más alto crack.")
        contadorturnos += 1
    if respuesta_usuario > numero_secreto :
        print("*Una Pista*, Te has pasado 3 pueblos el número secreto es más bajo.")
        contadorturnos += 1
    if respuesta_usuario == numero_secreto :
        print("¡VAMOOOOOSS! chaval lo has hecho de maravilla.")
        print(f"¡Y solo te ha tomado {contadorturnos} turnos en adivinarlo, te has fumado un porrazo chaval.")

#Fin Numero secreto
    

