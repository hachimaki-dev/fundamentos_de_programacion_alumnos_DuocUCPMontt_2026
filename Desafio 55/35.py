transferencias = [15000, 80000, 2000, 150000]
transferencias_importantes = []

for transferencia in transferencias :
    if transferencia > 50000 :
        transferencias_importantes.append(transferencia)

print(transferencias_importantes)