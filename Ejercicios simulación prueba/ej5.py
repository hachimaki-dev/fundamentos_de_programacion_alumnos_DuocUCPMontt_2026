#Inventario
hierbas = 0
frascos = 0
pociones = 0

#Oro disponible
oro = 500

#Bienvenida a la tienda
print("---Bienvenido/a alquimista---\n")
print("¿Qué deseas comprar?\n")
print("1) Hierba -------- $50 c/u")
print("2) Frasco -------- $100 c/u")
print("3) Fabricar poción -------- Requieres 2 hierbas y 1 frasco")
print("4) Salir")

#Momento de comprar
while True:
    
    opcion = int(input("\nIngrese su compra: "))
    
    if opcion == 4:
        print("\nMuchas gracias por su compra ¡Vuelva pronto!")
        break
    
    elif opcion == 1:
        
        #Se verifica el oro
        if oro >= 50:
            oro -=50
            hierbas +=1
            print(f"\nHas obtenido {hierbas} hierba(s)\nTu saldo actual es {oro} de oro")
            
        else:
            print(f"\nOro insuficiente\nTienes {oro} de oro")
            
    elif opcion == 2:
        
        #Se verifica el oro
        if oro >= 100:
            oro -= 100
            frascos += 1
            print(f"\nHas obtenido {frascos} frasco(s)\nTu saldo actual es {oro} de oro")
        else:
            print(f"\nOro insuficiente\nTienes {oro} de oro")
        
    elif opcion == 3:
        
        #Se verifica el material
        if hierbas >= 2 and frascos >= 1:
            hierbas -= 2
            frascos -= 1
            pociones += 1
            print(f"\n¡¡Has obtenido una poción de fuego!!")
        else:
            print("\nMaterial insuficiente")
    else:
        print("\nNo manejamos esa opción\n¿Deseas algo más alquimista?")

print(f"\nTu inventario actual es:\n{hierbas} hierbas\n{frascos} frascos\n{pociones} pociones de fuego")
print(f"\nTu saldo actual es {oro} de oro")
