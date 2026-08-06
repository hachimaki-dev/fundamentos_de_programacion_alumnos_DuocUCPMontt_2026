#1. El jefe final tiene 1000 puntos de vida iniciales.
#2. Usa un ciclo while que se repita mientras la vida del jefe sea mayor que 0.
#3. Dentro del ciclo, pide al usuario ingresar el daño del ataque (entero).
#4. Si el daño es menor a 0, muestra un mensaje "El ataque falló" y no restes vida.
#5. Si el daño es mayor o igual a 0, réstalo de la vida del jefe y muestra la vida restante.
#6. Si la vida es 0 o menos, rompe el ciclo o deja que termine naturalmente, y muestra "¡Jefe derrotado!".
jefe = 1000 

while jefe > 0:
    ataque = int(input("ingrese ataque: "))
    if ataque < 0:
        print("el ataque fallo")
    elif ataque > 0:
        jefe = jefe - ataque
        print(f"el jefe tiene {jefe} de vida ")
print("jefe derrotado")