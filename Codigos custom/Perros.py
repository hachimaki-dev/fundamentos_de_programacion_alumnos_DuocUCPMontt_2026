"""Negocio: Paseador de Perros
Objetivo: Control de ganancias de un negocio de servicios variables.

1. Pregunta al usuario cuántos perros paseó en total el día de hoy.
2. Usa un ciclo para que, por cada perro, pida ingresar su peso en kg.
3. Evalúa con if/elif/else:
- Perro pequeño (menos de 10 kg) -> Cuesta $2.000.
- Perro mediano (entre 10 y < 25 kg) -> Cuesta $4.000.
- Perro grande (25 kg o más) -> Cuesta $6.000.
4. Suma lo ganado en un acumulador total.
5. Al finalizar el ciclo, imprime "Resumen del día: Has paseado X perros ganando en total $Y".
"""
numero = 1
total = 0
Paseados = int(input("Cuantos perros paseaste hoy?"))
print("Por cada perro, tendras que decirme cual era su tamaño, para saber el pago para cada uno (Peso corporal en numeros enteros)")
print("Perro pequeño = $2000 (menos de 10 kg)")
print("Perro mediano = $4000 (entre 10 y < 25 kg)")
print("Perro grande = $6000 (25 kg o más)")
for x in range(Paseados):
    kg = int(input(f"Cual es el peso del perro {numero}? "))
    if kg < 10:
        print(f"Perro {numero} es pequeño")
        total = total + 2000
    elif kg < 25 and kg >= 10:
        print(f"Perro {numero} es mediano")
        total = total + 4000
    else:
        print(f"Perro {numero} es grande")
        total = total + 6000
    numero = numero + 1
print(f"Resumen del día: Has paseado {Paseados} perros ganando en total ${total}")