orden = {'Papas': 5000, 'Pizza': 10000}
total = 0
for i in orden.items():
    
    print(i)

total = orden['Papas'] + orden['Pizza']
total = total * 1.10
print(f"Total final: {total}")