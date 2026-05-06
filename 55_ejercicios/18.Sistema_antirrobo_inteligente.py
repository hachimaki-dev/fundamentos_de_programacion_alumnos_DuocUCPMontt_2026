movimiento = True
hora = 3
dueño_en_casa = True
if movimiento == True and dueño_en_casa == False:
    print("Alarma Sonando")
elif movimiento == True and (hora >= 0 and hora < 6):
    print("Alarma Sonando")
else:
    print("Modo Silencioso")