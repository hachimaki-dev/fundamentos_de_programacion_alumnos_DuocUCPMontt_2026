dia = 0
km_totales = 0

while dia < 7:
    km = float(input(f"Digite los km del día {dia + 1}: "))

    dia += 1
    print("Día:", dia)

    if km < 0:
        print(f"Te lesionaste el día {dia}")
        # no sumamos km
    else:
        km_totales += km  # solo suma si es válido

# esto va FUERA del while
if km_totales >= 30:
    print("¡Meta semanal cumplida! Eres un atleta")
else:
    print("¡Meta semanal no cumplida! Sigue esforzándote")

print(f"Total de km recorridos: {km_totales}")