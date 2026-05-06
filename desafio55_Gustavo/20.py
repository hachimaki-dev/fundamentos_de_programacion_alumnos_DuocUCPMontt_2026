saldo = 50000
limite = 200000
retiro = 60000

if retiro > limite :
    print("Excede limite diario")

elif retiro > saldo :
    print("Saldo insuficiente")

elif retiro%5000 != 0 :
    print("Monto invalido")

else :
    print("Error")