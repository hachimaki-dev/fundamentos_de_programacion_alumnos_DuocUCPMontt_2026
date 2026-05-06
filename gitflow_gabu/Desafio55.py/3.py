personas = 5
pichanga = 15000 
schops = 3500 
propina = 1.10

consumo_total = pichanga * 2 + schops * 5
consumo_total  = consumo_total * 1.10
 
consumo_persona = int(consumo_total / personas)
print("Esto es lo que debe pagar cada persona: " , consumo_persona)





