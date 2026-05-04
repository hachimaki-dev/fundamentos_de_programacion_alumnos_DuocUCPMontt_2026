movimiento=True
hora=3
dueno_presente=True
if (movimiento == True and dueno_presente==False) or (movimiento==True and hora < 6):
    print("Alarma sonando")
else:
    print("Modo silencioso")