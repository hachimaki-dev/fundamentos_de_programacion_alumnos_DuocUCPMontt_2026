total_personas = 5
pichangas = 15000
schops = 3500

consumo_total = pichangas * 2 + schops * 5
propina = consumo_total * 0.1
nuevo_consumo = propina + consumo_total
dinero_persona = nuevo_consumo // total_personas
print(f"El dinero que debe pagar cada uno son {dinero_persona}")
