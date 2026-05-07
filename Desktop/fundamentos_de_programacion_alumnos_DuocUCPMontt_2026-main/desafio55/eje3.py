personas = 5
dos_pichangas = 15000 * 2
cinco_shops = 3500 * 5
propina = 10

total_consumo = (dos_pichangas + cinco_shops * propina) / 100

total_consumo = total_consumo * 100
print(f"cada persona debe pagar: {total_consumo / personas}")  