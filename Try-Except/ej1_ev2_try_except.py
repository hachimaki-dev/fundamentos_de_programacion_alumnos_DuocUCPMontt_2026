valor_mensual_medicamento = 60000
valor_despacho = 8000

while True:
    try:
        edad_usuario = int( input("Ingrese su edad: ") )
        break
    except ValueError:
        print("No ha ingresado un número. Intente nuevamente")

while True: # Revisar
    try:
        tramo_usuario = input("Ingrese su tramo (A, B, C o D: )")
        break
    except:
        print("Valor ingresado no es válido. Intente nuevamente")

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

try:
    print(f"El valor de medicamentos es: {valor_mensual_medicamento}")
except NameError:
    print("Variable 'valor_mensual_medicamento' no está definida")
except:
    print("Algo salió mal")

try:
    print(f"El valor del despacho es: {valor_despacho}")
except NameError:
    print("Variable 'valor_despacho' no está definida")
except:
    print("Algo salió mal")
