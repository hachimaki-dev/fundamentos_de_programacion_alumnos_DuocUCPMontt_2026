total_perros = int(input("¿Cuántos perros paseaste hoy en total? "))

ganancia_total = 0

for i in range(1, total_perros + 1):
    peso = float(input(f"Ingresa el peso del perro #{i} (kg): "))
    
    if peso < 10:
        costo = 2000
    elif 10 <= peso < 25:
        costo = 4000
    else:
        costo = 6000
        
    ganancia_total += costo

print(f"\nResumen del día: Has paseado {total_perros} perros ganando en total ${ganancia_total}")


