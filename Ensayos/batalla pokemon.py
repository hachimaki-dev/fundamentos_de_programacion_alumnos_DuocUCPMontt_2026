vida_ratata=50
vida_charizard=50
puntos_de_accion=5

print("¡la batalla!")

while vida_ratata>0 and vida_charizard>0:
    print(f"vida de ratata:{vida_ratata},pokemones:{puntos_de_accion}")
    print(f"vida de charizard:{vida_charizard}")
    
    print("elije una accion:")
    print("1.arañazo")
    print("2.gruñido")
    print("3.placaje")

    accion=int(input("ratata ataca"))
    if accion ==1 :
        vida_charizard=vida_charizard-15
        print(f"!ratata a ataco a charizard¡,vida de charizard:{vida_charizard}")
    elif accion==2:
        if puntos_de_accion>=5:
            puntos_de_accion=puntos_de_accion-1
            vida_charizard=vida_charizard-15
            print(f"!ratata a utilizado gruñido ha bajado ataque de charizard:,puntos de accion:{puntos_de_accion}")

        else:  
            print("charizard a esquivado el ataque de ratata , turno de charizard")
    elif accion==3:
        vida_ratata=vida_ratata(50)
        puntos_de_accion=3
        print(f"ratata ha utilizado placaje contra charizard , vida de charizard:{vida_charizard} , puntos de accion{puntos_de_accion}")
    else:
        print("charizard a recibido el ataque de ratata y le ha hecho un critico")

