vidaplayer = 100
print("bienvenido. pelea contra el jefe, suerte")
mana = 20
jefe = 150
while vidaplayer > 0 and jefe > 0 :
    print("elije una opcion")
    print("atacar")
    print("magia")
    print("pocion de vida")
    respuesta = input("ingrese su opcion (escribe igual)")
    if respuesta == "atacar" :
        jefe = jefe - 20
        print("el jefe a perdido 20 de vida")
    elif respuesta == "magia" :
        if mana > 0 :
            jefe = jefe - 50
            print(f"el jefe a perdido 50 de vida, pero has perdido mana te queda {mana}")
        elif mana < 0 :
            print("no hay mana suficiente, el jefe no recibe daños")
    elif respuesta == "pocion de vida" :
        print("has usado pocion de vida")
        vidaplayer = vidaplayer + 30
        print(f"el jugador se ha curado 30, nueva vida {vidaplayer}")
        mana = 0
        print("se ha gastado todo tu mana")
    
    vidaplayer = vidaplayer - 15 
    print("el jefe ha atacado, ha quitado 15 de vida")
    print(f"la nueva vida del player es {vidaplayer}")

if jefe < 0 :
    print("has derrotado al jefe, felicidades")
elif vidaplayer > 0 :
    print("perdiste, vuelve a intentarlo")
