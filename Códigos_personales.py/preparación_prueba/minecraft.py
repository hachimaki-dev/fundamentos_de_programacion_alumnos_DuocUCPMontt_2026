craftear_espada = 1
craftear_pico = 2
salir = 3
opcion = None
while True:
    print("__Menú mesa de crafteo__")
    print("( ingrese 3 para salir )")
    print("""_ Crafteos disponibles:_
          1.Espada de diamante 
          2.Pico de diamante""")
    opcion = int(input("Elija una opción"))
    if opcion == 1:
        print("Ha crafteado una espada de diamante")
    elif opcion == 2:
        print("Ha crafteado un pico de diamante")
    elif opcion == 3:
        print("menu cerrado")
        break
    else:
        print("ingrese una receta válida")
        continue