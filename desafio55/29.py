inicio_calorias = 0
meta_calorias = 300
minuto = 0
while inicio_calorias != meta_calorias:
    minuto += 1
    if minuto <= 10:
        inicio_calorias += 20
    else:
        inicio_calorias += 10
print(f"Demoraste {minuto} minutos en quemar 300 calorias.")