"""Objetivo: Control de ganancias de un negocio de servicios variables.

1. Pregunta al usuario cuántos perros paseó en total el día de hoy.
2. Usa un ciclo para que, por cada perro, pida ingresar su peso en kg.
3. Evalúa con if/elif/else:
- Perro pequeño (menos de 10 kg) -> Cuesta $2.000.
- Perro mediano (entre 10 y < 25 kg) -> Cuesta $4.000.
- Perro grande (25 kg o más) -> Cuesta $6.000.
4. Suma lo ganado en un acumulador total.
5. Al finalizar el ciclo, imprime "Resumen del día: Has paseado X perros ganando en total $Y".  >) y menor que (< {}   

while True:
    cantidad_perros = int(input("¿Cuántos perros paseaste el día de hoy?: "))
    
    total_dia = 0 # Aquí acumularemos la ganancia de todos los perros
    contador = 0  # Para controlar cuántos pesos hemos pedido

    # Este bucle pedirá el peso para cada perro paseado
    while contador < cantidad_perros:
        peso_perro = int(input(f"Ingresa el peso del perro {contador + 1} en kg: "))
        
        # Lógica de precios usando solo if/elif
        if peso_perro < 10:
            valor = 2000
        elif peso_perro >= 10 and peso_perro <= 25:
            valor = 4000
        elif peso_perro > 25:
            valor = 6000
        
        # Sumamos el valor de este perro al total del día
        total_dia = total_dia + valor
        
        # Aumentamos el contador para no quedarnos en un bucle infinito
        contador = contador + 1

    print(f"Resumen del día: Has paseado {cantidad_perros} perros y has ganado en total {total_dia}")

    # Preguntamos si quiere cerrar el programa
    termino = input("¿Quieres registrar otro día? (si/no): ")
    if termino == "no" or termino == "No":
        break"""  

perro = 0
peso_perro = 0
contador = 0 
total_dia = 0
valor = 0

while True:
    perro = int(input("cuantos perros paseaste el dia de hoy ?: "))

    while contador <  perro:
        peso_perro = int(input(f"ingresa el peso del perro {contador + 1} en kilogramos:  "))
        
        if peso_perro < 10:
            valor = 2000
    
        elif peso_perro  >= 10 and peso_perro <= 25:
            valor = 4000
        
        elif peso_perro >= 25:
            valor = 6000
        
        total_dia = total_dia + valor 
        contador = contador +1
    
    print(f"resumen del dia: has paseado {perro}   y has ganado en total  {total_dia} ")
    break