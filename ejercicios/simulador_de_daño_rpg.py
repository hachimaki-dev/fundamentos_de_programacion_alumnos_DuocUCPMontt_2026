jefe_final = 1000
daño = 0 
while jefe_final > 0:
    daño = int(input("ingrese daño de ataque:"))
    if daño < 0 :
        print("el ataque fallo")
        print(f"{jefe_final} vida del jefe")
    elif daño >= 0:
        print("le realizas un ataque")
        jefe_final = jefe_final - daño
        print(f"{jefe_final} punto de vida del jefe")
if jefe_final <= 0:
    print("Felicidades derrotaste al jefe")

