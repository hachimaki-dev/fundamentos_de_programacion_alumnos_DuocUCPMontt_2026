transferencias_del_dia = [15000, 80000, 2000, 150000]

transferencias_importantes = []

for transferencia in transferencias_del_dia:

    if transferencia > 50000:
        transferencias_importantes.append(transferencia)

print("Transferencias importantes:", transferencias_importantes)