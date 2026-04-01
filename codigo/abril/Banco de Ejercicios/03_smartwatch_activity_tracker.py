contador = 1
acumulador_kilometros = 0
meta_kilometros = 30

while contador <= 7:
    kilometros_del_dia = int(input(f"¿Cuántos km corriste el día {contador}?: "))
    if kilometros_del_dia < 0:
        print("Día saltado")
        contador += 1
    else:
        acumulador_kilometros += kilometros_del_dia
        contador += 1

if acumulador_kilometros >= meta_kilometros:
    print(f"Kilometros recorridos: {acumulador_kilometros} km")
    print("¡Meta semanal cumplida! Eres un atleta.")
else:
    print(f"Sigue intentando, llevas {acumulador_kilometros} kilómetros, ¡tú puedes!")

