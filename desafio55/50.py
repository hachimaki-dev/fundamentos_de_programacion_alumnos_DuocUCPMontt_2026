cuenta = {
    "papas" : 5000,
    "pizza" : 10000
}
subtotal = 0
for plato, precio in cuenta.items():
    subtotal += precio
total_con_propina = subtotal * 1.10
print(total_con_propina)

