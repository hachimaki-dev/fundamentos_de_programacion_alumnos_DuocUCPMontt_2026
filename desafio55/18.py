movimiento = True
hora = 3
dueño_en_casa = True
Alarma = False
if (movimiento == True or dueño_en_casa == False) and (movimiento == True or hora == 6):
    print("Alarma Sonando")
else:
    print("Modo silencioso")
    
