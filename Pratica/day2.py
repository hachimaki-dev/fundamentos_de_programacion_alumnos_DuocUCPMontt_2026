def calculadora_tasa(ingresos, edad):
    tasa_base = 0.015
    if ingresos <= 1000000:
        if edad <= 30:
            tasa_final = tasa_base - 0.002 
        else:
            tasa_final = tasa_base - 0.004
    else:
        tasa_final = tasa_base

while True:

    print("Menu de opciones")
    print("1. Calculo creditro")
    print("2. Salir")

    opcion = (input("Seleccione una opcion entre 1 o 2: "))

    if opcion == "1":
        print("Nueva simulacion")

        monto = int(input("Ingrese el monto a solicitar (500.000 a 5.000.000): "))
        while monto < 500000 or monto > 5000000:
            print("ERROR monto fuera de rango")
            monto = int(input("Ingrese el monto a solicitar (500.000 a 5.000.000): "))
        cuotas = int(input("Ingrese cantidad de cuotas (12, 24 o 36): "))
        while cuotas != 12 and cuotas != 24 and cuotas != 36:
            print("ERROR ingrese un numero de cuotas que se solicita")
            cuotas = int(input("Ingrese cantidad de cuotas (12, 24 o 36): "))
        ingresos = int(input("Ingrese el sueldo Bruto: "))
        edad = int(input("Ingrese su edad: "))

        tasa_aplicada = calculadora_tasa(ingresos, edad)
        valor_cuotas = (monto * (1 + tasa_aplicada)) / cuotas

    print("Resultado de la simuacion")
    print(f"Monto aprobado es: {monto: ,}")
    print(F"Taza de interes: {tasa_aplicada * 100:.1f}")
    print(f"El valor de su cuota mensual es: {int(valor_cuotas):}")