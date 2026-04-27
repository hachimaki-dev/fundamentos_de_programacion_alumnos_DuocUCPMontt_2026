# TERMINADO

print("----- MENU DE CRAFTEO -----")

while True:

    print("1. Crafteo de espada de diamante")
    print("2. Crafteo de pico ")
    print("3. salir de la mesa de crafteo")

    opcion = input("Ingrese el numero de la opcion deseada (1/2/3): ")
    if opcion == "1":
        print("!CRAFTEASTE UNA ESPADA DE DIAMANTE!")
        otro_crafteo = input("¿Quieres craftear otro objeto? (si/no): ")
        if otro_crafteo == "si" or otro_crafteo == "SI" or otro_crafteo == "Si":
            continue

        elif otro_crafteo == "no" or otro_crafteo == "NO" or otro_crafteo == "No":
            print("HASTA LUEGO >:3")
            break   

    elif opcion == "2":
        print("!CRAFTEASTE UN PICO!")
        otro_crafteo = input("¿Quieres craftear otro objeto? (si/no): ")
        if otro_crafteo == "si" or otro_crafteo == "SI" or otro_crafteo == "Si":
            continue
        
        elif otro_crafteo == "no" or otro_crafteo == "NO" or otro_crafteo == "No":
            print("HASTA LUEGO >:3")
            break  

    elif opcion == "3":
        print("HASTA LUEGO >:3")
        break
    else:
        print("opcion invalida")
        continue


