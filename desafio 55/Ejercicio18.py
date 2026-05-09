movimiento = True
dueño_en_casa = True
hora = 3

if (movimiento == True and dueño_en_casa == False) or (movimiento == True and hora < 6):
    print("Alarma Sonando")
else:
    print("Alarma en silencio")