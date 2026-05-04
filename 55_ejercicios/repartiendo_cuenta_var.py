amigos = 5
pichangas = 15000
schops = 3500
total = pichangas * 2 + schops * 5
print(f"Fuiste a comer con tus {amigos} amigos \nEl total de lo que comieron fue de: {total}")
total = total * 1.10
total_repartido = total // amigos
print(f"Cada uno debería pagar: ${total_repartido}")