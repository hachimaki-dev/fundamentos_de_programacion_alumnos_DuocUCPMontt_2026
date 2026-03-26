opcion_usuario1 = ""
opcion_usuario2 = ""

puntaje_usuario1 = 0
puntaje_usuario2 = 0

print("\n*************Bienvenido al cachipun extremo***************")
print("**********Por favor escriba la palabra piedra, papel o tijeras***********\n")

#otra opcion de while con bandera + if

while puntaje_usuario1 < 3 and puntaje_usuario2 < 3:

    opcion_usuario1 = input("J1 ingrese su eleccion: ")
    opcion_usuario2 = input("J2 ingrese su eleccion: ")

    if opcion_usuario1 == "piedra" and opcion_usuario2 == "papel":
        puntaje_usuario2 = puntaje_usuario2 + 1
        print("J2 suma una victoria")
        print(f"J2 tu puntaje actual es {puntaje_usuario2}")

    elif opcion_usuario1 == "piedra" and opcion_usuario2 == "tijeras" :
        puntaje_usuario1 = puntaje_usuario1 + 1
        print("J1 suma una victoria")
        print(f"J1 tu puntaje actual es {puntaje_usuario2}")

    elif opcion_usuario1 == "piedra" and opcion_usuario2 == "piedra" :
        print("Empate - vuelva a jugar")

# agregar opciones que faltan

if puntaje_usuario1 > puntaje_usuario2:
    print("gana el 1")
else :
    print("gana el 2")

print("gracias")

