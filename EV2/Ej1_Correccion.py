valor_mensual_medicamento = 60000
valor_despacho = 8000
while True:
    try:
        edad_usuario = int(input("Ingrese su edad: "))
        break
    except ValueError :
        print("Porfavor ingrese una edad válida, letras no están permitidas.")

tramo_usuario = input("Ingrese su tramo (A,B,C o D: )")

if (edad_usuario <= 30) and (tramo_usuario == "A" or tramo_usuario == "B"):
    valor_mensual_medicamento = valor_mensual_medicamento * 0.82
    valor_despacho = valor_despacho * 0.9

elif (edad_usuario <= 30) and (tramo_usuario == "C" or tramo_usuario == "D"):
    valor_mensual_medicamento = valor_mensual_medicamento * 0.88

elif (edad_usuario >= 31 and edad_usuario <= 60) and (tramo_usuario == "A" or tramo_usuario == "B"):  
    if edad_usuario >= 55:
        valor_mensual_medicamento = valor_mensual_medicamento * 0.88
        valor_despacho = valor_despacho * 0.85
    else:
        valor_mensual_medicamento = valor_mensual_medicamento * 0.88
        valor_despacho = valor_despacho * 0.9
        
elif (edad_usuario >= 31 and edad_usuario <= 60) and (tramo_usuario == "C" or tramo_usuario == "D"):
    valor_mensual_medicamento = valor_mensual_medicamento * 0.92

print(f"El precio mensual de tus medicamentos será: {valor_mensual_medicamento}")

print(f"Y el de tu despacho sería de: {valor_despacho}")
