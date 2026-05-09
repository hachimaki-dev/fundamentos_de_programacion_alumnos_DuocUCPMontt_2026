
meta_kcal = 300
calorias_quemadas = 0
minutos = 0

while calorias_quemadas < meta_kcal:
    
    minutos += 1
      
    if minutos <= 10:
        calorias_quemadas += 20
    else:
        
        calorias_quemadas += 10

print(minutos)