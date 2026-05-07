Criptos = {'BTC': 0.5, 'ETH': 2.0}

opcion = str(input("Ingrese sol : ")).lower()

if opcion in Criptos:
    print ("Procesando")

else:
    print ("Moneda no soportada")