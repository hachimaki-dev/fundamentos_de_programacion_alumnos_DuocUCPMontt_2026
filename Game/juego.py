usuario_iniciado = False
id = ""
psw = 0
while usuario_iniciado == False:
    id = input("INGRESE SU USUARIO: ")
    if id == "seba":
        psw = int(input("ingrese su contraseña(numerica): "))
        if psw == 1234:
            print("acceso concedido")
            usuario_iniciado = True
        else:
            print("contraseña equivocada")
    else:
        print("usuario equivocado")
print("\nBienvenido a Fire Emblem 8000, que comience el juego....\napreta cualquier tecla para iniciar combate y revisar oponente. ")
input()
juego_iniciado = True
eleccion_menu_juego = 0
combate = True
vida_enemigo1 = 10
vida_enemigo2 = 10
vida_enemigo3 = 10
vida_aliado1 = 12
vida_aliado2 = 15
vida_aliado3 = 15
dañoataque = 10
eleccion_combate_aliado = 0
eleccion_combate_enemigo = 0
while juego_iniciado == True:
    eleccion_menu_juego = input(f"1)combate\n2)Revisar combatientes\n3)salir\n")
    if eleccion_menu_juego == "1":
        while combate == True:
            eleccion_combate_aliado = int(input(f"Escoja su aliado:\n1)Aliado1:\n2)Aliado2:\n3)Aliado3:\n"))
            eleccion_combate_enemigo = int(input(f"Escoja el enemigo:\nenemigo1:\nenemigo2:\nenemigo3:\n"))
            if eleccion_combate_aliado == 1 and eleccion_combate_enemigo == 1:
                vida_aliado1 -= 10
                vida_enemigo1 -=10
                print(f"el enemigo 1 tiene: {vida_enemigo1} de vida\nel enemigo 2 tiene: {vida_enemigo2} de vida\nel enemigo 3 tiene: {vida_enemigo3} de vida")
                print(f"el aliado 1 tiene: {vida_aliado1} de vida\nel aliado 2 tiene: {vida_aliado2} de vida\nel aliado numero 3 tiene: {vida_aliado3} de vida")   
            elif eleccion_combate_aliado == 2 and eleccion_combate_enemigo == 1:
                vida_aliado2 -=10
                vida_enemigo1 -=10
                print(f"el enemigo 1 tiene: {vida_enemigo1} de vida\nel enemigo 2 tiene: {vida_enemigo2} de vida\nel enemigo 3 tiene: {vida_enemigo3} de vida")
                print(f"el aliado 1 tiene: {vida_aliado1} de vida\nel aliado 2 tiene: {vida_aliado2} de vida\nel aliado numero 3 tiene: {vida_aliado3} de vida")
            elif eleccion_combate_aliado == 3 and eleccion_combate_enemigo == 1:
                vida_aliado3 -=10
                vida_enemigo1 -=10
                print(f"el enemigo 1 tiene: {vida_enemigo1} de vida\nel enemigo 2 tiene: {vida_enemigo2} de vida\nel enemigo 3 tiene: {vida_enemigo3} de vida")
                print(f"el aliado 1 tiene: {vida_aliado1} de vida\nel aliado 2 tiene: {vida_aliado2} de vida\nel aliado numero 3 tiene: {vida_aliado3} de vida")
            elif eleccion_combate_aliado == 1 and eleccion_combate_enemigo == 2:
                vida_aliado1 -=10
                vida_enemigo2 -=10
                print(f"el enemigo 1 tiene: {vida_enemigo1} de vida\nel enemigo 2 tiene: {vida_enemigo2} de vida\nel enemigo 3 tiene: {vida_enemigo3} de vida")
                print(f"el aliado 1 tiene: {vida_aliado1} de vida\nel aliado 2 tiene: {vida_aliado2} de vida\nel aliado numero 3 tiene: {vida_aliado3} de vida")
            elif eleccion_combate_aliado == 2 and eleccion_combate_enemigo == 2:
                vida_aliado2 -= 10
                vida_enemigo2 -= 10
                print(f"el enemigo 1 tiene: {vida_enemigo1} de vida\nel enemigo 2 tiene: {vida_enemigo2} de vida\nel enemigo 3 tiene: {vida_enemigo3} de vida")
                print(f"el aliado 1 tiene: {vida_aliado1} de vida\nel aliado 2 tiene: {vida_aliado2} de vida\nel aliado numero 3 tiene: {vida_aliado3} de vida")
            elif eleccion_combate_aliado == 3 and eleccion_combate_enemigo == 2:
                vida_aliado3 -= 10
                vida_enemigo2 -= 10
                print(f"el enemigo 1 tiene: {vida_enemigo1} de vida\nel enemigo 2 tiene: {vida_enemigo2} de vida\nel enemigo 3 tiene: {vida_enemigo3} de vida")
                print(f"el aliado 1 tiene: {vida_aliado1} de vida\nel aliado 2 tiene: {vida_aliado2} de vida\nel aliado numero 3 tiene: {vida_aliado3} de vida")
            elif eleccion_combate_aliado == 1 and eleccion_combate_enemigo == 3:
                vida_aliado1 -= 10
                vida_enemigo3 -= 10  
                print(f"el enemigo 1 tiene: {vida_enemigo1} de vida\nel enemigo 2 tiene: {vida_enemigo2} de vida\nel enemigo 3 tiene: {vida_enemigo3} de vida")
                print(f"el aliado 1 tiene: {vida_aliado1} de vida\nel aliado 2 tiene: {vida_aliado2} de vida\nel aliado numero 3 tiene: {vida_aliado3} de vida")
            elif eleccion_combate_aliado == 2 and eleccion_combate_enemigo == 3:
                vida_aliado2 -= 10
                vida_enemigo3 -= 10
                print(f"el enemigo 1 tiene: {vida_enemigo1} de vida\nel enemigo 2 tiene: {vida_enemigo2} de vida\nel enemigo 3 tiene: {vida_enemigo3} de vida")
                print(f"el aliado 1 tiene: {vida_aliado1} de vida\nel aliado 2 tiene: {vida_aliado2} de vida\nel aliado numero 3 tiene: {vida_aliado3} de vida")
            elif eleccion_combate_aliado == 3 and eleccion_combate_enemigo == 3:
                vida_aliado3 -= 10
                vida_enemigo3 -= 10
                print(f"el enemigo 1 tiene: {vida_enemigo1} de vida\nel enemigo 2 tiene: {vida_enemigo2} de vida\nel enemigo 3 tiene: {vida_enemigo3} de vida")
                print(f"el aliado 1 tiene: {vida_aliado1} de vida\nel aliado 2 tiene: {vida_aliado2} de vida\nel aliado numero 3 tiene: {vida_aliado3} de vida")
            if vida_enemigo1 <= 0 and vida_enemigo2 <= 0 and vida_enemigo3 <= 0:
                print("has ganado el combate")
                break
            elif vida_aliado1 <= 0 and vida_aliado2 <= 0 and vida_aliado3 <= 0:
                print("has perdido el combate")
                combate = False
            if eleccion_combate_aliado == 4 and eleccion_combate_enemigo == 4:
                print("bomba nuclear armada")
                vida_aliado1 -=99
                vida_aliado2 -=99
                vida_aliado3 -=99
                vida_enemigo1 -=99
                vida_enemigo2 -=99
                vida_enemigo3 -=99
                print(f"el enemigo 1 tiene: {vida_enemigo1} de vida\nel enemigo 2 tiene: {vida_enemigo2} de vida\nel enemigo 3 tiene: {vida_enemigo3} de vida")
                print(f"el aliado 1 tiene: {vida_aliado1} de vida\nel aliado 2 tiene: {vida_aliado2} de vida\nel aliado numero 3 tiene: {vida_aliado3} de vida")
    elif eleccion_menu_juego == "2":
        print("revision oponentes")
        print(f"vida del aliado 1 es: {vida_aliado1}pv\nvida del aliado 2 es: {vida_aliado2}pv\nvida del aliado 3 es: {vida_aliado3}pv")
        print(f"vida del enemigo 1 es: {vida_enemigo1}pv\nvida del enemigo 2 es: {vida_enemigo2}pv\nvida del enemigo 3 es: {vida_enemigo3}pv")
    elif eleccion_menu_juego == "3":
        print("salir")
        juego_iniciado = False
#cleado por Julian N, Benjamin C, Rogelio H.