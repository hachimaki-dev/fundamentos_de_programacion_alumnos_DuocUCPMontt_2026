dia = 1 
total_kilometros = 0
while dia <= 7:
    km = float(input(f"Cuantos km corriste el dia {dia}?: "))
    if km < 0:
        print("Dia saltado")
    else:
        total_kilometros += km
    dia += 1
print("resultado final")
if total_kilometros >=30:
    print(f"¡Meta semanal lograda! Eres una bestia total, has recorrido {total_kilometros}")
else:
    print(f"Sigue intentando maquina llevamos {total_kilometros} km vamos a por mas")    