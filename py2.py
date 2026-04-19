jugador = 100
mana = 20
jefefinal= 150
turno = 0
print("--juego rpg--)")
print("1 . atacar")
print("2. magia")
print("3. vida")
while jugador >= 0 or jefefinal >= 0 :
    opcion = int(input("Ingrese opcion :"))
    if opcion == 1 :
        print("Haz atacado al jefe")
        jefefinal = jefefinal - 20
        print(f"la vida del jefe final ahora es {jefefinal}")
        turno = turno + 1
        print("tu turno actual es {turno}")
    if opcion == 2 :
        print("haz lazado magia")
        jefefinal = jefefinal - 50
        mana= mana-5
        print(f"tu mana restante es {mana}")
    if jefefinal > 50 :
        print("turno del jefe final")
        jugador = jugador - 40
        print(f"tu vida actual es de {jugador}")
    if jugador >= 0 :
        print("Haz perdido")
        continue