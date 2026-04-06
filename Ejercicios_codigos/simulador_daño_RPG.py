print("Intenta derrotar al jefe")
print("ATAQUES: Ataque1, Ataque2, Ataque3, Ataque4")
ataque= input("selecciona tu ataque ").lower()

vida_jefe= 1000

while vida_jefe > 0:
    if ataque == "ataque1":
        vida_jefe= vida_jefe - 100
        print("Vamos, tu puedes")
        print(vida_jefe)
    elif ataque == "ataque2":
        vida_jefe= vida_jefe - 50
        print("Vamos, tu puedes")
        print(vida_jefe)
    else:
        vida_jefe= vida_jefe - 25
        print("Vamos, tu puedes")
        print(vida_jefe)



print("FELICIDADES, LO LOGRASTE!!")