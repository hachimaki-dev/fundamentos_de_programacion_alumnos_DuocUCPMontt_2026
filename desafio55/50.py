cuenta = {'Papas': 5000, 'Pizza': 10000}
total_final = 0
for plato,precio in cuenta.items():
    total_final += precio
    print(total_final)
propina = total_final * 0.10
total_final += propina
print(total_final)