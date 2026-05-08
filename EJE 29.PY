minutos = 0
calorias = 0
meta = 300
 
while calorias < meta:
    if minutos < 10:
        calorias += 20
    else:
        calorias += 10
    minutos += 1
 
print(minutos)
print()
 
 