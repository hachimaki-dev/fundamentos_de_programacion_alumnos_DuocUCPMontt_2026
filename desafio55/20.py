saldo_cajero = 50000
max_dinero_extraíble = 200000
retiro_cajero = 60000
multiplo_5000 = retiro_cajero % 5000
if retiro_cajero > max_dinero_extraíble:
    print("excede del límite diario")
elif retiro_cajero > saldo_cajero:
    print("Saldo insuficiente")
elif multiplo_5000 != 0:
    print("Monto inválido")
else:
    print("retiro exitoso")