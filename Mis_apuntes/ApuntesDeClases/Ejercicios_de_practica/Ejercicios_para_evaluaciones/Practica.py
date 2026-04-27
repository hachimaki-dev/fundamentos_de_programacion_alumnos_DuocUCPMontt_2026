print("===== BIENVENIDO AL MENÚ DE COMPRA ======")
operator = 1
vandal = 2
spectre = 3
sheriff = 4
phantom = 5
arma = 0 #CONTADOR
arma_selecta = int(input("Pickea un arma. \n 1)Operator \n 2)Vandal \n 3)Spectre \n 4)Sheriff \n 5)Phantom "))
while arma_selecta != 0 and arma_selecta < 6:
    if arma == 5:
        break
    if arma_selecta == 1:
        arma += 1
        print(f"Comprando exitosamente el arma numero {operator}.")
        print("Has escogido la Operator, destroza a tus enemigos")
        arma_selecta = int(input("Pickea un arma. 1)Operator \n 2)Vandal \n 3)Spectre \n 4)Sheriff \n 5)Phantom "))
    elif arma_selecta ==2:
        arma += 1
        print(f"Comprando exitosamente el arma numero {vandal}")
        print("Escogiste la Vandal, arma precisa y potente.")
        arma_selecta = int(input("Pickea un arma. 1)Operator \n 2)Vandal \n 3)Spectre \n 4)Sheriff \n 5)Phantom "))
    elif arma_selecta ==3:
        arma += 1
        print(f"Comprando exitosamente el arma numero {spectre}.")
        print("Escogiste la Spectre, mata a tus enemigos corriendo.")
        arma_selecta = int(input("Pickea un arma. 1)Operator \n 2)Vandal \n 3)Spectre \n 4)Sheriff \n 5)Phantom "))
    elif arma_selecta ==4:
        print("Sheriff: Notificación - Agotada.")
        arma_selecta = int(input("Pickea un arma. 1)Operator \n 2)Vandal \n 3)Spectre \n 4)Sheriff \n 5)Phantom "))
        continue
    elif arma_selecta ==5:
        arma += 1
        print(f"Comprando exitosamente el arma numero {phantom}.")
        print("Escogiste la phantom, silenciosa y rápida.")
        arma_selecta = int(input("Pickea un arma. 1)Operator \n 2)Vandal \n 3)Spectre \n 4)Sheriff \n 5)Phantom "))
print(f"Has comprado un total de {arma} armas.")
