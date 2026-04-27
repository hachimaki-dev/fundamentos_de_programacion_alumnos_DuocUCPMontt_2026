# TERMINADO PERO ESTUDIA Y REVISA

sumador_dias = 0
sumador_km = 0

print("===== Smartwatch =====")

respuesta = input("¿Corriste esta semana? (si/no): ").lower()

while respuesta == "si":
    
    km = int(input("¿Cuántos km corriste el lunes?: "))
    if km > 0:
        print("Km ingresados correctamente")
        sumador_dias += 1
        sumador_km += km
    else:
        print("Te lesionaste o descansaste, ¡cuidate! >:3")

    
    km = int(input("¿Cuántos km corriste el martes?: "))
    if km > 0:
        print("Km ingresados correctamente")
        sumador_dias += 1
        sumador_km += km
    else:
        print("Te lesionaste o descansaste, ¡cuidate! >:3")

    print("-" * 30)
    print(f"Total de km recorridos en la semana: {sumador_km}")
    print(f"Días de actividad registrados: {sumador_dias}")
    
    break 

if respuesta == "no":
    print("¡Ponte las pilas para la próxima semana! >:3")