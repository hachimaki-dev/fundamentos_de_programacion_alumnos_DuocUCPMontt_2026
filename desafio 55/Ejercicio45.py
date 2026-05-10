monedas = {"BTC": 0.5, "ETH": 2.0}
metodo_de_pago = "SOLANO"

for moneda in monedas:
    if moneda == metodo_de_pago:
        print("Pagado con exito")
        import sys
        sys.exit()
    else:
        continue
print("Moneda no soportada")