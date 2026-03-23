contador = 0
bandera = True
while bandera == True:
    print(f"hola, vamos en el número {contador}")
    contador=contador+1
    if contador == 10:
        bandera = False
        print("entre en el if y cambie la bandera")
print("salio del ciclo")