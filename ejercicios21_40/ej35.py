transferencia = [15000, 80000, 2000, 150000]
importante = []

for money in transferencia:
    if money > 50000:
        importante.append(money)
print(importante)