movimiento = True
dueño_en_casa = True
hora = 3
if (movimiento and not dueño_en_casa) or (movimiento and hora < 6):
    print("alarma sonando")
else:
    print("alarma silenciosa")