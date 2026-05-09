transferencias_dia = [15000, 80000, 2000, 150000]

maximo = []

for monto in transferencias_dia:
    if monto > 50000:

        maximo.append(monto)

print(maximo)