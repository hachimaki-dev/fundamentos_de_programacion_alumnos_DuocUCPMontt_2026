"""Minijuego: El Número Secreto
Objetivo: Programar un juego clásico de interacción constante.

1. Guarda en una variable un número secreto (fijo, por ejemplo el 42).
2. Usa un while que se repita MIENTRAS la "respuesta del usuario" sea diferente (!=) al "número secreto".
3. Dentro del while: pide un número al usuario.
- Si el ingresado es menor al secreto, dile "El número secreto es más ALTO".
- Si el ingresado es mayor al secreto, dile "El número secreto es más BAJO".
4. Usa un contador para registrar en cuántos turnos logró adivinar.
5. Imprime al final "¡Ganaste en X intentos!".
"""
intentos = 1
numero = 23

while True:
    Respuesta = int(input("Achuntale a un numero aleatorio del 1 al 50  "))
    if Respuesta > 23:
        print("El número secreto es más BAJO")
        intentos = intentos + 1
    elif Respuesta < 23:
        print("El número secreto es más ALTO")
        intentos = intentos + 1
    else:
        print("Adivinaste")
        break
print(f"¡Ganaste en {intentos} intentos!")
    
    