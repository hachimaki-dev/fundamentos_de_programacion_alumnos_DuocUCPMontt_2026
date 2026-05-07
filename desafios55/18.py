movimiento = True
hora = 3
dueño_en_casa = True

if movimiento == True or dueño_en_casa == True :
    print("Modo silencioso")

elif movimiento == True or hora < 6 :
    print("Alarma Sonando")