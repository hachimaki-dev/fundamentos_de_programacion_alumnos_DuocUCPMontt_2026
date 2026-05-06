saldo_cliente = 50000
limite_de_giro = 200000

retiro_de_dinero = 60000

if retiro_de_dinero > limite_de_giro :
    print("excede el limite de giro")

if retiro_de_dinero > saldo_cliente:
    print("saldo insuficiente")

if retiro_de_dinero % 5000:
    print("si puedes sacar dinero por que es multiplo de 5000")