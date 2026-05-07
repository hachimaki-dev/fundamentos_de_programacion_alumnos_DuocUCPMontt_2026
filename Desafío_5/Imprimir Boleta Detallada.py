Cuenta = {"PAPAS" : 5000, "PIZZA" : 10000}
total = 0

for plato, precio in Cuenta.items():
    
    total += precio

    propina = total * 0.10

    total_final = total + propina

print ("Total final", total_final)
