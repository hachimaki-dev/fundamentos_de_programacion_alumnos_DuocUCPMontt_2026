minutos = 0
calorias = 0

while True:
    minutos += 1
    
    if minutos <= 10:
        calorias += 20
    elif minutos >= 11:
        calorias += 10

    if calorias >= 300:
        print(f"META LOGRADA EN {minutos} MINUTOS") 
        break