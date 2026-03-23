contador = 0 
Pokebandero = True
while Pokebandero == True :
    print(f"Hola causita vamos en el numero {contador}")
    contador = contador + 1
    if contador == 10 :
        Pokebandero = False
        print("Entre en el if del while cambie la Pokebandero")

print("Sali del ciclo")