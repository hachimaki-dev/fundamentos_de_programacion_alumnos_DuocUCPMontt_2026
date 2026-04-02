contador = 0
km_totales = 0

while contador < 7:
    km_corridos = int(input(f"¿Cuantos kilómetros corriste el día {contador+1}?: "))
    if km_corridos < 0:
        print("Día saltado")
    else:
        km_totales += km_corridos
    contador += 1

if km_totales >= 30:
    print("¡Meta semanal cumplida! Eres un atleta")
else:
    print(f"Sigue intentando, llevas {km_totales} kilómetros, ¡Tú puedes!")
    