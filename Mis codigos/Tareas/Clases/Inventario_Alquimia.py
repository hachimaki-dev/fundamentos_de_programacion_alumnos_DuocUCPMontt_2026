hierbas = 50
frascos = 100
monedas_de_oro = 500
hierbas_compradas = 0
frascos_comprados = 0
pociones_fuego = 0
print("--BIENVENIDO A LA MESA DE ALQUIMIA--")
while True:
    opcion = input("Necesitas 1).Comprar / 2).Utilizar de Alquimia / 3).Salir de la Tienda")
    if opcion == "1":
        print("BIENVENIDO A LA TIENDITA KAWAII")
        print("")
        print("1) Comprar Hierba ($50 c/u)")
        print("2) Comprar Frasco ($100 c/u)")
        print("3) Salir de Tienda")
        
        opcion_tienda = input("")
        while opcion_tienda != "1" and opcion_tienda != "2" and opcion_tienda != "3":
            opcion_tienda = input("Ingrese nùmero vàlido")
        
        while opcion_tienda == "1" and monedas_de_oro < frascos: 
            opcion_tienda = print("No tienes suficiente dinero")
            opcion_tienda = 0
        
        while opcion_tienda == "2" and monedas_de_oro < hierbas:
            print("No tienes dinero suficiente")
            opcion_tienda = 0

        if opcion_tienda == "1" and monedas_de_oro >= hierbas:
            hierbas_compradas = hierbas_compradas + 1 
            monedas_de_oro = monedas_de_oro - hierbas
            print(f"Ahora tienes {hierbas_compradas} hierbas")
            print("")

        elif opcion_tienda == "2" and monedas_de_oro >= frascos:
            frascos_comprados = frascos_comprados + 1
            monedas_de_oro = monedas_de_oro - frascos  
            print(f"Ahora tienes {frascos_comprados} frascos")
            print("")
     
        
        
    elif opcion == "2":
        if hierbas_compradas >= 2 and frascos_comprados >= 1:
            pociones_fuego = pociones_fuego + 1
            print("Haz fabricado una pociòn de Fuego")
            seguir_pociones = input("¿Quieres seguir haciendo pociones?").lower()
            if seguir_pociones == "si":
                print()
            elif seguir_pociones == "no":
                print(f"cantidad total de pociones{pociones_fuego}")
                print("Saliste de la mesa de alquimia")
                break
        else:
            print("Materiales insuficientes")
    
    elif opcion == "3":
        print("Saliste")
        break   


    
