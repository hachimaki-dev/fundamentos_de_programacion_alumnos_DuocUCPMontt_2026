vida_jefe1 = 1000
vida_jugador = 1000



rasen_shuriken = 100
chidogan = 200

import time
import random

escupir_acido = 100
garras = 200
mordedura = 300

dinero = 0

ataque1 = ["Escupir Ácido", 100]
ataque2 = ["Garras", 200]
ataque3 = ["Mordedura", 300]

opciones_jefe1 = [ataque1, ataque2, ataque3]

pocion_curativa_menor = 300
pocion_curativa_media = 500
pocion_curativa_meyor = 700


print("BIENVENIDO A LUMINARY")
print("")
time.sleep(1)

nombre_jugador = input("Para empezar ¿Como te llamas?")
print("")
time.sleep(1)
print(f"Perfecto. Bienvenido {nombre_jugador}")
print("")
time.sleep(2)
print("")
print("Comencemos el juego")
print("")
time.sleep(1)
print("Despiertas a oscuras. No sabes donde te encuentras ni el por que. Miras a tu alrededor y de pronto aparece una luz que te ciega completamente.")
print("")
time.sleep(3)
print(f"???: Hola {nombre_jugador}. Te doy la bienvenida.")
print("")
time.sleep(3)
print(f"{nombre_jugador}: ...")
time.sleep(2)
print("")
print(f"{nombre_jugador}: ¿Còmo sabes mi nombre?.")
print("")
time.sleep(3)
print("???: Eso ahora mismo no importa. Te explicarè como funcionan las cosas aquì.")
time.sleep(2)
print("")
print(f"???: Cuentas con {vida_jugador}HP. Tienes que derrotar al jefe de esta secciòn. El jefe tendra UNICAMENTE en esta seccion {vida_jefe1}HP, ya que, a medida que avances te encontraràs con enemigos mucho màs poderosos. Tambièn tu poder irà incrementando a medida que avances. Te otorgarè algunas habilidades para que comiences con tu aventura.")
time.sleep(5)
print("")
print("*Has adquirido Chidogan y Rasen Shuriken*")
print("")
time.sleep(3)
respuesta1 = int(input("1).Muchas gracias 2)...."))
if respuesta1 == 1:
    print("")
    print(f"{nombre_jugador}: Muchas gracias")
    print("")
    time.sleep(2)
    print("???: No hay de que.")
    print("")
    time.sleep(2)
elif respuesta1 == 2:
    print("")
    print(f"{nombre_jugador}: ...")
    time.sleep(2)
print("???: Ah... se me olvidaba algo.")
print("")
time.sleep(2)
print("*Has adquirido pociòn curativa (3)*")
print("")
time.sleep(2)
print("???: Buena suerte... la necesitaràs.")
print("")
time.sleep(2)
print(f"{nombre_jugador}: ¡¡¡ESPERA!!!")
print("")
time.sleep(3)
print("Ves como lo que habia ahì desaparece por completo. A los extremos de las paredes comienzan a encenderse antorchas que iluminan toda la zona, desvelando poco a poco una bestia gigante de 4 metros, con una gran boca y colnillos afillados, tiene los ojos rojos, una piel muy pàlida y rugosa. La bestia te mira fijamente con una sonrisa inquietante.")
print("")
time.sleep(10)
print("Comienza La Batalla")
time.sleep(2)
print("")
print(f"---Darkorus---HP:{vida_jefe1}---")
print("")
print(f"---{nombre_jugador}---HP:{vida_jugador}")
print("")


contador_curativa = 0

while vida_jefe1 > 0:
    print("Habilidades: ")
    print("")
    print(f"1).rasen shuriken - {rasen_shuriken}")
    print("")
    print(f"2).chidogan - {chidogan}")
    print("")
    print("3).Pociòn curativa - +300")
    print("")
    ataque = input("")
    print("")
    
    while ataque == "3" and contador_curativa >= 3:
        ataque = input("No te quedan pociones, escoja otra opciòn")
        print("")

    if ataque == "1":
        vida_jefe1 = vida_jefe1 - rasen_shuriken
        print(f"Has infligido {rasen_shuriken} Ptos de daño.")
        print("")
        time.sleep(1)
        print(f"---Darkorus---HP:{vida_jefe1}---")
        print("")
        time.sleep(1)

    elif ataque == "2":
        vida_jefe1 = vida_jefe1 - chidogan
        print(f"Has infligido {chidogan} Ptos de daño.")
        print("")
        time.sleep(1)
        print(f"---Darkorus---HP:{vida_jefe1}---")
        print("")
        time.sleep(1)
    
    elif ataque == "3" and contador_curativa < 3:
        vida_jugador = vida_jugador + pocion_curativa_menor
        print(f"Tu salud ha incrementado +300. Tu salud actual es de {vida_jugador}")
        contador_curativa = contador_curativa + 1
        print("")
    
    elif ataque != "1" and ataque != "2" and ataque != "3":
        print("Ataque nulo. Pierdes un turno")
        print("")
        time.sleep(1)
        print(f"HP:{vida_jefe1}")
        print("")
        time.sleep(1)


    if vida_jefe1 > 0:
        
        ataque_del_jefe = random.choice(opciones_jefe1)
        nombre_ataque_jefe1 = ataque_del_jefe[0]
        daño_ataque_jefe1 = ataque_del_jefe[1]
        vida_jugador = vida_jugador - daño_ataque_jefe1
        print(f"Darkous ha utilisado  {nombre_ataque_jefe1}. Te ha infligido {daño_ataque_jefe1}Ptos de daño")
        print("")
        time.sleep(1)
        print(f"---{nombre_jugador}---HP:{vida_jugador}")
        print("")
        time.sleep(1)

    while vida_jugador <= 0:
        print("Game Over")
        print("")
        continuar_1 = int(input("¿Continuar? 1).si 2).no"))
        if continuar_1 == 1:
            vida_jefe1 = 1000
            vida_jugador = 1000



        elif continuar_1 == 2:
            print("Saliste del juego")
            exit()

        while continuar_1 != 1 and continuar_1 != 2:
            continuar_1 = input("Ingrese una respuesta valida")


print("")
print("Un destello te ciega la vista")
print("")
time.sleep(2)
print(f"???: Veo que lograste pasar la primera etapa. Muy bien hecho {nombre_jugador}")
time.sleep(2)
print("")
print("???: Ten tu recompensa")
time.sleep(2)
print("")
print("*Has conseguido 300 Monedas de plata*")
dinero = 300
time.sleep(2)
print("")
print("???: Se me olvidò explicarte.")
time.sleep(2)
print("")
print("???: Cada vez que pases de secciòn te darè una recompansa. Podràs comprar pociones con estas monedas, nada mal ¿no?.")
print("")
time.sleep(2)
print(f"{nombre_jugador}: Ya dime que es lo que pasa")
print("")
time.sleep(2)
print("???: Aun no es el momento... Ya lo sabras")
print("")
time.sleep(2)
print(f"{nombre_jugador}: ¿Entonces... ahora que es lo siguiente?")
time.sleep(2)
print("")
print("???: Te quitarè tus pociones actuales.")
time.sleep(2)
contador_curativa = 3
print("")
print("???: Y lo siguiente serà tu primera compra en la tienda.")
time.sleep(2)
print("")
contador_curativa_menor = 0
contador_curativa_media = 0
contador_curativa_mayor = 0

pocion_curativa_menor_precio = 100
pocion_curativa_media_precio = 300
pocion_curativa_meyor_precio = 500
#TIENDA PARA POCIONES INICIO--------------------------------------------------------------
while True:
    print("")
    print("TIENDA DE ALQUIMIA")
    print("")
    print("1).Pociòn de vida - $100")
    print("")
    print("2).Pociòn de vida media - $300")
    print("")
    print("3).Pociòn de vida mayor - $500")
    print("")
    print("4).Salir")
    print("")
    eleccion_compra = input("¿Què deseas comprar?")
    print("")
    if eleccion_compra == "1" and dinero >= pocion_curativa_menor_precio:
        dinero = dinero - pocion_curativa_menor_precio
        contador_curativa_menor = contador_curativa_menor + 1
        print(f"Has comprado pociòn curativa menor\n\nINVENTARIO\n\nPocion curativa menor ({contador_curativa_menor})\n\nPocion curativa media ({contador_curativa_media})\n\nPocion curativa mayor ({contador_curativa_mayor})")
        seguir_tienda = input("¿Quieres seguir comprando? 1).si 2).no")
        if seguir_tienda == "1":
            print("")
        elif seguir_tienda == "2":
            break

    elif eleccion_compra == "2" and dinero >= pocion_curativa_media_precio:
        dinero = dinero - pocion_curativa_media_precio
        contador_curativa_media = contador_curativa_media + 1
        print(f"Has comprado pociòn curativa media\n\nINVENTARIO\n\nPocion curativa menor ({contador_curativa_menor})\n\nPocion curativa media ({contador_curativa_media})\n\nPocion curativa mayor ({contador_curativa_mayor})")
        seguir_tienda = input("¿Quieres seguir comprando? 1).si 2).no")
        if seguir_tienda == "1":
            print("")
        elif seguir_tienda == "2":
            break

    elif eleccion_compra == "3" and dinero >= pocion_curativa_meyor_precio:
        dinero = dinero - pocion_curativa_meyor_precio
        contador_curativa_mayor = contador_curativa_mayor + 1
        print(f"Has comprado pociòn curativa mayor\n\nINVENTARIO\n\nPocion curativa menor ({contador_curativa_menor})\n\nPocion curativa media ({contador_curativa_media})\n\nPocion curativa mayor ({contador_curativa_mayor})\n\n")
        seguir_tienda = input("¿Quieres seguir comprando? 1).si 2).no")
        if seguir_tienda == "1":
            print("")
        elif seguir_tienda == "2":
            break

    elif eleccion_compra == "4":
        print("???: Perfecto.")
        time.sleep(2)
        print("")
        print("???: Continuemos con tu aventura.")
        break

    else:
        print("No tienes suficiente dinero")
        print("")




#TIENDA PARA POCIONES FINAL-----------------------------------------------------------------------
time.sleep(2)
print("")
print("???: Necesito comentarte que a medida que avances en la aventura se iràn desbloqueando nuevas mecànicas.")
time.sleep(2)
print("")
print("???: En este caso has desbloqueado LA TIENDA, te permite comprar objetos como pociones y arm...")
time.sleep(2)
print("")
print(f"{nombre_jugador}: ...")
time.sleep(2)
print("")
print("???: ...")
time.sleep(2)
print("")
print("???: Uff... casi me adelanto.")
time.sleep(2)
print("")
print("???: En fin. Suerte.")
time.sleep(2)
print("")
print("*Ves como lentamente desaparece*")
time.sleep(2)
print("")
print(f"{nombre_jugador}: ¡¡¡ESPERAAAAAAAA!!!")











#SEGUNDA PARTE------------------------------------------------------------------------------

print("Notas una neblina espesa y muy densa que te da mucho sueño.")
time.sleep(2)
print("")
print("*Caes dormido*")
time.sleep(2)
print("")

print("Despiertas en el patio de un castillo, es una zona muy abierta por alguna extraña razon, hay una neblia que te llega hasta los tobillos. ")
time.sleep(2)
print("")
print(f"???: hola {nombre_jugador}, veo que ya despertaste.")
time.sleep(2)
print("")
print(f"{nombre_jugador}: ¿Què haces aqui tu de nuevo? me debes una explicacion.")
time.sleep(2)
print("")
print(f"{nombre_jugador}: Me debes una explicacion.")
time.sleep(2)
print("")
print("???: Yo no te debo nada.")
time.sleep(2)
print("")
print(" *Procede a desaparecer entre la neblina del lugar*")
time.sleep(3)
print("")
print("Escuhas un ruido muy fuerte de tus alrededores, ves en el cielo una sombra que vuela y no logras identificar que es.")
time.sleep(3)
print("")
print("Ves caer en picada un dragon del cual se baja un caballero.")
time.sleep(3)
print("")
print(f"{nombre_jugador}: quien eres tu y que haces aqui.")
time.sleep(3)
print("")
print("Caballero: yo soy conocido como el rey sin nombre y vengo acabar con tu vida.")
time.sleep(3)
print("")
print("ves salir de tus manos un aura de color azul.")
time.sleep(3)
print("")
print("*****************************************************")
print("            !!haz subido de nivel¡¡"                  )
print("tu vida ahora es de 2000hp")
print("todos tus ataquen ganan un +100 de daño")
print("haz desbloqueado una nueva habilidad super genkidama")
print("*****************************************************")
time.sleep(3)
print("")

rasen_shuriken = 200
chidogan = 300
super_genkidama = 400
vida_jugador = 2000
vida_jefe2 = 2000

apuñalar = 200
filo_del_cazador = 500
puñal_deslumbrante = 300
puño_de_acero = 100

ataque21 = ["puño_de_acero", 100]
ataque22 = ["apuñalar", 200]
ataque23 = ["puñal_deslumbrante", 300]
ataque24 = ["filo_del_cazador", 500]

opciones_jefe2 = [ataque21, ataque22, ataque23, ataque24]



print(" la vida del jefe es de 2000")
time.sleep(3)
print("")
print("Comienza el combate")
time.sleep(3)
print("")

while vida_jefe2 > 0:
    print("")
    print(f"1).rasen_shuriken - {rasen_shuriken} de daño")
    print("")
    print(f"2).chidogan - {chidogan} de daño")
    print("")
    print(f"3).super genkidama - {super_genkidama} de daño")
    print("")
    print(f"4).Usar pociòn curativa")
    
    ataque = input("Escoge una habilidad")
    
    if ataque == "4":
        while True:

            print("Pociones:")
            print("")
            print(f"1).Pocion curativa ({contador_curativa_menor})")
            print("")
            print(f"2).Pocion curativa media ({contador_curativa_media})")
            print("")
            print(f"3).Pocion curativa mayor ({contador_curativa_mayor})")
            print("")
            print("4).Salir")
            eleccion_pociones = input("")

            while eleccion_pociones != "1" and eleccion_pociones != "2" and eleccion_pociones != "3" and eleccion_pociones != "4":
                eleccion_pociones = input("No vàlido")
                print("")
        
            if eleccion_pociones == "1" and contador_curativa_menor > 0:
                vida_jugador = vida_jugador + pocion_curativa_menor
                contador_curativa_menor = contador_curativa_menor - 1
                print(f"Recuperaste {pocion_curativa_menor} de salud")
                print("")
        
            elif eleccion_pociones == "2" and contador_curativa_media > 0:
                vida_jugador = vida_jugador + pocion_curativa_media
                contador_curativa_media = contador_curativa_media - 1
                print(f"Recuperaste {pocion_curativa_media} de salud")
                print("")
        
            elif eleccion_pociones == "3" and contador_curativa_mayor > 0:
                vida_jugador = vida_jugador + pocion_curativa_meyor
                contador_curativa_mayor = contador_curativa_mayor - 1
                print(f"Recuperaste {pocion_curativa_meyor} de salud")
                print("")

            elif eleccion_pociones == "4":
                print("")
                ataque = input("Escoge una habilidad")
                break
            

    elif ataque == "1":
        vida_jefe2 = vida_jefe2 - rasen_shuriken
        print(f"Has infligido {rasen_shuriken} Ptos de daño.")
        print("")
        time.sleep(1)
        print(f"---Rey sin nombre---HP:{vida_jefe2}---")
        print("")
        time.sleep(1)

    elif ataque == "2":
        vida_jefe2 = vida_jefe2 - chidogan
        print(f"Has infligido {chidogan} Ptos de daño.")
        print("")
        time.sleep(1)
        print(f"---Rey sin nombre---HP:{vida_jefe2}---")
        print("")
        time.sleep(1)

    
    elif ataque == "3":
        vida_jefe2 = vida_jefe2 - chidogan
        print(f"Has infligido {super_genkidama} Ptos de daño.")
        print("")
        time.sleep(1)
        print(f"---Rey sin nombre---HP:{vida_jefe2}---")
        print("")
        time.sleep(1)


        

    
    
    
    else:
        print("Ataque nulo. Pierdes un turno")
        print("")
        time.sleep(1)
        print(f"---Rey sin nombre---HP:{vida_jefe2}")
        print("")
        time.sleep(1)
    
    if vida_jefe2 > 0:
        ataque_del_jefe2 = random.choice(opciones_jefe2)
        nombre_ataque_jefe2 = ataque_del_jefe2[0]
        daño_ataque_jefe2 = ataque_del_jefe[1]
        vida_jugador = vida_jugador - daño_ataque_jefe2
        print(f"Darkous ha utilisado  {nombre_ataque_jefe2}. Te ha infligido {daño_ataque_jefe2}Ptos de daño")
        print("")
        time.sleep(1)
        print(f"---{nombre_jugador}---HP:{vida_jugador}")
        print("")
        time.sleep(1)

print(f"{nombre_jugador}: Ya te he vencido rindete rey sin nombre.")
time.sleep(2)
print("")
print("rey sin nombre: Aqui no acaba mi historia.")
time.sleep(2)
print("")
print("El rey sin nombre empieza a golpear el suelo repetidas veces haciendo un temblor el suelo, se abre en 2 y caes hacia abajo.")
time.sleep(2)
print("")
print("*Quedas inconsciente por el golpe al caer*")
time.sleep(2)
print("")
print("???: ¿Hola...?.")
time.sleep(2)
print("")
print("*Te picotea con un palo*")
time.sleep(2)
print("")
print("???: Oh... estas vivo. ")
time.sleep(2)
print("")
print(f"{nombre_jugador}: ¿Q... Què pasò...?")
time.sleep(2)
print("")
print("???: Nada, solo caiste desde allà arriba.")
time.sleep(2)
print("")
print(f"{nombre_jugador}: Ya veo...¿y ahora que tengo que hacer?.")
time.sleep(2)
print("")
print(f"{nombre_jugador}: Yo tan solo quiero que todo esto pase.")
time.sleep(2)
print("")
print("???: Tranqui, solo ya te queda poco.")
time.sleep(2)
print("")
print("???: Mientras te recuperas podrìas comprar algunas pociones.")
time.sleep(2)
print("")
print("???: Ten, te darè un par de monedas")
dinero = dinero + 600
time.sleep(2)
print("")
print(f"*Ahora tienes {dinero} monedas de plata*")
time.sleep(2)
print("")

contador_espada_infernus = 0

espada_infernus_precio = 600

while True:
    print("")
    print("TIENDA DE ALQUIMIA")
    print("")
    print("1).Pociòn de vida - $100")
    print("")
    print("2).Pociòn de vida media - $300")
    print("")
    print("3).Pociòn de vida mayor - $500")
    print("")
    print("4).Espada infernus - $600")
    print("")
    print("5).Salir")
    print("")
    eleccion_compra = input("¿Què deseas comprar?")
    print("")
    if eleccion_compra == "1" and dinero >= pocion_curativa_menor_precio:
        dinero = dinero - pocion_curativa_menor_precio
        contador_curativa_menor = contador_curativa_menor + 1
        print(f"Has comprado pociòn curativa menor\n\nINVENTARIO\n\nPocion curativa menor ({contador_curativa_menor})\n\nPocion curativa media ({contador_curativa_media})\n\nPocion curativa mayor ({contador_curativa_mayor})")
        seguir_tienda = input("¿Quieres seguir comprando? 1).si 2).no")
        if seguir_tienda == "1":
            print("")
        elif seguir_tienda == "2":
            break

    elif eleccion_compra == "2" and dinero >= pocion_curativa_media_precio:
        dinero = dinero - pocion_curativa_media_precio
        contador_curativa_media = contador_curativa_media + 1
        print(f"Has comprado pociòn curativa media\n\nINVENTARIO\n\nPocion curativa menor ({contador_curativa_menor})\n\nPocion curativa media ({contador_curativa_media})\n\nPocion curativa mayor ({contador_curativa_mayor})")
        seguir_tienda = input("¿Quieres seguir comprando? 1).si 2).no")
        if seguir_tienda == "1":
            print("")
        elif seguir_tienda == "2":
            break

    elif eleccion_compra == "3" and dinero >= pocion_curativa_meyor_precio:
        dinero = dinero - pocion_curativa_meyor_precio
        contador_curativa_mayor = contador_curativa_mayor + 1
        print(f"Has comprado pociòn curativa mayor\n\nINVENTARIO\n\nPocion curativa menor ({contador_curativa_menor})\n\nPocion curativa media ({contador_curativa_media})\n\nPocion curativa mayor ({contador_curativa_mayor})\n\n")
        seguir_tienda = input("¿Quieres seguir comprando? 1).si 2).no")
        if seguir_tienda == "1":
            print("")
        elif seguir_tienda == "2":
            break

    elif eleccion_compra == "5":
        print("???: Perfecto.")
        time.sleep(2)
        print("")
        print("???: Continuemos con tu aventura.")
        break

    elif eleccion_compra == "4" and dinero >= espada_infernus_precio and contador_espada_infernus == 0:
        contador_espada_infernus = contador_espada_infernus + 1
        print("")
        print("*Has adquirido Espada infernus*")
        time.sleep(2)
        print("")

    elif eleccion_compra == "4" and dinero >= espada_infernus_precio and contador_espada_infernus > 0:
        print("")
        print("No puedes volver a comprarla")
        time.sleep(2)
        print("")


    

    else:
        print("No tienes suficiente dinero.")
        print("")

print("")
print("*Haz pasado a la tercera pelea*")
time.sleep(2)
print("")
print("??? :Ha sido un camino largo, haz estado cerca de morir varias veces, pero haz logrado sobrevivir")
time.sleep(2)
print("")
print("???: Te felicito")
time.sleep(2)
print("")
print("Te encuentras frente a un nuevo enemigo, su nombre es Shepyroth")
time.sleep(2)
print("")
print("*Sientes que esta pelea serà la mas difìcil de todas*")
time.sleep(2)
print("")
print("Tu vida se ha restablecido, es momento de pelear")
time.sleep(2)
print("")



vida_jugador = 1000
vida_jefe3 = 10000
rasen_shuriken = 1000
chidogan = 1000
super_genkidama = 2000
espada_infernus = 2500
contador_super_genkidama = 0




ataque31 = ["Golpe nuclear", 400]
ataque32 = ["Aliento divino", 600]
ataque33 = ["Fuego negro", 800]


opciones_jefe3 = [ataque31, ataque32, ataque33]




print("¡el jefe se dirige rapido hacia ti, debes elegir un ataque!")
time.sleep(2)
print("")





while vida_jefe3 > 0:
    
    time.sleep(1)
    print(f"---{nombre_jugador}---HP:{vida_jugador}")
    print("")
    time.sleep(1)

    while vida_jugador <= 0:
        print("shepyroth te ha derrotado")
        print("game over")

        continuar_3 =int(input("¿deseas continuar? 1) si , 2) no"))
        if continuar_3 == 1:
            vida_jefe3 = 10000
            vida_jugador = 1000
        elif continuar_3 == 2:
            print(" juego finalizado ")
            exit()
    print("")
    print("Habilidades: ")
    print("")
    print("1).Rasen shuriken")
    print("")
    print("2).Chidogan")
    print("")
    print("3).Super genkidama")
    print("")
    print("4).Pociones")

    if contador_espada_infernus > 0:
        print("5).Espada infernus")
    print("")        
    ataque_jugador = int(input("Escoge un ataque"))
    print("")


    if ataque_jugador == 1:
        vida_jefe3 -= rasen_shuriken
        print("¡usaste rasen shuriken!")
        time.sleep(2)
        print("")
        print(f"Has infligido {rasen_shuriken} Ptos de daño.")
        print("")
        time.sleep(1)
        print(f"---Darkorus---HP:{vida_jefe3}---")
        print("")
        time.sleep(1)
        if vida_jefe3 <= 0:
            break

    elif ataque_jugador == 2:
        vida_jefe3 -= chidogan
        print("¡usaste chidogan!")
        time.sleep(2)
        print("")
        print(f"Has infligido {chidogan} Ptos de daño.")
        print("")
        time.sleep(1)
        print(f"---Darkorus---HP:{vida_jefe3}---")
        print("")
        time.sleep(1)
        if vida_jefe3 <= 0:
            break
    
    elif ataque_jugador == 3:
        vida_jefe3 -= super_genkidama
        print("usaste super genkidama")
        time.sleep(2)
        print("")
        contador_super_genkidama += 1
        if contador_super_genkidama >= 2:
            super_genkidama = 0    
        print(f"Has infligido {super_genkidama} Ptos de daño.")
        print("")
        time.sleep(1)
        print(f"---Darkorus---HP:{vida_jefe3}---")
        print("")
        time.sleep(1)
        if vida_jefe3 <= 0:
            break

    elif ataque_jugador == 4:
        while True:

            print("Pociones:")
            print("")
            print(f"1).Pocion curativa ({contador_curativa_menor})")
            print("")
            print(f"2).Pocion curativa media ({contador_curativa_media})")
            print("")
            print(f"3).Pocion curativa mayor ({contador_curativa_mayor})")
            print("")
            print("4).Salir")
            eleccion_pociones = input("")

            while eleccion_pociones != "1" and eleccion_pociones != "2" and eleccion_pociones != "3" and eleccion_pociones != "4":
                eleccion_pociones = input("No vàlido")
                print("")
        
            if eleccion_pociones == "1" and contador_curativa_menor > 0:
                vida_jugador = vida_jugador + pocion_curativa_menor
                contador_curativa_menor = contador_curativa_menor - 1
                print(f"Recuperaste {pocion_curativa_menor} de salud")
                print("")
        
            elif eleccion_pociones == "2" and contador_curativa_media > 0:
                vida_jugador = vida_jugador + pocion_curativa_media
                contador_curativa_media = contador_curativa_media - 1
                print(f"Recuperaste {pocion_curativa_media} de salud")
                print("")
        
            elif eleccion_pociones == "3" and contador_curativa_mayor > 0:
                vida_jugador = vida_jugador + pocion_curativa_meyor
                contador_curativa_mayor = contador_curativa_mayor - 1
                print(f"Recuperaste {pocion_curativa_meyor} de salud")
                print("")

            elif eleccion_pociones == "4":
                print("")
                ataque = input("Escoge una habilidad")
                break

    
    elif ataque_jugador == 5 and contador_espada_infernus > 0:
        vida_jefe3 -= espada_infernus
        print("¡usaste espada infernus!")
        time.sleep(2)
        print("")
        print("¡recuerda que solo puedes usar este ataque una vez!")
        time.sleep(2)
        print("")
        contador_espada_infernus = contador_espada_infernus - 1
        print(f"Has infligido {espada_infernus} Ptos de daño.")
        print("")
        time.sleep(1)
        print(f"---Darkorus---HP:{vida_jefe3}---")
        print("")
        time.sleep(1)
        if vida_jefe3 <= 0:
            break
    
    else:
        print("ataque invalido")
    
    ataque_del_jefe = random.choice(opciones_jefe3)
    nombre_ataque_jefe3 = ataque_del_jefe[0]
    daño_ataque_jefe3 = ataque_del_jefe[1]
    vida_jugador = vida_jugador - daño_ataque_jefe3
    print(f"Darkous ha utilisado  {nombre_ataque_jefe3}. Te ha infligido {daño_ataque_jefe3}Ptos de daño")
    print("")


time.sleep(2)
print("")
print("???: Wow...")
time.sleep(2)
print("")
print("???: No pensè que lo lograrias.")
time.sleep(2)
print("")
print("???: Creo que ahora si te mereces saber quien soy...")
time.sleep(2)
print("")
print("Dr.Robert: Soy Robert Bloodbane, trabajo para una compañìa llamada Vitality Company, se dedica a la experimentaciòn con realidad virtual")
time.sleep(2)
print("")
print(f"{nombre_jugador}: ...")
time.sleep(2)
print("")
print(f"{nombre_jugador}: ¿Y eso que tiene que ver conmigo?")
time.sleep(2)
print("")
print("Dr.Robert: Tus padres tomaron esta decisiòn por ti.")
time.sleep(2)
print("")
print(f"{nombre_jugador}: ¿A que te refieres con eso...?")
time.sleep(2)
print("")
print("Dr.Robert: Es preferible que ellos mismos te cuenten.")
time.sleep(2)
print("")
print("*Se oscurece todo*")
time.sleep(2)
print("")
print("Despues de un segundo no logras ver nada.")
time.sleep(2)
print("")
print("Logras ver una luz blanca, es muy pequeña y va creciendo de manera exponencial")
time.sleep(3)
print("")
print("Ciega completamente tu visiòn")
time.sleep(2)
print("")
print("Escuchas unas voces")
time.sleep(2)
print("")
print("Abres los ojos")
time.sleep(2)
print("")
print("Ves tu entorno")
time.sleep(2)
print("")
print("Te encuentras en una camilla, conectado a una maquina la cual no comprendes su funciòn")
time.sleep(2)
print("")
print("Ves a dos personas")
time.sleep(2)
print("")
print("Papà: ¿Y que tal te fue?")
time.sleep(2)
print("")
print(f"{nombre_jugador}: ...")
time.sleep(2)
print("")
print(f"{nombre_jugador}: ¿Y... quien eres tu? ")
time.sleep(2)
print("")



continuara = """
###########################################################################################
#                                                                                         #
#     _____  ____  _   _  _______ _____ _   _ _    _          _____        _              #
#    / ____|/ __ \| \ | ||__   __|_   _| \ | | |  | |   /\   |  __ \      / \             #
#   | |    | |  | |  \| |   | |    | | |  \| | |  | |  /  \  | |__) |    / ^ \            #
#   | |    | |  | | . ` |   | |    | | | . ` | |  | | / /\ \ |  _  /    / /_\ \           #
#   | |____| |__| | |\  |   | |   _| |_| |\  | |__| |/ ____ \| | \ \   /  ___  \          #
#    \_____|\____/|_| \_|   |_|  |_____|_| \_|\____//_/    \_\_|  \_\ /__/   \__\         #
#                                                                                         #
#                                                                                         #
###########################################################################################
"""

print(continuara)



      













    





































print("Juego terminado")


    

