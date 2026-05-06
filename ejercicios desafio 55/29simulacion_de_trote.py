minutos_trotando = 0
calorias_quemadas = 0
while calorias_quemadas < 300:
    minutos_trotando = minutos_trotando + 1
    if minutos_trotando <= 10:
        calorias_quemadas = calorias_quemadas + 20
    else:
        calorias_quemadas = calorias_quemadas + 10
print(minutos_trotando)