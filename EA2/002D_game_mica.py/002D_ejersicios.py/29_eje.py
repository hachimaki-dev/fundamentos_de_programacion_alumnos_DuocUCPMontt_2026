quemar_kcal =300 
minitos = 0
calorias_quemadas = 0

while calorias_quemadas < quemar_kcal:
    minutos += 10
    if minutos <= 10:
        calorias_quemadas += 20
    else:
        calorias_quemadas += 10

print(minutos)
