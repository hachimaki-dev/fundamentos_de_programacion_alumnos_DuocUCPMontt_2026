bandera = True
contador = 0
while bandera == True:
    print("Hola")
    contador = contador +1
    print(f"Contando en {contador}")
    if contador == 10:
        print(f"Estamos apunto de salir, la bandera es {bandera}")
        bandera = False

print(f"Estamos fuera y la bandera vale {bandera}")