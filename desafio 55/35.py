Transferencias = [15000, 80000, 2000, 150000]
importantes = []

for monto in Transferencias:
    if monto > 50000:
        importantes.append(monto)

print("Trasferencias sospechosas al investigar", importantes)    
