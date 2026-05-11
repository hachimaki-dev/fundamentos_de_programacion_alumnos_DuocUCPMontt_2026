transferencias_dia = [15000, 80000, 2000, 150000]
transferencias_sospechosas = []
for monto in transferencias_dia:
    if monto > 50000:
        transferencias_sospechosas.append(monto)

print(transferencias_sospechosas)