movimiento = True
hora = 3
dueño_en_casa = True
if movimiento and dueño_en_casa == False or movimiento and hora <= 6:
    print("Alarma sonando")
else:
    print("Modo Silencio")