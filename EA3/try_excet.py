valor_medicamentos_mensual = 60000

valor_despacho = 8000


try:
    edad_usuario = int(input("Ingrese su edad"))

    tramo_usuario = input("Ingrese su tramo")
except:
    print("ingrese un numero valido")

if (edad_usuario <= 30 ) and (tramo_usuario == "A" or tramo_usuario == "B"):

        valor_medicamentos_mensual *= 0.82

        valor_despacho *= 0.9



elif (edad_usuario <= 30 ) and (tramo_usuario == "C" or tramo_usuario == "D"):

        valor_medicamentos_mensual *= 0.88



elif (edad_usuario >= 31 and edad_usuario <= 60) and (tramo_usuario == "A" or tramo_usuario == "B") :
    if edad_usuario >= 55:

        valor_despacho *= 0.85

        valor_medicamentos_mensual *= 0.88

    else:

        valor_medicamentos_mensual *= 0.88



elif (edad_usuario >= 31 and edad_usuario <= 60) and (tramo_usuario == "C" or tramo_usuario == "D"):

   valor_medicamentos_mensual *= 0.92


print(f"El valor de medicamentos es: {valor_medicamentos_mensual}")



print(f"El valor del despacho es: {valor_despacho}")