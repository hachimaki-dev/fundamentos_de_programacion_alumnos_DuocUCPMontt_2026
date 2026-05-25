valor_mensual_medicamentos = 60000
valor_despacho_domicilio = 8000

while True:
    try:
        edad_usuario = int(input("Ingrese su edad: "))
        break
    except:
        print("Ocurrió un error")
        print("Intenta nuevamente")

while True:
    try:
        tramo_usuario = input("Ingrese su tramo (A, B, C o D): ")
        break
    except:
        print("Ocurrió un error")
        print("Intenta nuevamente")

if (edad_usuario <= 30) and (tramo_usuario == "A" or tramo_usuario == "B" ):
  valor_mensual_medicamentos = valor_mensual_medicamentos * 0.82
  valor_despacho_domicilio = valor_despacho_domicilio * 0.9

elif (edad_usuario <= 30) and (tramo_usuario == "C" or tramo_usuario == "D" ):
  valor_mensual_medicamentos = valor_mensual_medicamentos * 0.88

elif (edad_usuario >= 31 and edad_usuario <= 60) and (tramo_usuario == "A" or tramo_usuario == "B" ):
  if edad_usuario >= 55 and edad_usuario <= 60:
    valor_mensual_medicamentos = valor_mensual_medicamentos * 0.88
    valor_despacho_domicilio = valor_despacho_domicilio * 0.85

  else:
    valor_mensual_medicamentos = valor_mensual_medicamentos * 0.88
    valor_despacho_domicilio = valor_despacho_domicilio * 0.9

elif (edad_usuario >= 31 and edad_usuario <= 60) and (tramo_usuario == "C" or tramo_usuario == "D" ):
  valor_mensual_medicamentos = valor_mensual_medicamentos * 0.92

print(f"El valor de medicamentos es: {valor_mensual_medicamentos}")
print(f"El valor del despacho es: {valor_despacho_domicilio}")