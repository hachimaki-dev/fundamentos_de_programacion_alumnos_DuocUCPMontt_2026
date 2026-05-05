movimiento=True
hora=3 #3 am
dueño_en_casa=True

if (movimiento==True and dueño_en_casa==False) or (movimiento==True and hora<6):
    print("Alarma Sonando")

else:
    print("Modo Silencioso")
