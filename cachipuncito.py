opcion_jugador1 =""
opcion_jugador2 =""
marcador_jugador1 = 0
marcador_jugador2 = 0

print("******inicio Cachipun******")
print("******Eliga entre piedra, papel o tijera*****")


opcion_jugador1 = input("J1: Eliga piedra, papel o tijera")
opcion_jugador2 = input("J1: Eliga piedra, papel o tijera")
#si empatan las piedras 
if opcion_jugador1 =="piedra" and opcion_jugador2 == "piedra" :
    print("Empate vuelva a inventario")
#si gana con piedra    
elif ocpion_jugador1 =="piedra" and opcion_jugador2 == "tijera" :
    print("El jugador 1 gana 1 punto")
    print(f"El J1 tiene {marcador_jugador1}")
 #si pierde piedra
 elif opcion_jugador1 == "piedra" and opcion_jugador2 =="papel" :
    print("El jugador 1 gana 1 punto")
    print(f"El J1 tiene {marcador_jugador}")



