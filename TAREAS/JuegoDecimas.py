import random
import time

zenis = 500 #Moneda del juego que se podra aumentar a medida que tengas combates
#Las variables inciales
Mochila_Personajes = [] 
personajes_nombres = [] 
personajes_Poder = []
personajes_rareza = []

guerreros_z = ["MrSatan", "Chaoz", "Nappa", "TrunksFuturo", "Goten", "Maestro Roshi"]
guerreros_comunez = ["Yamcha", "Puar", "Goku de Namek", "Krillin ", "TenshinHan"]
guerreros_raroz = ["Piccolo", "VegetaSSJ1", "GohanSSJ2"]
guerreros_miticoz = ["GokuUI", "VegetaUltraEgo", "GohanBeast", "GokuMUI"]

print("......................")
print(".....Bienvenido.......")
print(".........A............")
print(".....DragonBall.......")
print(".....DuocUCGame.......")
print("......................")
 
print("¡¡¡Tu objetivo es obtener recompensas a medida que avanzas!!!")

jugando = True
while jugando:
    print(f"\n....MENU PRINCIPAL....")  
    print("f\nZennis Actuales ${zenis}")
    print("1. Tirar Gacha (Cuesta 100 Zenis)")
    print("2. Ver la coleccion de personajes)")
    print("3. Combatir (Ganar zenis)")
    print("4. Salir del juego")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        if zenis >= 150:
            zenis -=150
            suerte = random.randint(1, 100)  

            nuevo_guerrero = {}

            if suerte <= 60:
                print(f"\n¡Aparece Shenlong! - Gacha Comun")
                nuevo_guerrero["nombre"] = random.choice(guerreros_comunez + guerreros_z)
                nuevo_guerrero["poder"] = random.randint(100, 1000)
                nuevo_guerrero["rareza"] = "comun"

            elif suerte<= 90:
                print(f"\nAparece Porunga - Gacha PocoComun")
                nuevo_guerrero["nombre"] = random.choice(guerreros_raroz)
                nuevo_guerrero["poder"] = random.randint(1400, 4600)
                nuevo_guerrero["rareza"] = "raro"

            else:
                print(f"\n[Aparece SuperShenlong] - Gacha Legendario")
                nuevo_guerrero["nombre"] = random.choice(guerreros_miticoz)
                nuevo_guerrero["poder"] = random.randint(14000, 46000)
                nuevo_guerrero["rareza"] = "MITICO"

            Mochila_Personajes.append(nuevo_guerrero)
            print(f"¡Has obtenido a {nuevo_guerrero['nombre']}!")
        else:
            ("\n¡No tienes suficientes Zenis")

    elif opcion == "2":
        print("---TU MOCHILA---")
        for personaje in range(len(Mochila_Personajes)):
            p = Mochila_Personajes [personaje]
            print(f"{personaje + 1}. {p["nombre"]}   / poder: {p["poder"]}  / Rareza: {p["rareza"]}")

    elif opcion == "3":
        if len(Mochila_Personajes) == 0:
            print("\n¡No tienes personajes para pelear!")
        else:
            print("\n--- SELECCIONA TU GUERRERO ---")
            for i in range(len(Mochila_Personajes)):
                p = Mochila_Personajes[i]
                print(f"{i + 1}. {p['nombre']} (Poder: {p['poder']})")
            
            selec = int(input("\nNúmero del guerrero: ")) - 1
            mi_pj = Mochila_Personajes[selec]
            suerte_rival = random.randint(1, 100)
            if suerte_rival <= 60:
                rival = {"nombre": random.choice(guerreros_comunez), "poder": random.randint(500, 1500), "rareza": "comun", "pago": 250}
            elif suerte_rival <= 90:
                rival = {"nombre": random.choice(guerreros_raroz), "poder": random.randint(2000, 6000), "rareza": "raro", "pago": 600}
            else:
                rival = {"nombre": random.choice(guerreros_miticoz), "poder": random.randint(15000, 45000), "rareza": "MITICO", "pago": 2500}

            print(f"\n¡Aparece {rival['nombre']}! Rareza: {rival['rareza']} | Poder: {rival['poder']}")

            print("\n¿Cómo quieres atacar?")
            print("1. Golpe Normal (x1.0 poder)")
            print("2. Cargar Ki (x1.5 poder)")
            print("3. ATAQUE ESPECIAL (x2.0 poder)")
            atk = input("Elige (1/2/3): ")

            poder_final = mi_pj["poder"]
            if atk == "2": poder_final *= 1.5
            elif atk == "3": poder_final *= 2.0

            print(f"\n¡{mi_pj['nombre']} ataca con un poder de {int(poder_final)}!")
            time.sleep(1)

            if poder_final >= rival["poder"]:
                ganancia = rival["pago"] + random.randint(50, 100)
                zenis += ganancia
                print(f"¡VICTORIA! Le ganaste a un {rival['rareza']}. Recompensa: ${ganancia}")
            else:
                print(f"DERROTA... {rival['nombre']} era muy fuerte.")

    elif opcion == "4":
        print("\nSaliendo del juego")
        jugando = False
    else: 
        print("Error")
