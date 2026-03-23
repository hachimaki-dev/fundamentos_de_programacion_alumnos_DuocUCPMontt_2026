print("=== BOSQUE MÍNIMO ===")
print("Te despiertas en un bosque misterioso.")
print("Hay dos caminos.\n")

print("1) Camino claro")
print("2) Camino oscuro\n")
c = input("Elige (1/2): ")

if c == "1":
    print("\nEl camino claro te lleva a un cofre.")
    print("1) Abrir")
    print("2) Ignorar\n")
    x = input("Elige (1/2): ")

    if x == "1":
        print("\nDentro hay una llave mágica.")
        print("Encuentras una puerta y escapas.")
        print("¡GANASTE!")
    elif x == "2":
        print("\nTe pierdes entre los árboles.")
        print("FINAL: Atrapado para siempre.")
    else:
        print("\nDudas demasiado.")
        print("El bosque te consume.")
elif c == "2":
    print("\nUna figura aparece entre las sombras.")
    print("1) Hablar")
    print("2) Correr\n")
    y = input("Elige (1/2): ")

    if y == "1":
        print("\nLa figura te ofrece poder o libertad.")
        print("1) Libertad")
        print("2) Poder\n")
        z = input("Elige (1/2): ")

        if z == "1":
            print("\nApareces fuera del bosque.")
            print("¡GANASTE!")
        elif z == "2":
            print("\nTe conviertes en guardián del bosque.")
            print("FINAL: Poder sin salida.")
        else:
            print("\nNo respondes.")
            print("Te transformas en árbol.")
    elif y == "2":
        print("\nTropiezas y caes por un barranco.")
        print("FINAL: Fin abrupto.")
    else:
        print("\nNo decides.")
        print("La figura te atrapa.")
else:
    print("\nNo eliges nada.")
    print("La noche cae y desapareces.")
       