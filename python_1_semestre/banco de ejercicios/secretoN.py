""" Minijuego: El Número Secreto

Objetivo: Programar un juego clásico de interacción constante.

1. Guarda en una variable un número secreto (fijo, por ejemplo el 42).

2. Usa un while que se repita MIENTRAS la "respuesta del usuario" sea diferente 
(!=) al "número secreto".

3. Dentro del while: pide un número al usuario.
- Si el ingresado es menor al secreto, dile "El número secreto es más ALTO".
- Si el ingresado es mayor al secreto, dile "El número secreto es más BAJO".

4. Usa un contador para registrar en cuántos turnos logró adivinar.

5. Imprime al final "¡Ganaste en X intentos!"."""

respuesta_del_usuario = 0
contador = 0

while respuesta_del_usuario != 42:
    
    respuesta_del_usuario = int(input(" ingresa un numero: "))
    
    if respuesta_del_usuario > 42:
        print("el numero secreto es mas bajo")
        contador +=1
    
    elif respuesta_del_usuario < 42:
        print("el numero secreto es mas alto")
        contador +=1

    elif respuesta_del_usuario == 42:
        print(f"ganaste en {contador} intentos")