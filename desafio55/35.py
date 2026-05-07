transferencias = [15000, 80000, 2000, 150000]
importantes = []
for i in transferencias:
    if i >= 50000:
        importantes.append(i)
print(importantes)