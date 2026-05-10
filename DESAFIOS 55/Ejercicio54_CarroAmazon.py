carro=[{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]
total=0
for i in carro:
    total+=(i['qty']*i['precio'])
    
if total > 50000:
    total-=total*0.1
    
print(total)      