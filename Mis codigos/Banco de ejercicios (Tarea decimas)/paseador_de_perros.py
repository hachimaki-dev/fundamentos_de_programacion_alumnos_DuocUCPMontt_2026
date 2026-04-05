# Negocio: Paseador de Perros
# Objetivo: Control de ganancias de un negocio de servicios variables.

# 1. Pregunta al usuario cuántos perros paseó en total el día de hoy.
# 2. Usa un ciclo para que, por cada perro, pida ingresar su peso en kg.
# 3. Evalúa con if/elif/else:
#     - Perro pequeño (menos de 10 kg) -> Cuesta $2.000.
#     - Perro mediano (entre 10 y < 25 kg) -> Cuesta $4.000.
#     - Perro grande (25 kg o más) -> Cuesta $6.000.
# 4. Suma lo ganado en un acumulador total.
# 5. Al finalizar el ciclo, imprime "Resumen del día: Has paseado X perros ganando en total $Y".

print(" PASEADOR DE PERROS ".center(40, "-"))

perros_paseados = int(input("¿Cuantos perros paseo el dia de hoy? "))
numero_perro = 1
precio_paseo = 0
total = 0

while perros_paseados > 0:
    peso_perro = int(input(f"Ingrese el peso del perro {numero_perro}: "))

    while perros_paseados < 0:
        print("Error: Valor no puede ser negativo")
        perros_paseados = int(input(f"Ingrese el peso del perro {numero_perro}: "))

    if peso_perro < 10:
        precio_paseo = 2000
    elif peso_perro > 10 and peso_perro < 25:
        precio_paseo = 4000
    else:
        precio_paseo = 6000
    total = total + precio_paseo
    perros_paseados -= 1
    numero_perro += 1

if perros_paseados == 0:
    print(f"Resumen del día: Has paseado {numero_perro - 1} perros, ganando en total ${total}")
    
