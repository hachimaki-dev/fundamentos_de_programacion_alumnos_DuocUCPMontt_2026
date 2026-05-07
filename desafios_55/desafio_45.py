usuario_criptos = {'BTC': 0.5, 'ETH': 2.0}
moneda_pago = "SOL"

if moneda_pago in usuario_criptos:
    print("Procesando")
else:
    print("Moneda no soportada")