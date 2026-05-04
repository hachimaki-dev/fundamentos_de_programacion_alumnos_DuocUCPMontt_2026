personas = 5

pichanga = 15000
schop = 3500

propina = 0.1

consumo = pichanga*2 + schop*5

total = consumo * propina
consumo_propina = consumo + total

print(f"en total se paga: ${total} de propina")

todos = consumo_propina / personas

print(f"entre los 5 pagan: ${todos}")