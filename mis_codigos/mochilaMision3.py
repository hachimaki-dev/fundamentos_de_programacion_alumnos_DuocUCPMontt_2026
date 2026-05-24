semana = 7
km = 0
run = 0


while semana > 0 :
    for i in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"] :
        print(f"¿cuántos kilómetros corriste hoy {i}?")
        run = int(input())
        if run <= 0 :
            print("día sin correr")
            semana -= 1
        elif run > 0 :
            km += run
            semana -= 1
if km >= 30 :
    print(f"¡Meta de 30 kilómetros cumplida! ({km})")
    print("¡Felicidades! sigue así")
elif km < 30 :
    print(f"no alcanzaste tu meta ({km}) ¡sigue intentando!")