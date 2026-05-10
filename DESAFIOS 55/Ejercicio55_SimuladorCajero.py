montoretiro=37000
billetes=[20000, 10000, 5000, 1000]
resultados={}

for i in billetes:
    resultados[i]=montoretiro//i
    montoretiro=montoretiro%i
print(resultados)    