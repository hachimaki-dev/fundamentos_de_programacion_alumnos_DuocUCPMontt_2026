vida_jefe1 = 1000
vida_jugador = 1000

rasen_shuriken = 50
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
    print("1).rasen shuriken - 50")
    print("")
    print("2).chidogan - 200")
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
print("*Has conseguido 200 Monedas de plata*")
dinero = 200
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
print("???: Y lo siguiente serà tu primera compra en la tienda de alquimia.")
time.sleep(2)
print("")
contador_curativa_menor = 0
contador_curativa_media = 0
contador_curativa_mayor = 0

pocion_curativa_menor_precio = 100
pocion_curativa_media_precio = 300
pocion_curativa_meyor_precio = 500

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











print("Juego terminado")


    

