import time

opcion_usuario1 = ""
opcion_usuario2 = ""
puntaje_usuario1 = 0
puntaje_usuario2 = 0
print("Vamos a jugar cachipun, solo 3 rondas")
for x in range(3):
    print("1- piedra")
    print("2- papel")
    print("3- tijera")
    opcion_usuario1 = int(input("Escoge tu opcion"))
    print("1- piedra")
    print("2- papel")
    print("3- tijera")
    opcion_usuario2 = int(input("Escoge tu opcion"))
    if opcion_usuario1 == 1 and opcion_usuario2 == 1:
        print("empate")

    elif opcion_usuario1 == 2 and opcion_usuario2 == 2:
        print("empate")
        
    elif opcion_usuario1 == 3 and opcion_usuario2 == 3:
        print("empate")
        
    elif opcion_usuario1 == 3 and opcion_usuario2 == 2:
        puntaje_usuario1 = puntaje_usuario1 + 1
        print("Usuario 1 gana")
    elif opcion_usuario1 == 2 and opcion_usuario2 == 3:
        puntaje_usuario2 = puntaje_usuario2 + 1
        print("Usuario 2 gana")
        
    elif opcion_usuario1 == 1 and opcion_usuario2 == 3:
        puntaje_usuario1 = puntaje_usuario1 + 1
        print("Usuario 1 gana")
    elif opcion_usuario1 == 3 and opcion_usuario2 == 1:
        puntaje_usuario2 = puntaje_usuario2 + 1
        print("Usuario 2 gana")
        
    elif opcion_usuario1 == 2 and opcion_usuario2 == 1:
        puntaje_usuario1 = puntaje_usuario1 + 1
        print("Usuario 1 gana")
    elif opcion_usuario1 == 1 and opcion_usuario2 == 2:
        puntaje_usuario2 = puntaje_usuario2 + 1
        print("Usuario 2 gana")
    else:
        print("Turno no valido")
if puntaje_usuario1 < puntaje_usuario2:
    print("El jugador numero 2 A GANADO")
    print("El jugador numero 2 A GANADO")
    print("El jugador numero 2 A GANADO")
    print("El jugador numero 2 A GANADO")
elif puntaje_usuario1 > puntaje_usuario2:
    print("El jugador numero 1 A GANADO")
    print("El jugador numero 1 A GANADO")
    print("El jugador numero 1 A GANADO")
    print("El jugador numero 1 A GANADO")
else:
    print("EMPATE FRACASADOS")
    print("EMPATE FRACASADOS")
    print("EMPATE FRACASADOS")
    print("EMPATE FRACASADOS")