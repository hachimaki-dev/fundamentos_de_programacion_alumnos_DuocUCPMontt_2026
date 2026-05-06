movimiento = True
hora = 3
duenio_en_casa = True

if (movimiento and not duenio_en_casa) or (movimiento and hora < 6) :
    print("Alarma Sonando")
else :
    print("Modo Silencioso")