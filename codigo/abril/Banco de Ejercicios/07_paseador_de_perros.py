maximo_perro_chico = 9 # Peso en KGs
minimo_perro_grande = 25

paga_perro_chico = 2000 # Paga en CLP
paga_perro_mediano= 4000
paga_perro_grande = 6000

acumulador_ganancia = 0

perros_paseados = int(input("¿Cuántos perros paseaste hoy?: ")) 
# Convertir la cantidad a un rango, empezando por el 1 y sumando 1 a la cantidad ingresada para manejarlo con más facilidad.
# Ejemplo: si perros_paseados es 3, range(1, 4) dará 1, 2, 3.
rango_perros_paseados = range(1, perros_paseados + 1)

for perro in rango_perros_paseados:
    peso = int(input(f"\nIngresa el peso en kilos del perro {perro} (sin decimales): "))
    if peso <= maximo_perro_chico: # Perros pequeños
        acumulador_ganancia += paga_perro_chico
        print(f"Perro pequeño. Ganaste ${paga_perro_chico}")
    elif peso > maximo_perro_chico and peso < minimo_perro_grande: # Perro mediano
        acumulador_ganancia += paga_perro_mediano
        print(f"Perro mediano. Ganaste ${paga_perro_mediano}")
    else: # Perro grande
        acumulador_ganancia += paga_perro_grande
        print(f"Perro grande. Ganaste ${paga_perro_grande}")

print(f"\nResumen del día:\nHas paseado {perros_paseados} perros y en total ganaste ${acumulador_ganancia}")
