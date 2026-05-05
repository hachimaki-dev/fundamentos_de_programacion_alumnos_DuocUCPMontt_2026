compra = 0.05
btc_antiguo = 50000
btc_actual = 62000
pesos_chilenos = 900

btc_diferencia = (btc_actual - btc_antiguo) * compra
ganancia = btc_diferencia * pesos_chilenos

print(f"Tu ganancia es de: {ganancia}")
