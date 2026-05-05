movimiento = True
hora = 3
dueño_esta_en_la_casa = True
if movimiento == True and dueño_esta_en_la_casa == False or (movimiento == True and hora <
 6):
    print("Alarma sonando")
else:
    print("modo silencioso")