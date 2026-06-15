def calcular_multa(dias_atraso, valor_por_dia=100):
    return dias_atraso * valor_por_dia

while True:
    try:
        opcion = int(input("Escriba los días de atraso: "))
        if opcion > 0:
            break
        else:
            print("Error: Escriba un numero natural valido")
    except ValueError:
        print("Error: Escriba un numero en valor, no en letras, por favor, vuelva a intentarlo")
resultado = calcular_multa(opcion)
print("")