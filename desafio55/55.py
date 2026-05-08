dinero = 37000
billete = [20000, 10000, 5000 , 1000]
resultados = {}
for plata in billete:
    billetes = dinero // plata
    resultados[plata] = billetes
    dinero = dinero % plata
print(resultados)
