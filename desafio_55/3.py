#Repartiendo la cuenta en el bar

personas = 5
cantidad_pichangas = 2
cantidad_shops= 5 
valor_pichangas = 15000
valor_shops = 3500
consumo = (cantidad_pichangas * valor_pichangas) + (cantidad_shops * valor_shops)

propina = (consumo * 10) / 100 

total = (consumo + propina)

print(f"el total es {total/5}")



