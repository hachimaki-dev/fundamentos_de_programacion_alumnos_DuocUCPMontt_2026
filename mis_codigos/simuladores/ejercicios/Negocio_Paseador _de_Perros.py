# Objetivo: Control de ganancias de un negocio de servicios variables.
# Pregunta al usuario cuántos perros paseó en total el día de hoy.
perros = int(input("cuantos perros paseó hoy: "))
total = 0
perros_totales = perros
#  Usa un ciclo para que, por cada perro, pida ingresar su peso en kg.
while perros > 0:
    peso = float(input("Ingrese el peso del perro en kg: "))
    # Perro pequeño (menos de 10 kg) -> Cuesta $2.000.
    if peso < 10:
        print("Servicio para perro pequeño: $2.000")
        total += 2000
    elif peso <= 25:
        print("Servicio para perro mediano: $4.000")
        total += 4000
    # Perro grande (25 kg o más) -> Cuesta $6.000.
    else:
        print("Servicio para perro grande: $6.000")
        total += 6000
    perros -= 1
    # Al finalizar el ciclo, imprime "Resumen del día: Has paseado X perros ganando en total $Y".
print(f"Resumen del día: Has paseado {perros_totales} perros ganando en total ${total}")
