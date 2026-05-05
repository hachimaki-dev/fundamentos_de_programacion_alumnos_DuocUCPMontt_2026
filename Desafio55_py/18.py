movimiento = True
hora = 3
dueño_en_casa = True


if movimiento == True and dueño_en_casa == False:
    print("ALARMA SONANDO !!!")
elif movimiento == True and hora < 6:
    print("ALARMA SONANDO !!!!")
else:
    print("MODO SILENCIOSO")
