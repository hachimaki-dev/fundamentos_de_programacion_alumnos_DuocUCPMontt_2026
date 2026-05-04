compra_inicial_Bitcoin=0.05 #BTC

valor_BTC_al_comprar=50000 #valor de 1 BTC al momento de comprar

valor_BTC_hoy=62000 #valor de 1 BTC hoy

costo_inicial_BTC=compra_inicial_Bitcoin*valor_BTC_al_comprar
costo_actual_BTC=compra_inicial_Bitcoin*valor_BTC_hoy

ganancia_actual=900*(costo_actual_BTC-costo_inicial_BTC)


print(f"${ganancia_actual} has ganado al dia de hoy")