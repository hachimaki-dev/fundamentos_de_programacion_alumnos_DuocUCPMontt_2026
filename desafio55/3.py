personas = 5
pichanga = 15000 
schops = 3500 
propina = 10

total_consumo = (pichanga * 2) + (schops * 5)
total_propina = total_consumo * propina/100
total = total_consumo + total_propina
total_a_pagar = total/personas

print(f"El total del consumo es de {total_a_pagar}")