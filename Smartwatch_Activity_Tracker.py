dias_corriendo= 1
acumulacion_km= 0

while dias_corriendo<=7:
    km_recorridos= int(input("¿Cuántos km corriste el dia de hoy: "))
    if km_recorridos<0:
        print("Día saltado")
        dias_corriendo+=1
    elif km_recorridos>=0:
        acumulacion_km+= km_recorridos
        dias_corriendo+=1
if acumulacion_km >= 30:
    print("¡Meta semanal cumplida! Eres un atleta")
else:
    print(f"Sigue intentando, llevas {acumulacion_km} kilometros,¡tú puedes!")