vida_jefe = 1000

while vida_jefe > 0:
    ataque = int(input("Ingresa la cantidad de daño de tu ataque (número entero): "))
    
    if ataque < 0:
        print("El ataque falló")
    else:
        vida_jefe = vida_jefe - ataque
        print(f"Ataque: {ataque}\nVida restante del jefe: {vida_jefe}\n")

print("¡Jefe derrotado!")
