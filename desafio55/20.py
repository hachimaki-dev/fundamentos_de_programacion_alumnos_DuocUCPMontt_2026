saldo = 50000
limite = 200000

retiro = int(input("Monto a retirar: "))
if retiro % 5000 != 0 :
    print("Monto invalido")
    
elif retiro > limite :
    print("Exede el limite diario")

elif retiro > saldo :
    print("Saldo insuficiente") 


else :
    print("Retiro exitoso")