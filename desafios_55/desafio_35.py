transferencias_del_dia = [15000, 80000, 2000, 150000]
importantes = []

for monto in transferencias_del_dia:
    if monto > 50000 :
        importantes.append(monto)

print(importantes)
    