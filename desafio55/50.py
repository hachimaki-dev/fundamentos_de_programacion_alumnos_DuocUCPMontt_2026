cuenta = {"Papas":5000, "Pizza": 10000}
valor_platos = 0
for alimento, precio in cuenta.items():
    valor_platos += precio
    propina = 0.10 * valor_platos
    subtotal = propina + valor_platos
print(f"Total Final : {subtotal}")