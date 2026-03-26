opcion_usuario1 = ""
opcion_usuario2 = ""

puntaje_usuario1 = 0
puntaje_usuario2 = 0

print("bienvenido al cachipun" )
print("eliga la palabra piedra,papel o tijera")

opcion_usuario1 = print("j1- imgrese su eleccion ")
opcion_usuario2 = print("j2- imgrese su eleccion ")

if opcion_usuario1 == "piedra" and opcion_usuario2 == "papel" :
    puntaje_usuario2 = puntaje_usuario2 + 1
    print(f"j2 haz acupulado 1 victoria")
    print (f"j2 tu puntaje actual es {puntaje_usuario2}")

        
else opcion_usuario1 == "piedra" and opcion_usuario2 == "tijera" :
    puntaje_usuario1 = puntaje_usuario1 + 1
    print(f"j1haz acupulado 1 victoria")
    print (f"j1 tu puntaje actual es {puntaje_usuario1}")
      