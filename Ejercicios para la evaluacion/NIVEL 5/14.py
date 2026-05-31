#CAFETERIA EXOTICA
sueldo_en_caja = 0
continuar_turno = True
print("=== BIENVENIDO A CAFETERIA DE BELLIUM ===")
while continuar_turno:
    while True:
        try:
            eleccion_menu = int(input("1. Ver saldo en caja.\n2. Registrar venta.\n3. Registrar gasto.\n4. Salir\n ===> "))
            if eleccion_menu > 4 or eleccion_menu < 1:
                print("Vuelva a ingresar solo una de las opciones en pantalla.")
                continue
            else:
                break
        except ValueError:
            print("Debe ingresar el número de la opción que requiere.")

    if eleccion_menu == 1:
        print(f"Saldo en caja: {sueldo_en_caja}.")
    elif eleccion_menu == 2:
        while True:
            try:
                valor_del_ingreso = int(input("Ingrese cuanto dinero ingreso: "))
                if valor_del_ingreso < 0:
                    print("No se permiten numeros negativos.")
                    continue
                else:
                    sueldo_en_caja += valor_del_ingreso
                    break
            except ValueError:
                print("ERROR, debe ingresar numeros enteros.")
    elif eleccion_menu == 3:
        while True:
            try:
                valor_del_retiro = int(input("Ingrese cuanto dinero retiro: "))
                if valor_del_retiro < 0:
                    print("No se permiten numeros negativos.")
                    continue
                else:
                    sueldo_en_caja -= valor_del_retiro
                    break
            except ValueError:
                print("ERROR, debe ingresar numeros enteros.")
    else:
        print(f"Dinero registrado al final del día: {sueldo_en_caja}.")
        continuar_turno = False