hubo_movimiento=True
hora=3
dueño_en_casa=True
if hubo_movimiento==True and dueño_en_casa==False:
    print("Alarma Sonando")
elif hubo_movimiento==True and hora<=6:
    print("Alarma Sonando")
else:
    print("Modo Silencioso")