
print("Bienvenido al banco")
saldo_total = 0
while True :
    print(f"saldo actual:{saldo_total}")
    print("1.depositar")
    print("2.retirar")
    print("3.salir")

    opcion=int(input("elija"))
   
    if opcion == 1 :
        saldo_depositado = int(input("cuanto desea depositar"))

        saldo_total = saldo_total + saldo_depositado
    
    if opcion == 2 :
     saldo_retirado =int(input("cuanto desea retirar"))

     if saldo_total < saldo_retirado:
        print("no hay fondos suficientes")
     else :
        saldo_total = saldo_total - saldo_retirado
    if opcion == 3 :
        break
    
   
