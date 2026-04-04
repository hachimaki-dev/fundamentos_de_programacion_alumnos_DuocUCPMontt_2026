# Negocio: Paseador de Perros
# Objetivo: Control de ganancias de un negocio de servicios variables.

# 1. Pregunta al usuario cuántos perros paseó en total el día de hoy.
# 2. Usa un ciclo para que, por cada perro, pida ingresar su peso en kg.
# 3. Evalúa con if/elif/else:
# - Perro pequeño (menos de 10 kg) -> Cuesta $2.000.
# - Perro mediano (entre 10 y < 25 kg) -> Cuesta $4.000.
# - Perro grande (25 kg o más) -> Cuesta $6.000.
# 4. Suma lo ganado en un acumulador total.
# 5. Al finalizar el ciclo, imprime "Resumen del día: Has paseado X perros ganando en total $Y".

cantidad_perros = int(input("¿Cuántos perros paseó en total el día del hoy?: "))
contador = 0
ganancia = 0
while cantidad_perros > contador:
    peso_del_perro_kg = int(input("ingresa su peso del perro en kg: "))
    if peso_del_perro_kg < 10 :
        ganancia += 2000
    elif peso_del_perro_kg >= 10 and peso_del_perro_kg < 25 :
        ganancia += 4000
    else:
        peso_del_perro_kg >= 25
        ganancia += 6000
    contador += 1

print(f"Resumen del día: Has paseado {cantidad_perros} perros ganado en total ${ganancia}")