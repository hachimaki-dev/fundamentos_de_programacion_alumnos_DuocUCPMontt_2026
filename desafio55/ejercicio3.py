pichanga = 15000
schops = 3500
cantidad_de_personas = 5

pichangas_pedidas = pichanga * 2
schops_pedidos = schops * 5
consumo = pichangas_pedidas + schops_pedidos
 
propina = consumo * 0.1

total_a_pagar = propina + consumo

total_a_pagar_individual = total_a_pagar / cantidad_de_personas
print(f"Cada uno tendrà que pagar {total_a_pagar_individual}CLP")

