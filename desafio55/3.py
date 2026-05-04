personas = 5
pichangas = 15000 * 2
schops = 3500 * 5

consumo_total = pichangas + schops
propina = consumo_total * 0.1
monto_final = consumo_total + propina 
print(f"El total a pagar cada persona es de ${monto_final / personas}")
