transferencias_diarias = [15000, 80000, 2000, 150000]
importantes = []
for t in transferencias_diarias:
    if t > 50000:
        importantes.append(t)
print(importantes)