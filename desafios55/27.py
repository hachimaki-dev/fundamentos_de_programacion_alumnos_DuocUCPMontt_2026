ventas_del_dia = [1500,-200,5000,0,100]
total = 0

for i in ventas_del_dia :
    if i <= 0 :
        continue
    total = total + i

print(total)