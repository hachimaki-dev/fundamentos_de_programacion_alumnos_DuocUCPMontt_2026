print("Bienvenido al programa KilometerTracker\nEn este programa ṕodrás saber cuantos kilometros haces a la semana")
dias = 1
kilometros_recorridos = 0

while dias <= 7:
    respuesta = int(input(f"Cuantos kilometros recorriste el día {dias}: "))
    if respuesta <= 0:
        print("Te lesionaste, día saltado.")
        dias += 1
    elif respuesta > 0:
        kilometros_recorridos += respuesta
        print(f"Recorriste {kilometros_recorridos} kilometros el día {dias}")
        dias += 1

print(f"En total recorriste {kilometros_recorridos} kilometros en 7 días")
if kilometros_recorridos >= 30:
    print("¡Felicidades, cumpliste la meta semanal!")
elif kilometros_recorridos < 30:
    print(f"No has logrado la meta semanal.\n¡Pero sigue intentando! que llevas {kilometros_recorridos} de 30 kilometros recorridos.")
        
        