# continue: Saltar el turno
# A diferencia de break, continue NO termina el ciclo. Solo interrumpe la iteración *actual*, 
# ignora las instrucciones que queden abajo y regresa arriba para hacer la validación y seguir iterando.

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        continue # <--- Si es par, se lo salta y NO imprime
    print("Número impar válido:", numero)