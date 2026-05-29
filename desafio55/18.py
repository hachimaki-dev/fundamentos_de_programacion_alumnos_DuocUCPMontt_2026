movimiento = True
hora= 3 #De la madrugada
dueño_de_casa = True
if (movimiento == True and dueño_de_casa == False) or (movimiento == True and hora < 6):
    print("ALARMA SONANDO")
else:
    print("modo: s i l e n c i o")