movimiento = True
hora = 3
dueno_en_casa = True


if (movimiento and not dueno_en_casa) or (movimiento and hora < 6):
    print("alarma sonando")

else:
    print("modo silencioso")
    