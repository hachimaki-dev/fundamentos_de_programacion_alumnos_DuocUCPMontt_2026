
cuenta = {'Papas': 5000, 'Pizza': 10000}
total = 0
 
for precio in cuenta.items():
    total += precio[1]
 
propina = total * 0.10
total_final = total + propina
 
print(f"Total final: {total_final}")
print()