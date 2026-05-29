ventas_del_día = [1500, -200, 5000, 0, 100]
total = 0
contador_ventas = 0

for i in ventas_del_día:
    if i > 0:
        total = total + i
    else:
        continue
    contador_ventas += 1
print(total)

