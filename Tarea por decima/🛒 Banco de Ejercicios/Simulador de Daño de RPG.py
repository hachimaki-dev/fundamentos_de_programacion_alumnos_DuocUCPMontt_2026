#Simulador de Daño de RPG
#Objetivo: Crear un pequeño simulador de un combate de rol (RPG).

#1. El jefe final tiene 1000 puntos de vida iniciales.
#2. Usa un ciclo while que se repita mientras la vida del jefe sea mayor que 0.
#3. Dentro del ciclo, pide al usuario ingresar el daño del ataque (entero).
#4. Si el daño es menor a 0, muestra un mensaje "El ataque falló" y no restes vida.
#5. Si el daño es mayor o igual a 0, réstalo de la vida del jefe y muestra la vida restante.
#6. Si la vida es 0 o menos, rompe el ciclo o deja que termine naturalmente, y muestra "¡Jefe derrotado!". 

jefe_final = 1000
daño_del_ataque = 0

print("¨****Bienvenidos al simulador de daño de RPG****")

while jefe_final > 0:
    daño_del_ataque = int(input("Ingrese el daño del ataque: "))
    if daño_del_ataque <= 0:  
      print("El ataque falló")
    elif daño_del_ataque > jefe_final:
       print("El jefe final esquivo el ataque")
    elif daño_del_ataque >= 0:
      jefe_final = jefe_final - daño_del_ataque
      print(f"La vida restante del jefe final es de {jefe_final} puntos")
    else:
       jefe_final <= 0
       break
    
print("¡Jefe Derrotado!")