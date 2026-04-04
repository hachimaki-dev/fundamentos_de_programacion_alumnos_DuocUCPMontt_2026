#1. El jefe final tiene 1000 puntos de vida iniciales.
#2. Usa un ciclo while que se repita mientras la vida del jefe sea mayor que 0.
#3. Dentro del ciclo, pide al usuario ingresar el daño del ataque (entero).
#4. Si el daño es menor a 0, muestra un mensaje "El ataque falló" y no restes vida.
#5. Si el daño es mayor o igual a 0, réstalo de la vida del jefe y muestra la vida restante.
#6. Si la vida es 0 o menos, rompe el ciclo o deja que termine naturalmente, y muestra "¡Jefe derrotado!".

jefe_final = 1000 
daño_de_ataque = 0

while jefe_final > 0 :
    daño_de_ataque = int(input("ingrese daño"))
    if daño_de_ataque < 0 :
        print(f"ataque fallido, la vida del jefe final es {jefe_final}")
    elif daño_de_ataque >= 0 :
        jefe_final = jefe_final - daño_de_ataque
        if jefe_final < 0:
            jefe_final = 0
        print(f"la vida del jefe es {jefe_final}")
print("jefe derrotado!")
        

