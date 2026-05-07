ventas = [1500, -200, 5000, 0, 100]
total = 0
for i in ventas:
    if i < 0:
        continue
    total += i

print(total)