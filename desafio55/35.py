transferencias_del_día = [15000, 80000, 2000, 150000]
transferencia_importante = []
contadoreishon = 0
for i in transferencias_del_día:
    if i > 50000:
        transferencia_importante.append(transferencias_del_día[contadoreishon])
    contadoreishon += 1
print(transferencia_importante)