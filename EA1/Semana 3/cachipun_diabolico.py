opcion_usuario1 = ""
opcion_usuario2 = ""

puntaje_usuario1 = 0
puntaje_usuario2 = 0

print("*****Bienvenido al cachipun extremo devil*****")
print("*****Por favor escriba la palabra piedra, papel o tijeras*****")

while puntaje_usuario1 < 3 and puntaje_usuario2 < 3 :
    opcion_usuario1 = input("J1 - Por favor ingrese su elección")
    opcion_usuario2 = input("J2 - Por favor ingrese su elección")

    #Aca J1 Pierde y J2 Gana
    if opcion_usuario1 == "piedra" and opcion_usuario2 == "papel" :
        puntaje_usuario2 = puntaje_usuario2 + 1
        print(f"J2 haz acumulado 1 victoria")
        print(f"J2 tu puntaje actual es {puntaje_usuario2}")

    #Aca J1 gana y j2 PIERDE
    elif opcion_usuario1 == "piedra" and opcion_usuario2 == "tijeras" :
        puntaje_usuario1 = puntaje_usuario1 + 1
        print(f"J1 haz acumulado 1 victoria")
        print(f"J1 tu puntaje actual es {puntaje_usuario1}")

    #Aca J1  y J2 EMPAATAN
    elif opcion_usuario1 == "piedra" and opcion_usuario2 == "piedra" :
        print(f"EMPATE - Vuelva a jugar")
        

    elif opcion_usuario1 == "papel" and opcion_usuario2 == "tijeras" :
        puntaje_usuario2 = puntaje_usuario2 + 1
        print(f"J2 haz acumulado 1 victoria")
        print(f"J2 tu puntaje actual es {puntaje_usuario2}")

    #Aca J1 gana y j2 PIERDE
    elif opcion_usuario1 == "papel" and opcion_usuario2 == "piedra" :
        puntaje_usuario1 = puntaje_usuario1 + 1
        print(f"J1 haz acumulado 1 victoria")

    #Aca J1  y J2 EMPAATAN
    elif opcion_usuario1 == "papel" and opcion_usuario2 == "papel" :
        print(f"EMPATE - Vuelva a jugar")
        
    elif opcion_usuario1 == "tijeras" and opcion_usuario2 == "piedra" :
        puntaje_usuario2 = puntaje_usuario2 + 1
        print(f"J2 haz acumulado 1 victoria")
        print(f"J2 tu puntaje actual es {puntaje_usuario2}")

    #Aca J1 gana y j2 PIERDE
    elif opcion_usuario1 == "tijeras" and opcion_usuario2 == "papel" :
        puntaje_usuario1 = puntaje_usuario1 + 1
        print(f"J1 haz acumulado 1 victoria")
        print(f"J1 tu puntaje actual es {puntaje_usuario1}")

    #Aca J1  y J2 EMPAATAN
    elif opcion_usuario1 == "tijeras" and opcion_usuario2 == "tijeras" :
        print(f"EMPATE - Vuelva a jugar")
        

if puntaje_usuario1 > puntaje_usuario2 :
    print("j1 haz ganado todo el juego eres el mejor")
else:
    print("j2 haz ganado todo el juego eres el mejor")


print("Gracias por jugar")