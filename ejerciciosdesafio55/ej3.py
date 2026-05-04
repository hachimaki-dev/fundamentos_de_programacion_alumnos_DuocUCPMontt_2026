total_personas = 5
valor_pichanga = 15000
valor_schops = 3500

valor_pichanga = valor_pichanga * 2
valor_schops = valor_schops * 5
#suma pichanga y los schops
total_a_pagar = valor_pichanga + valor_schops
#total mas propina
propina = 110 # suma del 100% + 10 %

total_final = total_a_pagar * propina / 100
total_por_persona = total_final / 5

print(f"el total a pagar por persona es: {total_por_persona}")