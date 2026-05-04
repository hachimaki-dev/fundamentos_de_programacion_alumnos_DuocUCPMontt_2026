personas = 5
pichangas = 2 * 15000
shops = 5 * 3500

consumo_total = pichangas + shops
total_con_propina = consumo_total * 1.10

couta_por_persona =  total_con_propina // personas

print(f"la couta por persona es de: ${couta_por_persona}")