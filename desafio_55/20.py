saldo_cliente = 50000
limite_maximo_giro = 200000
retiro_dinero = 60000

regla_1 = True
regla_2 = True
regla_3 = True


if retiro_dinero > limite_maximo_giro:
    print("excede limite diario")
    
else:
    regla_1 = True
    
if retiro_dinero > saldo_cliente:
    print("saldo insuficiente")
else:
    regla_2 = True
    
if retiro_dinero % 5000 == 0:
    print("retiro exitoso")
    regla_3
else:
    print("no puede retirar dinero solo multiplo de 5")

if regla_1 == True and regla_2 == True and regla_3 == True:
    saldo_cliente = retiro_dinero - saldo_cliente
    print(f"retiraste {retiro_dinero} y te queda {saldo_cliente}")
    
    


