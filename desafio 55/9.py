polera = 15000
tela = 4000
estampado = 2500
empaque= 500
poleras_vendidas = 50

valor_por_una_polera = (estampado + empaque + tela)

costo_de_50_poleras = (valor_por_una_polera * poleras_vendidas)

ganancia_50_poleras = (polera * poleras_vendidas)

ganancia_total = (ganancia_50_poleras - costo_de_50_poleras)



print("Vas a vender poleras estampadas y necesitas calcular tus ganancias mensuales.")

input()

print(f"El costo total de hacer 1 polera es de: {valor_por_una_polera}.")

input()

print(f"El costo de hacer 50 poleras es de: {costo_de_50_poleras}.")

input()

print(f"Como vendiste 50 poleras cada una valuada en 15000 generaste {ganancia_50_poleras}, pero restando los costos de fabricacion en total ganaste: {ganancia_total}. ")