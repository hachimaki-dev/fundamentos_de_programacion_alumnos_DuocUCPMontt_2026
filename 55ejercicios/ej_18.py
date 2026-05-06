# Ejercicio 18: Sistema Anti-Robo Inteligente (Smart Home)

print("Sistema de alarma inteligente")

movimiento = True
hora = 3
dueno_en_casa = True

if (movimiento and dueno_en_casa == False) or (movimiento and hora < 6):
    print("Alarma Sonando")
else:
    print("Modo Silencioso")