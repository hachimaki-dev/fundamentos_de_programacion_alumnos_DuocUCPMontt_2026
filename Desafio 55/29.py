minutos_trotando = 0

meta_kcal_quemadas = 300
kcal_actuales_quemadas = 0

while minutos_trotando < 10 :
    kcal_actuales_quemadas += 20
    minutos_trotando += 1

while kcal_actuales_quemadas < meta_kcal_quemadas :
    kcal_actuales_quemadas += 10
    minutos_trotando += 1

print(minutos_trotando)