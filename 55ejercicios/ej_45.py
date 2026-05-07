# Ejercicio 45: Validación de Existencia (Criptos)

print("========================")
print("Validacion medio de Pago")
print("========================")

usuario = {'BTC': 0.5, 'ETH': 2.0}

if 'SOL' in usuario:
    print('Procesando')
else:
    print('Moneda no soportada')