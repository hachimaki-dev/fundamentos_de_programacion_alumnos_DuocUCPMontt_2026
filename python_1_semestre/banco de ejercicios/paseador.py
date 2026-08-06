""" Objetivo: Control de ganancias de un negocio de servicios variables.

1. Pregunta al usuario cuántos perros paseó en total el día de hoy.
2. Usa un ciclo para que, por cada perro, pida ingresar su peso en kg.
3. Evalúa con if/elif/else:
- Perro pequeño (menos de 10 kg) -> Cuesta $2.000.
- Perro mediano (entre 10 y < 25 kg) -> Cuesta $4.000.
- Perro grande (25 kg o más) -> Cuesta $6.000.
4. Suma lo ganado en un acumulador total.
5. Al finalizar el ciclo, imprime "Resumen del día: Has paseado X perros
 ganando en total $Y"."""

perros = int(input("cuantos perros paseaste hoy ?: "))
contador = 0
total = 0

while contador < perros:
    peso = int(input("ingresa el peso de cada perro en kg: "))

    if peso < 10:
        print("cuesta 2000")
        total +=2000
        contador +=1

    elif peso >= 10 and peso < 25:
        print("cuesta 4000")
        total += 4000
        contador +=1

    elif peso >= 25:
        total += 6000
        print("cuesta 6000")
        contador +=1

print(f" has paseado a {perros} perros y has ganado un total de {total}")

    

