ventas = [1500 , -200  , 5000 , 0 ,100]

suma_total = 0
for v in ventas:

    if v <= 0:
        continue

    suma_total += v



print(suma_total)