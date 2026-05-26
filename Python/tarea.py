valor_mensual_medicamento = 60000
edad_usuario = 0
valor_despacho = 8000
while True:
    try:
        edad_usuario = int( input("Ingrese su edad: ") )
    except :
        print("ingrese un numero valido")
    try:
        tramo_usuario = input("Ingrese su tramo (A, B, C o D: )")
    except :
        print("ingrese el tramo ")

except:
    if (edad_usuario <= 30) and (tramo_usuario == "A" or tramo_usuario == "B"):
        valor_mensual_medicamento *= 0.82
        valor_despacho *= 0.9



elif (edad_usuario <= 30) and (tramo_usuario == "C" or tramo_usuario == "D"):

  valor_mensual_medicamento *= 0.88



elif (edad_usuario >= 31 and edad_usuario <= 60) and (tramo_usuario == "A" or tramo_usuario == "B"):
    if edad_usuario >= 55:
        valor_despacho *= 0.85
        valor_mensual_medicamento *= 0.88
    else:
        valor_mensual_medicamento *= 0.88



elif (edad_usuario >= 31 and edad_usuario <= 60) and (tramo_usuario == "C" or tramo_usuario == "D"):

  valor_mensual_medicamento *= 0.92



print(f"El valor de medicamentos es: {valor_mensual_medicamento}")



print(f"El valor del despacho es: {valor_despacho}")