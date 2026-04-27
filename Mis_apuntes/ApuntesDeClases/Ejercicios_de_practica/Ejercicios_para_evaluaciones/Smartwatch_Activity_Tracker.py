dia = 1
km = 0
while dia <= 7:
    kmd = int(input(f"Cuantos km corriste el dia {dia}? "))
    if kmd < 0:
        print("Día saltado.")
    else:
        km += kmd
    dia += 1
if km >= 30:
    print("Meta semanal alcanzada.")
else:
    print("Tu puedes, sigue intentado!")