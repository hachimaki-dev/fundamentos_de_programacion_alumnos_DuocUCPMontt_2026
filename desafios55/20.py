saldo_usuario = 50000
limite_diario = 200000
retiro = 60000

if saldo_usuario > limite_diario :
    print("Excede limite diario")

elif saldo_usuario < retiro :
    print("Saldo insuficiente")

elif retiro != 5000 % 5 == 0 :
    print("Monto Invalido")
else :
    print("Retiro Exitoso")


