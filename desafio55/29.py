meta = 300
calorias = 0
minuto = 0

while calorias < meta:
    minuto += 1
    if minuto <= 10:
        calorias += 20
    
    else:
        calorias += 10

print("minutos totales", minuto)