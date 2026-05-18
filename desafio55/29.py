meta_kcal = 300
kcal_quemadas = 0
contador_minutos = 0
while kcal_quemadas < meta_kcal:
    contador_minutos += 1
    if contador_minutos <= 10:
        kcal_quemadas += 20
    else:
        kcal_quemadas += 10
    
print(contador_minutos)
