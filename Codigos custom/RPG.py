"""
Simulador de Daño de RPG
Objetivo: Crear un pequeño simulador de un combate de rol (RPG).

1. El jefe final tiene 1000 puntos de vida iniciales.
2. Usa un ciclo while que se repita mientras la vida del jefe sea mayor que 0.
3. Dentro del ciclo, pide al usuario ingresar el daño del ataque (entero).
4. Si el daño es menor a 0, muestra un mensaje "El ataque falló" y no restes vida.
5. Si el daño es mayor o igual a 0, réstalo de la vida del jefe y muestra la vida restante.
6. Si la vida es 0 o menos, rompe el ciclo o deja que termine naturalmente, y muestra "¡Jefe derrotado!".
"""



Boss = 1000

while Boss > 0:
    Daño = int(input("Cuanto daño quieres hacerle al jefe?"))
    if Daño < 0:
        print("El ataque fallo")
    elif Daño >= 0:
        Boss = Boss - Daño
        print(f"Vida del jefe es {Boss}")
print("¡Jefe derrotado!")