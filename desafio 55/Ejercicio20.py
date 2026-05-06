saldo = 50000
retiro_maximo = 200000
retiro = 60000

print(f"Tu saldo actual es de {saldo}")
print(f"El máximo para retirar en el cajero es de {retiro_maximo}")
print(f"Deseas retirar {retiro}")

if retiro <= saldo and retiro <= retiro_maximo and retiro % 5000 == 0:
    saldo = saldo - retiro
    print(f"Has retirado {retiro} con éxito")
    print(f"Tu nuevo saldo es de {saldo}")
elif retiro > saldo:
    print("Saldo insuficiente")
elif retiro > retiro_maximo:
    print("Supera el monto máximo permitido")
else:
    print("Monto inválido (debe ser múltiplo de 5000)")