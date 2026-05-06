ventas_del_dia = [1500,-200,5000,0,100]

total = 0

for i in ventas_del_dia :
    if i > 0 :
        total += i
    elif i < 0 :
        continue
print(total)