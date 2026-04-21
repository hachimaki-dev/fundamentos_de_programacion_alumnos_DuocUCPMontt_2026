klm_corridos = ""
dias_semana = 1
kilometros_totales = 0

while dias_semana <= 7 :
    klm_corridos = int(input(f"Cuantos kilometros corriste en el dia {dias_semana}:  "))
    kilometros_totales += klm_corridos
    dias_semana += 1
    if klm_corridos < 0 :
        print("D í a  s a l t a d o ")

if kilometros_totales >= 30 :
    print("¡Meta semanal cumplida! Eres un atleta")
elif kilometros_totales < 30 :
    print(f"Sigue intentando, llevas {kilometros_totales} kilómetros, ¡tú puedes!")
    