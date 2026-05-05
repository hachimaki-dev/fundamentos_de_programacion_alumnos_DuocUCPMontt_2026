# Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.
BTC_nuevo = 62000
BTC_antiguo = 50000
CLP = 900
cantidad_de_BTC = 0.05
print(f"haz invertido {cantidad_de_BTC} en su momento 1 BTC esta a {BTC_antiguo} pero ahora vale {BTC_nuevo}")
diferencia_de_BTC = BTC_nuevo - BTC_antiguo
ganancia_usd = diferencia_de_BTC * cantidad_de_BTC
ganancia_CLP = ganancia_usd * CLP

print(f"tu ganancia es de {ganancia_CLP} mil pesos chilenos")





















