cuenta={'Papas': 5000, 'Pizza': 10000}
total= 0
for comida,i in cuenta.items():
    print(comida,i)
    total += i
print(f'Propina Sugerida ${int(total*0.1)}')
print(f'Total final {int(total + (total*0.1))}')    