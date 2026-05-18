transferencias_dia = [15000, 80000, 2000, 150000]
importantes = []
for transferencia in transferencias_dia:
    if transferencia > 50000:
        importantes.append(transferencia)

print(importantes)