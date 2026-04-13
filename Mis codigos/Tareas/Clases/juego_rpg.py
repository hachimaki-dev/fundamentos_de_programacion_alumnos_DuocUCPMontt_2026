Jefe = 1000
fire_ball = 200
aporrear = 100
kamehameha = 500

nombre_usuario = input("Hola mercenario, ¿cual es tu nombre?.")

print()
print(f"Perfecto {nombre_usuario}. Comencemos la aventura.")
print()
print("Te encuentras en una mazmorra, hay un titan colosal frente a ti. Cuentas con los siguientes poderes malditos; (1)fire ball (2)aporrear y (3)kamehameha. ")
print()
print(f"\n\n Jefe HP:{Jefe} \n\n")

ataque = input("¿Que poder maldito desear usar? Recuerda ingresar el nùmero asignado al poder")
if ataque == "1":
    Jefe = Jefe - fire_ball
elif ataque == "2":
    Jefe = Jefe - aporrear
elif ataque == "3":
    Jefe = Jefe - kamehameha
else:
    print("Ataque no válido")
    
while Jefe > 0:
    print(f"---Al jefe le quedan {Jefe} HP---")
    print("....sigue atacando....")
    ataque = input("Elije otro ataque")
    if ataque == "1":
        Jefe = Jefe - fire_ball
        print(f"Lanzaste una bola de fuego ---Al Jefe le quedan {Jefe} HP---")
    elif ataque == "2":
        Jefe = Jefe - aporrear
        print(f"Le diste un combo ---Al jefe le quedan {Jefe} HP---")
    elif ataque == "3":
        Jefe = Jefe - kamehameha
        print(f"Lanzaste una honda vital ---Al jefe le quedan {Jefe} HP---")
    else:
        print("No válido")








print("\n-Felicidades-\n\n-Haz derrotado a la bestia-\n\nYou Win\n")