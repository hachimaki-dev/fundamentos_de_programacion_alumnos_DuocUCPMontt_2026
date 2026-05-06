trasferencias_del_dia = [15000, 80000, 2000, 150000]
importantes = []
for transferencia in trasferencias_del_dia:
    if transferencia > 50000:
        importantes.append(transferencia)
print(importantes)