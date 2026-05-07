criptomonedas = {"BTC": 0.5,
                 "ETH": 2.0}
cripto_seleccionada = input("¿Que cripto desea usar?")
if cripto_seleccionada in criptomonedas:
    print("Procesando")
else:
    print("Moneda no encontrada")