usuario1=""
usuario2=""
puntaje_u1=0
puntaje_u2=0
print("Piedra , papel o tijera")
usuario1=input("Ingrese su opcion :")
usuario2=input("Ingrese su opcion :")

if usuario1=="tijera" and usuario2=="papel" : 
    print(f"Ha ganado el usuario 1 {puntaje_u1}")
    puntaje_2=puntaje_u1 + 1    
elif usuario1=="piedra" and usuario2=="papel" : 
    puntaje_u2=puntaje_u2 + 1 
    print(f"Ha ganado el usuario 2 {puntaje_u2}")
elif usuario1==""