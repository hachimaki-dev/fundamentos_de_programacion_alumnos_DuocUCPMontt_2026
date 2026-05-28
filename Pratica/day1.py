print("=====================")
print("Bienvenido al Camping")
print("=====================")

dias_del_usuario = int(input("Ingre cuantos Días: "))
tramo_del_usuario = input("Ingrese su tramo (A, B, C, D): ")

precio_camping_por_personas = 15000
seguro_medico = 5000

if (dias_del_usuario <= 5) and (tramo_del_usuario == "A" or tramo_del_usuario == "B"):
    precio_camping_por_personas *= 0.10

elif (dias_del_usuario <= 5) and (tramo_del_usuario == "C" or tramo_del_usuario == "D"):
    precio_camping_por_personas *= 0.05

elif (dias_del_usuario >= 6 and dias_del_usuario <=12) and (tramo_del_usuario == "A" or tramo_del_usuario == "B"):
    precio_camping_por_personas *= 0.20

elif (dias_del_usuario >= 6 and dias_del_usuario <=12) and (tramo_del_usuario == "C" or tramo_del_usuario == "D"):
    precio_camping_por_personas *= 0.15

elif (dias_del_usuario <= 5) and (tramo_del_usuario == "A" or tramo_del_usuario == "B"):
    precio_camping_por_personas *= 0.10

print(f"Los días que se queda son:{dias_del_usuario}")
print(f"El valor sera:{precio_camping_por_personas}")