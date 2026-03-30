opcion_usuario1 = ""
opcion_usuario2 = ""

puntaje_usuario1 = 0
puntaje_usuario2 = 0

print("B i e n v e n i d o  a l  c a c h i p u n ")
print("por favor elija una  opcion piedra , papel , tijera ")

opcion_usuario1 = input("usuario 1 - por favor elija una opcion")

opcion_usuario2 = input("usuario 2 - por favor elija una opcion")

if opcion_usuario1 == "piedra" and opcion_usuario2 == "papel" :
    puntaje_usuario2 = puntaje_usuario2 + 1
    print(f"usuario 2 haz acumulado 1 victoria")
    print(f"usuario 2 tu puntaje actual es {puntaje_usuario2}")
    