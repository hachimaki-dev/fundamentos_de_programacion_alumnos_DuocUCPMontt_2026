contador = 0
bandera = True
while bandera == True :
    print(f"hola mundito vamos en el numero {contador}")
    contador = contador + 1
    if contador == 10 :
        break
        bandera = False
        print("entre en el if del while y cambie la bandera")
print("sali del ciclo")