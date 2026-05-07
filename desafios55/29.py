calorias = 0
minutos = 0

while calorias < 300 :

    if minutos < 10 : 
        calorias = calorias + 20
        minutos = minutos + 1

    else :
        calorias = calorias + 10
        minutos = minutos + 1


print(minutos)