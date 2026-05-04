amigos = 5
pichangas = 15000
schops = 3500
print(f"Fuiste a comer con tus {amigos} amigos \nEl total de lo que comieron fue de: {pichangas * 2 + schops * 5}")
total = pichangas * 2 + schops * 5
total = total * 1.10
total_repartido = total // amigos
print(f"Cada uno debería pagar: ${total_repartido}")