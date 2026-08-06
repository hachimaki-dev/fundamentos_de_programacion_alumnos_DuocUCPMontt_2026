contador=0
bandera=True
while bandera==True:
    print(f"Hola mundito vamos en el numero{contador}")
    contador=contador+1
    if contador==10:
        bandera=False
        print("Entre em el if de while y cambie la bandera")

print("Sali del ciclo")