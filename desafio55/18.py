movimiento = True

hora = 3

dueño_en_casa = True

if movimiento == True or dueño_en_casa == False:
    print("Alarma Sonando")

elif movimiento == True and hora > 6 and dueño_en_casa == False or dueño_en_casa == True:
    print("Alarma Sonando")

