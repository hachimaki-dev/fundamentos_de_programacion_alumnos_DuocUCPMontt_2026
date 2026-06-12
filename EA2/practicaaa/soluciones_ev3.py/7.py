critica = 0
normales = 0
bajas = 0

for i in range(5):
    temperatura = float(input("ingrese una temperatura:"))
    if temperatura > 80:
        print("ALERTA: Temperatura critica")
        critica += 1
    elif temperatura >=50 and temperatura <= 80:
        print("NORMAL: temperatura en estado normal")
        normales += 1
    else:
        temperatura <=50
        print("BAJA: temperatura baja ")
        bajas += 1

print("temperatura critica",critica)
print("temperatura normal",normales)
print("temperatura baja",bajas)

