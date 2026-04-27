turnos = 0
ns = 60
nselec = int(input("Escoge un numero. "))
while nselec != ns:
    if nselec < ns:
        print("Te equivocaste, es un numero más alto.")

    else:
        print("Te equivocaste, es un numero más bajo.")
    nselec = int(input("Intenta con otro numero. "))
    turnos += 1

print(f"Ganaste en {turnos} intentos!")