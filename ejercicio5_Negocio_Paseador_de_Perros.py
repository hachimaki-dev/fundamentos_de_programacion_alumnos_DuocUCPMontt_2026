total_perros = int(input("¿Cuántos perros paseaste hoy?: "))
total_ganado = 0
contador = 0

while contador < total_perros :
    peso = float(input(f"Ingrese el peso del perro {contador + 1} en kg: "))

    if peso < 10 :
        costo = 2000
    elif peso < 25 :
        costo = 4000
    else:
        costo = 6000

    total_ganado += costo
    contador += 1

print(f"Resumen del día: Has paseado {total_perros} perros ganado en total ${total_ganado}")