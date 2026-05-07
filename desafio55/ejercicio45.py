criptos = {'BTC': 0.5, 'ETH': 2.0}
print("El usuario quiere pagar algo usando solana, se revisara si dispone de esta.")

if "SOL" in criptos:
    print("Procesando pago...")
else:
    print("Moneda no soportada.")
