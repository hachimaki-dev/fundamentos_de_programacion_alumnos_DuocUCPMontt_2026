#1. El jefe final tiene 1000 puntos de vida iniciales.
#2. Usa un ciclo while que se repita mientras la vida del jefe sea mayor que 0.
#3. Dentro del ciclo, pide al usuario ingresar el daño del ataque (entero).
#4. Si el daño es menor a 0, muestra un mensaje "El ataque falló" y no restes vida.
#5. Si el daño es mayor o igual a 0, réstalo de la vida del jefe y muestra la vida restante.
#6. Si la vida es 0 o menos, rompe el ciclo o deja que termine naturalmente, y muestra "¡Jefe derrotado!".

vida_jefe = 1000

while vida_jefe > 0:
    daño_ingresado = int(input("Ingrese el daño: "))
    if daño_ingresado >= 0:
        vida_jefe = vida_jefe - daño_ingresado
        print(f"inflingiste {daño_ingresado} puntos de daño")
        print(f"el jefe ahora tiene {vida_jefe} puntos de vida")
    else:
        print("el ataque fallo")
print("el jefe ha sido derrotado")