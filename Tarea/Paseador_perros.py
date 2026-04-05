print("Paseador de perritos :)")
print("Descubre cuantos perritos paseaste y cuanto ganaste!")
Perritos_paseados = 0 
Perritos_paseados = int(input("¿Cuantos perritos has paseado en total el dia de hoy?: "))
Ganancia_perritos = 0 
contador = 0
total = 0  
for i in range (Perritos_paseados):
    peso = int(input("Ingresa el peso del perro en kg: "))
    if peso < 10:
        print("Perro pequeño: $2000")
        total = total + 2000
    elif peso < 25:
        print("Perro mediano: $4000")
        total = total + 4000
    else:
        print("Perro grande: $6000")
        total = total + 6000
contador = contador + 1
print(f"Resumen del dia: Has paseado {Perritos_paseados} perros ganando en total {total}")






#1. Pregunta al usuario cuántos perros paseó en total el día de hoy.
#2. Usa un ciclo para que, por cada perro, pida ingresar su peso en kg.
#3. Evalúa con if/elif/else:
#- Perro pequeño (menos de 10 kg) -> Cuesta $2.000.
#- Perro mediano (entre 10 y < 25 kg) -> Cuesta $4.000.
#- Perro grande (25 kg o más) -> Cuesta $6.000.
#4. Suma lo ganado en un acumulador total.
#5. Al finalizar el ciclo, imprime "Resumen del día: Has paseado X perros ganando en total $Y".