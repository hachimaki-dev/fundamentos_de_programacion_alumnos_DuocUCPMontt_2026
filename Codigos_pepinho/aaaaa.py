vida_usuario=100
vida_enemigo=100
turno=1

ataque_enemigo=20

while vida_usuario > 0 and vida_enemigo > 0:
    print("=================================")
    print(f"Estamos en el turno {turno}")
    print(f"Tu vida es de {vida_usuario}")
    print(f"La vida enemiga es de {vida_enemigo}")
    print("=================================")

    print("Elige tu siguiente movimiento!")
    print("1. Ataque de Tierra")
    print("2. Gruñido")
    print("3. Ataque de Agua")
    print("4. Ataque de Fuego")

    movimiento=int(input("¿Que eligues? "))
    print("=================================")

    if movimiento==1:
        vida_enemigo=vida_enemigo-20
        print("Tu ataque es eficaz")
        vida_usuario=vida_usuario-ataque_enemigo
        turno = turno + 1

    elif movimiento==2:
        print("=================================")
        ataque_enemigo=ataque_enemigo-5
        print("Usaste gruñido")
        print("El ataque del enemigo bajo")
        vida_usuario=vida_usuario-ataque_enemigo
        print("Enemigo te ataca")
        print("=================================")