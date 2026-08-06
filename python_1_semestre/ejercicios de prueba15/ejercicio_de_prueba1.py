"""Objetivo: Crear un pequeño simulador de un combate de rol (RPG).

1. El jefe final tiene 1000 puntos de vida iniciales.
2. Usa un ciclo while que se repita mientras la vida del jefe sea mayor que 0.
3. Dentro del ciclo, pide al usuario ingresar el daño del ataque (entero).
4. Si el daño es menor a 0, muestra un mensaje "El ataque falló" y no restes vida.
5. Si el daño es mayor o igual a 0, réstalo de la vida del jefe y muestra la vida restante.
6. Si la vida es 0 o menos, rompe el ciclo o deja que termine naturalmente, y muestra "¡Jefe derrotado!".       >) y menor que (< {} """ 

jefe_final = 1000 
daño_de_ataque_al_mounstro = 0 
vida = 100

while jefe_final > 0:
    daño_de_ataque_al_mounstro = int(input(" daño de ataque al mounstro: "))
    if daño_de_ataque_al_mounstro < 0:
        print ("el ataque fallo")
        
    elif daño_de_ataque_al_mounstro >= 0:
        jefe_final = jefe_final - daño_de_ataque_al_mounstro
        print(f"vida del mounstro",jefe_final)
    
    elif jefe_final < 0: 
        break
print("jefe derrotado")
