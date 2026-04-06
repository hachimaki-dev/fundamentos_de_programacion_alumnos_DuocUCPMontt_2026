Vida_jefe = 1000
print("Damos inicio al Gran jefe Marciano ")
while Vida_jefe > 0:
    print(f"\nVida actual del jefe: {Vida_jefe}")
    daño =int(input("Ingresa el daño de tu ataque: "))
    if daño < 0:
        print("El ataque ha fallado(con daño negativo dudo que logres matarlo crack)")
    else:
        Vida_jefe = Vida_jefe - daño
        if Vida_jefe > 0:
            print(f"Le has causado daño al jefe continua asi mira que le queda {Vida_jefe}")
print("¡Has acabado con el Gran Jefe Marciano! Eres una maquina de matar")