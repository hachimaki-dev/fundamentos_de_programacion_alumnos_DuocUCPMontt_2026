movimiento = True
hora = 3
madrugada = 6
duenno_en_casa = True
alerta = "Alarma Sonando"
tranquilo = "Modo Silencioso"
if (movimiento == True and duenno_en_casa == False) or (movimiento == True and hora < madrugada):
    print(alerta)
else:
    print(tranquilo)