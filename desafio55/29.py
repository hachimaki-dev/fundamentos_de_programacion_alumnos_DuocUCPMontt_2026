meta_calorias_quemadas = 300 # kcal
calorias_quemadas = 0
cronometro = 0

while calorias_quemadas < meta_calorias_quemadas:
    cronometro = cronometro + 1
   
    if cronometro <= 10:
        calorias_quemadas = calorias_quemadas + 20
    else:
        calorias_quemadas = calorias_quemadas + 10

print(cronometro)
