#Ejercicio 18: Sistema Anti-Robo Inteligente (Smart Home)

movimiento = True
hora = 3
dueño_en_casa = True

if (movimiento and not dueño_en_casa) or (movimiento and hora < 6):
    print("Alarma sonando")
else:
    print("Modo silencio")