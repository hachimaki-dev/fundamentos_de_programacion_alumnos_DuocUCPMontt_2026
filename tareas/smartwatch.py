dias = 0
kilometros_recorridos = 0
print("--bienvenidos a samrtwatch Activity Tracker--")
print("veamos cuanto recorriste estos 7 dias!!")
while dias != 7:
    dias = dias + 1
    kilometros = int(input(f"cuantos kilometros recorriste el dia {dias}?"))
    if kilometros <= 0:
        print("dia saltado")
    elif kilometros >= 1:
        kilometros_recorridos = kilometros_recorridos + kilometros
if kilometros_recorridos >= 30:
    print("--¡meta semanal completa!--")
    print(f"recorriste {kilometros_recorridos} kilometros!!")
elif kilometros_recorridos < 30:
    print(f"sigue intentadolo,llevas {kilometros_recorridos} kilometros,tu puedes!!")