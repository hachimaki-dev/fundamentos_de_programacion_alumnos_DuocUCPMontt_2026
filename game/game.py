print("Bienvenido a Super Smash Bros.")
print("1. Mario")
print("2. Donkey Kong")
print("3. Link")
print("4. Samus")
print("5. Yoshi")
print("6. Kirby")
print("7. Fox")
print("8. Pikachu")

dolor_jugador = 0
vidas_jefe = 100

while True:
    seleccion = input("Seleccione tu personaje: ")
    if seleccion == "Mario":
        print(f"{seleccion} tiene {dolor_jugador}% de daño")
        print(f"Debes enfrentarte a Master Hand, que tiene {vidas_jefe} vidas")
        print("Utiliza tus ataques para vencerlo, si llega a 0 ganas")
        print("Si te ataca te da más daño, si llega a 300% mueres y termina la partida")
        
        ataques_mario = ["Golpe salto", "Bola de fuego", "Patada", "Super capa"]
        print(f"{seleccion} puede usar {ataques_mario}")
        
        for a in ataques_mario:
            ataque_seleccionado = input("Seleccione el ataque: ")
            if ataque_seleccionado == "Golpe salto":
                vidas_jefe = vidas_jefe - 20
                print(f"{seleccion} usó {ataque_seleccionado}")
                print(f"Master Hand tiene {vidas_jefe} de 100")
            elif ataque_seleccionado == "Bola de fuego":
                vidas_jefe = vidas_jefe - 10
                print(f"{seleccion} usó {ataque_seleccionado}")
                print(f"Master Hand tiene {vidas_jefe} de 100")
            elif ataque_seleccionado == "Patada":
                vidas_jefe = vidas_jefe - 15
                print(f"{seleccion} usó {ataque_seleccionado}")
                print(f"Master Hand tiene {vidas_jefe} de 100")
            elif ataque_seleccionado == "Super capa":
                vidas_jefe = vidas_jefe - 5
                print(f"{seleccion} usó {ataque_seleccionado}")
                print(f"Master Hand tiene {vidas_jefe} de 100")
            else:
                print("No está en la lista")
    else:
        print("Seleccione los que están presentes")