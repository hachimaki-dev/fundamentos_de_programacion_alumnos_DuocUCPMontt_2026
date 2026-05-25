meta_quemar_calorias = 300
minuto = 0
calorias_quemadas = 0
while meta_quemar_calorias >= calorias_quemadas:
    if minuto <= 10:
        calorias_quemadas += 20
        minuto += 1
    else:
        calorias_quemadas += 10
        minuto += 1
print(minuto)