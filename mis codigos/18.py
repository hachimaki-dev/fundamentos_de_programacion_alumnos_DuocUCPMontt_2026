Movimiento = True

dueño_casa = True

hora = 3

if Movimiento == True and dueño_casa == False or Movimiento == True and hora < 6:

    print("¡Alarma Sonando!")
else:
    print("Modo silencioso")