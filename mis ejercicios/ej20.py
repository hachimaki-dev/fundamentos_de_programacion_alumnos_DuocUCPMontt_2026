saldo_cliente = 50000
limite_giro_maximo_cliente = 200000
retiro_dinero_cliente = 60000

regla_1 = False
regla_2 = False
regla_3 = False

if retiro_dinero_cliente > limite_giro_maximo_cliente:
    print(f"estimado cliente, su retiro excede limite maximo por que el maximo es {limite_giro_maximo_cliente} y tu quieres sacar {retiro_dinero_cliente}")
else: regla_1 = True
    
if retiro_dinero_cliente > saldo_cliente:
        print(f"no puedes retirar un monto mayor a tu saldo. Tu saldo actual es: {saldo_cliente} y tu quieres retirar {retiro_dinero_cliente}")
else:
        regla_2:True
        
        if retiro_dinero_cliente % 5000 == 0 :
            print("si puedes sacar dinero, dado que el monto que quieres sacar son multiplos de 5000")
            regla_3 = True
        else: 
            print("cajero solo puede entregar billetes de 5000")
        
        if regla_1 and regla_2 and regla_3:
            saldo_cliente -= retiro_dinero_cliente
            print(f"Retiro exitoso de ${retiro_dinero_cliente:,}")
            print(f"Tu nuevo saldo es: ${saldo_cliente:,}")
        else:
            print("retiro no autorizado. Revise las condiciones.")

        
    
