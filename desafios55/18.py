movimiento = True
hora = 3
dueño_en_casa = True

hora_madrugada = 6

if (movimiento and not dueño_en_casa) or (movimiento and hora < hora_madrugada):
    print("Alarma Sonando")
else:
    print("Modo Silencioso")