#Banco Virtual (If Anidados)

saldo_inicial = 50000
seleccion_menu = 0
monto_giro = 0
saldo_final = 0
monto_inversion = 0

input("Ingrese su clave de cuatro dígitos")

print("***** Bienvenido a Banco BrandoMas *****")

while True:
    print("¿Qué desea hacer el día de hoy?")
    print(" 1.- Ver Saldo")
    print(" 2.- Girar Dinero")
    print(" 3.- Inversión")
    print(" 4.- Salir")
    seleccion_menu = int(input("Ingrese el número de la acción que desea realizar"))
    if seleccion_menu = 1:
        print("Usted ha elegido hacer una revisión de su saldo")
        print(f"Su saldo actual es de {saldo_inicial}")
        break
    if seleccion_menu = 2:
        monto_giro = int(input("¿Cuál es el monto del giro que desea realizar?"))
        if saldo_inicial <= monto_giro and monto_giro % 5000 = 0:
            print(f"Usted a seleccionado girar ${monto_giro} pesos")
            saldo_final = saldo_inicial - monto_giro
            print(f"El grio de dinero ha sido efectuado su nuevo saldo es de ${saldo_final} pesos")
            break
        else:
            print("Acción invalida, ya que no tiene el saldo suficiente y/o su monto a girar no es múltiplo de 5000")
            break
    if seleccion_menu = 3:
        print("Usted ha elegido hacer una Inversión")
        monto_inversion = int(input("¿Cuánto dinero desea invertir el día de hoy?"))
        if saldo_actual >= monto_inversion:
            saldo_final = saldo final - monto_inversion
            saldo_final = saldo final + monto_Inversion * 2
            print(f"Su saldo final es de ${saldo_final} pesos")
            print("Gracias por preferirnos")
            break
        else:
            print("Su saldo es insuficiente para realizar esta acción")
            break
    if seleccion_menu = 4:
        print("Usted ha elegido Salir de el menú")
        print("Gracias por preferirnos el día de hoy")
        break        






