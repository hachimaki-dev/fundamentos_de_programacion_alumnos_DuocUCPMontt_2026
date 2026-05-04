vida_jefe1 = 1000
vida_jugador = 1000

rasen_shuriken = 100
chidogan = 200

import time


print("BIENVENIDO A LUMINARY")
print("")
time.sleep(1)
nombre_jugador = input("Para empezar ¿Como te llamas?")
print("")
time.sleep(1)
print(f"Perfecto. Bienvenido {nombre_jugador}")
print("")
time.sleep(2)
print("Para comenzar, te explicarè el juego")
time.sleep(3)
comprension_juego = input("Te encontraràs con 3 secciones. En cada secciòn hay 1 jefe, tendràs que derrotarlo para avanzar hacia la siguiente secciòn. Comienzas con 2 poderes, tendràs que seleccionar uno de estos para atacar, esto se hace con las letras (1) y (2). Màs adelante se te darà el menu de selecciòn y veràs que poderes posees. ¿Comprendido? 1).si 2).no")
while comprension_juego != "1":
    print("")
    comprension_juego = input("Te encontraràs con 3 secciones. En cada secciòn hay 1 jefe, tendràs que derrotarlo para avanzar hacia la siguiente secciòn. Comienzas con 2 poderes, tendràs que seleccionar uno de estos para atacar, esto se hace con las letras (1) y (2). Màs adelante se te darà el menu de selecciòn y veràs que poderes posees. ¿Comprendido? 1).si 2).no")
print("")

print("Despiertas a oscuras. No sabes donde te encuentras ni el por que. Miras a tu alrededor y de pronto aparece una luz que te ciega completamente.")
print("")
time.sleep(3)
print(f"???: Hola {nombre_jugador}. Te doy la bienvenida.")
print("")
time.sleep(3)
print(f"{nombre_jugador}: ...")
time.sleep(2)
print(f"{nombre_jugador}: ¿Còmo sabes mi nombre?.")
print("")
time.sleep(3)
print("???: Eso ahora mismo no importa. Te explicarè el juego.")
time.sleep(2)
print(f"???: Cuentas con {vida_jugador}HP. Tienes que derrotar al jefe de esta secciòn. El jefe tendra UNICAMENTE en esta seccion {vida_jefe1}HP, ya que, a medida que avances te encontraràs con enemigos mucho màs poderosos. Tus poderes son los siguientes:")
time.sleep(5)
print("Poderes:")
print("")
print(f"1).Chidogan {chidogan}Ptos de daño")
print("")
print(f"2).Rasen Shuriken {rasen_shuriken}Ptos de daño")
print("")
time.sleep(3)
print("*Has adquirido Chidogan y Rasen Shuriken*")
print("")
time.sleep(3)
print("???: Buena suerte... la necesitaràs.")
print("")
time.sleep(1)
print(f"{nombre_jugador}: ¡¡¡ESPERA!!!")
print("")
time.sleep(3)
print("Ves como lo que habia ahì desaparece por completo. A los extremos de las paredes comienzan a encenderse antorchas que iluminan toda la zona, desvelando poco a poco una bestia gigante de 4 metros, con una gran boca y colnillos afillados, tiene los ojos rojos, una piel muy pàlida y rugosa. La bestia te mira fijamente con una sonrisa inquietante.")
print("")
time.sleep(10)
print("Comienza La Batalla")
print("")
print(f"---Darkorus---HP:{vida_jefe1}---")
print("")
print(f"---{nombre_jugador}---HP:{vida_jugador}")
print("")
print("Habilidades: ")
print("")
print("1).rasen shuriken")
print("")
print("2).chidogan")
print("")

print("")
while vida_jefe1 > 0:
    ataque = input("Escoge una habilidad")
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

    else:
        print("Ataque nulo. Pierdes un turno")
        print("")
        time.sleep(1)
        print(f"HP:{vida_jefe1}")
        print("")
        time.sleep(1)
    

    if vida_jefe1 > 0:
        
         vida_jugador = vida_jugador - 100
         print("")
         time.sleep(1)
         print(f"Te han inflingido 100 Ptos de daño.")
         print("")
         time.sleep(1)
         print(f"---{nombre_jugador}---HP:{vida_jugador}")
         print("")
         time.sleep(1)
print("")
print("Un destello te ciega la vista")
print("")
time.sleep(1)
print(f"???: Veo que lograste pasar la primera etapa. Muy bien hecho {nombre_jugador}")
print("")
time.sleep(3)
print(f"{nombre_jugador}: Ya dime que es lo que pasa")
print("")
time.sleep(3)
print("???: Aun no es el momento... Ya lo sabras")
print("")
time.sleep(2)
print(f"{nombre_jugador}: ¿Entonces... ahora que es lo siguiente?")
time.sleep(3)

print("notas una neblina espesa y muy densa que te da mucho sueño y caes dormido")
time.sleep(2)


print("despiertas en el patio de un castillo es una zona muy abierta por alguna extraña razon hay una neblia que te llega hasta los tobillos ")
time.sleep(2)
print(f"???: hola {nombre_jugador} veo que ya despertaste")
time.sleep(2)
print(f"{nombre_jugador}: que haces aqui tu de nuevo me debes una explicacion")
time.sleep(2)
print("???: yo no te debo nada")
time.sleep(2)
print("???: procede a desaparecer entre la neblina del lugar")
time.sleep(3)
print("escuhas un ruido fuerte de tus alrededores vez en el cielo una sombra que vuela ,¿que podra ser?")
time.sleep(3)
print("vez caer en picada un dragon del cual se baja un caballero")
time.sleep(3)
print(f"{nombre_jugador} quien erese tu y que haces aqui")
time.sleep(3)
print("caballero: yo soy conocido como el rey sin nombre y vengo acabar con tu vida")
time.sleep(3)
print("vez salir de tus manos un aura de color azul")
time.sleep(3)
print("*****************************************************")
print("            !!haz subido de nivel¡¡"                  )
print("tu vida ahora es de 2000hp")
print("todos tus ataquen ganan un +100 de daño")
print("haz desbloqueado una nueva habilidad super genkidama")
print("*****************************************************")
rasen_shuriken = 200
chidogan = 300
super_genkidama = 400
vida_jugador = 2000
vida_jefe2 = 2000
print(" la vida del jefe es de 2000")
print(f" 1.rasen_shuriken {rasen_shuriken} de daño")
print(f"2.chidogan {chidogan} de daño")
print(f"3.super genkidama {super_genkidama} de daño")

while vida_jefe2 > 0:
    ataque = input("Escoge una habilidad")
    print("")
    if ataque == "1":
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
        print(f"HP:{vida_jefe2}")
        print("")
        time.sleep(1)
    

    if vida_jefe2 > 0:
        
         vida_jugador = vida_jugador - 200
         print("")
         time.sleep(1)
         print(f"Te han inflingido 200 Ptos de daño.")
         print("")
         time.sleep(1)
         print(f"---{nombre_jugador}---HP:{vida_jugador}")
         print("")
         time.sleep(1)

print(f"{nombre_jugador}:ya te e vencido rindete rey sin nombre")
time.sleep(1)
print("rey sin nombre: aca no acaba mi historia")
time.sleep(2)
print("el rey sin nombre empieza a golpear el suelo repetidas veces haciendo un temblor el suelo se abre en 2 y caes hacia abajo")
time.sleep(2)



