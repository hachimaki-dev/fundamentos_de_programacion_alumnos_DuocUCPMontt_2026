sueldo_base = 800000
bonos = {"colacion": 50000, "movilizacion": 30000}
descuentos = {"AFP": 0.10, "Salud":0.07}
valor_descuentos = 0
valor_bonos = 0
for valor in bonos.values():
    valor_bonos += valor
for descuento in descuentos.values():
    valor_descuentos += (descuento*sueldo_base)
    total_liquido = sueldo_base + valor_bonos - valor_descuentos
print(total_liquido)