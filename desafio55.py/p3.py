cantidad_de_amigos = 5
precio_pichanga = 15000
precio_schops = 3500

valor_pedidos = (precio_pichanga * 2) + (precio_schops * 5)

propina = valor_pedidos // 10

valor_cuenta = valor_pedidos + propina

pago_por_persona = valor_cuenta // 5
print(pago_por_persona)