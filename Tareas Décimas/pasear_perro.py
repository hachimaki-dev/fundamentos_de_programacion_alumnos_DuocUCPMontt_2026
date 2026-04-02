'''
1. Pregunta al usuario cuántos perros paseó en total el día de hoy.
2. Usa un ciclo para que, por cada perro, pida ingresar su peso en kg.
3. Evalúa con if/elif/else:
- Perro pequeño (menos de 10 kg) -> Cuesta $2.000.
- Perro mediano (entre 10 y < 25 kg) -> Cuesta $4.000.
- Perro grande (25 kg o más) -> Cuesta $6.000.
4. Suma lo ganado en un acumulador total.
5. Al finalizar el ciclo, imprime "Resumen del día: Has paseado X perros ganando en total $Y".
'''

dinero_ganado = 0

perros_paseados = int (input("¿Cuántos perros paseó en total el día de hoy? "))

for i in range(perros_paseados) :
    peso_en_kg = int (input("Ingrese el peso del perro (kg): "))

    if peso_en_kg < 10 :
        dinero_ganado += 2000
    elif peso_en_kg >= 10 and peso_en_kg < 25 :
        dinero_ganado += 4000
    else :
        dinero_ganado += 6000

print(f"Resumen del día: Has paseado {perros_paseados} perros ganando en total ${dinero_ganado}")