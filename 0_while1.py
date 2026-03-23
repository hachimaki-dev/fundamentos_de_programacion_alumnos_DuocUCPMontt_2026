contador=0
bandera =True
while bandera == True :
    print(f"peo numero {contador}")
    contador=contador+1
    if contador == 10 :
        bandera = False
        print("estoy en bucle we pero cambio la bandera")
print("ya no estoy en bucle we")