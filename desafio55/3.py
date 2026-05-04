personas_en_total = 5
precio_pichanga = 15000
precio_schop = 3500
porcentaje_propina = 10
total_consumo = (precio_pichanga*2)+(precio_schop*5)
subtotal_propina = total_consumo*porcentaje_propina/100
total_a_pagar = subtotal_propina + total_consumo
pago_de_cada_uno = total_a_pagar/personas_en_total
print(f"Cada persona debe pagar {pago_de_cada_uno}.")