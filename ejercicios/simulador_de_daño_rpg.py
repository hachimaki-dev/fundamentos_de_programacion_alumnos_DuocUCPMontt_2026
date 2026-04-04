jefe_final = 1000
daño = 0 
while jefe_final > 0:
    daño = int(input("ingrese daño de ataque:"))
    if daño < 0 :
        print("el ataque fallo")
        print(f"la vida del jefe es {jefe_final}")
    elif daño >= 0:
        jefe_final = jefe_final - daño
        if jefe_final < 0:
            jefe_final = 0
        print(f"le realizas un ataque, la vida del jefe es {jefe_final}")
        
else:
    jefe_final <= 0
    print("Felicidades derrotaste al jefe")

