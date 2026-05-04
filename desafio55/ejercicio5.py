print("Ejercicio 5: Administración de carga BIP")

saldo = 10000

print("Vas viajando y tomas un pasaje de micro")
saldo -= 730
print("Una vez llegaste a la estación tomas un viaje en metro ida y vuelta.")
saldo -= 850 * 2
print("Después de un largo día estas dispuesto a irte a casa, pero antes recargas 3000$ a tu tarjeta BIP.")
saldo += 3000
print(f"En total te quedan ${saldo} pesos en la tarjeta BIP.")