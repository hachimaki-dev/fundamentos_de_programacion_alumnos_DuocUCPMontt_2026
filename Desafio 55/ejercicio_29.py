# Simulación de Trote (Apple Watch)
# Calcula cuánto rato te tomará quemar tus calorías del día trotando.

meta_De_calorias = 300
calorias_quemadas = 0
minutos = 0

while calorias_quemadas < meta_De_calorias:
    minutos += 1    

    if minutos <= 10:
        calorias_quemadas += 20
    else:
        calorias_quemadas += 10

print(minutos)        

