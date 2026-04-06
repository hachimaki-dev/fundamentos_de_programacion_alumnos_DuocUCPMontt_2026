kmcorridos = 0
dia_de_semana = 1
while dia_de_semana <= 7:
    km = float(input(f"¿Cuantos km corriste el día {dia_de_semana}? "))
    if km < 0:
        print("Día saltado")
        dia_de_semana = dia_de_semana + 1        
    elif km >= 0:
        kmcorridos = kmcorridos + km
        dia_de_semana = dia_de_semana + 1
if kmcorridos >= 30:
    print("¡Meta semanal cumplida! Eres un atleta")
else:
    print(f"Sigue intentando, llevas {kmcorridos} kilómetros, ¡Tú puedes!")