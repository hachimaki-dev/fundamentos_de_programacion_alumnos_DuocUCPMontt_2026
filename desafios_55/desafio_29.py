meta_calorias_quemadas = 300
calorias_quemadas = 0
minuto = 0

while calorias_quemadas <= meta_calorias_quemadas:
    if minuto >= 11:
        calorias_quemadas += 10
        minuto += 1
    else:
        minuto += 1
        calorias_quemadas += 20

print(f"el tiempo que tardaste en quemar 300kcal fueron: {minuto} minutos")