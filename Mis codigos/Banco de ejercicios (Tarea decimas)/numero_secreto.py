# Minijuego: El Número Secreto
# Objetivo: Programar un juego clásico de interacción constante.

# 1. Guarda en una variable un número secreto (fijo, por ejemplo el 42).
# 2. Usa un while que se repita MIENTRAS la "respuesta del usuario" sea diferente (!=) al "número secreto".
# 3. Dentro del while: pide un número al usuario.
# - Si el ingresado es menor al secreto, dile "El número secreto es más ALTO".
# - Si el ingresado es mayor al secreto, dile "El número secreto es más BAJO".
# 4. Usa un contador para registrar en cuántos turnos logró adivinar.
# 5. Imprime al final "¡Ganaste en X intentos!".

print(" EL NUMERO SECRETO ".center(40, "-"))

numero_secreto = 3
numero_usuario = 0
intentos = 0

while numero_usuario != numero_secreto:
    numero_usuario = int(input("\nAdivine el numero secreto: "))
    intentos = intentos + 1
    if numero_usuario < numero_secreto:
        print("El número secreto es más ALTO") 
    if numero_usuario > numero_secreto:
        print("El número secreto es más BAJO")

print(f"\n¡Felicidades, era el numero {numero_secreto}!")
print(f"¡Ganaste en {intentos} intentos!")