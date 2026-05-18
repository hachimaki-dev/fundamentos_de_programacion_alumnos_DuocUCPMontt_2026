cantidad_btc=0.05
precio_antiguo_btc=50000
precio_actual_btc=62000
dolar_a_peso_chileno=900

diferencia_de_precios=(precio_antiguo_btc - precio_actual_btc)
ganacias_de_usd= cantidad_btc * diferencia_de_precios

ganacias_de_clp=ganacias_de_usd * dolar_a_peso_chileno

print(ganacias_de_clp)