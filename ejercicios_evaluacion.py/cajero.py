saldo_inicial = 50000
monto = 0
opcion_elegida = 0
cantidad_a_invertir = 0
print("bienvenido!!\nen que podemos ayudarte hoy?")
print("1. Ver saldo")
print("2. Girar dinero")
print("3. Invertir")
print("4. salir")
while opcion_elegida != 4:
    opcion_elegida = int(input("eliga una de las opciones: "))
    if opcion_elegida == 1:
        print(f"su saldo actual es de {saldo_inicial}")
    elif opcion_elegida == 2:
        monto = int(input("que monto desea girar?"))
        if monto <= 50000  and monto %5000 == 0:
                saldo_inicial = saldo_inicial - monto
                print("el giro se ha relizado con exito")
                print(f"su nuevo saldo es de {saldo_inicial}")
        else:
            print("saldo insuficiente o monto no acepatado :8")
    elif opcion_elegida == 3:
        cantidad_a_invertir = int(input("ingresa la cantidad que deseas invertir"))
        if cantidad_a_invertir >= 50000:
            nuevo_saldo = saldo_inicial + (saldo_inicial * 2)
            print(f"la inversion se ha realizado con exito su nuevo saldo es de {nuevo_saldo}")
        else:
            print("saldo insuficiente :( ")
    else:
        print("ingrese una opcion valida")
if opcion_elegida == 4: 
    print("hasta luego!!\ncajero apagandose")