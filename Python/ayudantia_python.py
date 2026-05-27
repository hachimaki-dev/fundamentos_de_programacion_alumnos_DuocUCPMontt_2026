precio_por_noche_camping = 15000
seguro_asistencia_medica = 5000

cantidad_dias = int(input("Ingrese la cantidad de dias de estadia : "))
tramo_usuario = input("Ingrese el tramo (A , B , C o D)").upper()

valor_camping_bruto = precio_por_noche_camping * cantidad_dias

if cantidad_dias <= 5:
    if tramo_usuario == "A" or tramo_usuario == "B":
        valor_camping_bruto *= 0.9
    elif tramo_usuario == "C" or tramo_usuario == "D":
        valor_camping_bruto *= 0.95
    else:
        print("El tramo debe ser de la A a la D")
elif 6 <= cantidad_dias <= 12:
    if tramo_usuario == "A" or tramo_usuario == "B":
        valor_camping_bruto *= 0.8
        seguro_asistencia_medica *= 0.2
    elif tramo_usuario == "C" or tramo_usuario == "D":
        valor_camping_bruto *= 0.85
    else:
        print("El tramo debe ser de la A a la D")
else:
    valor_camping_bruto = valor_camping_bruto
    seguro_asistencia_medica = seguro_asistencia_medica

print(f"Valor del camping en bruto: {valor_camping_bruto}")
print(f"Seguro de asistencia: {seguro_asistencia_medica}")
