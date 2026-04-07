import time
import sys

Frascos = 0
Hierbas = 0
cantidad_de_frascos = 0
cantidd_de_hierbas = 0
Monedas = 500
valor_frascos = 50
valor_hierba = 100
inventario = 0
pociones_hechas = 0

print ("/===========================/")
print ("/====Alquimista crafting====/")
print ("/===========================/\n")

print ("Eres un alquimista y tu proposito es crear 'Posiciones de Fuego' para ayudar en una gran guerra que se acerca.")
print ("Cuentas con una cantidad minima de recursos.")
print ("Y una presión muy grande.\n")
print ("¿Podrás crear las pociones a tiempo?\n")
time.sleep(2)

print ("CARGANDO OBJETIVOS...\n")
time.sleep(3)

print ("CARGANDO RECURSOS...\n")
time.sleep(3)

print ("CARGANDO MENÚ...\n")
time.sleep(3)

print ("==============================")
print ("========MENÚ DE INICIO========")
print ("==============================\n")

print ("1. Jugar. ")
print ("2. Opciones.")
print ("3. Salir.\n")

eleccion_de_usuario = int(input("¿Confirme su respuesta? : "))
print()

while True:
    if eleccion_de_usuario == 1:
        print("Indequenos cual sera su nombre para esta aventura.\n")
        Nombre_de_usuario = str(input("¿Qué nombre desea usar? : ")).lower()
        print()
        time.sleep(2)
        print (f"Gran alquimista {Nombre_de_usuario}, estamos bastante preocupados.")
        print ("Se acerca una gran guerra y no tenemos los recursos que necesitamos.")
        print ("Y por ello lo estabamos buscando.")
        print ("Necesitamos crear la maxima cantidad de pociones que usted puedad hacer.\n")
        print (f"-{Nombre_de_usuario}- 'Bien, yo me encaragare de esto.'")
        print (f"-{Nombre_de_usuario}- 'Solo esperenme aquí.'\n")
        

        print ("CAMINO A LA TIENDA...")
        time.sleep(4)

        print (f"-Maga de la tienda-  'Bienvenido alquimista {Nombre_de_usuario} cuenteme que esta buscando.'\n")

        print (f"-{Nombre_de_usuario}- 'Estoy en busca de unos frascos y hierbas.'\n")

        print ("-Maga de la tienda- 'Bien, se encuentran en el pasillo 4'\n")

        print ("CAMINO AL PASILLO 4...\n")
        time.sleep(2)

        print (f"-{Nombre_de_usuario}- 'UMH, estan bastante caros los productos, y yo solo cuento con ${Monedas}'.")
        print ("¿Debería comprarlas?")

        decision_de_usuario = str(input("¿Comprar productos? (SI/NO) : " )).lower()
        print()
        if decision_de_usuario == "si":
            print (f"-{Nombre_de_usuario}- 'Bien, vamos a ver que tal.'")
            print()
            time.sleep(2)
            print ("==================")
            print ("PRODUCTOS EN VENTA")
            print ("==================\n")

            print (f"1. Frascos (C/U) ${valor_frascos}.")
            print (f"2. Hierbas (C/U) ${valor_hierba}.")
            print (f"-{Nombre_de_usuario}- 'Umh, para crear una posción necesito maximo 2 de hierba y 1 frasco.'")
            print ("¿Cuántos debería llevarme?\n")
            print ()
        
        elif decision_de_usuario == "no":
            print ("Fin del juego. Tu acto de cobardia no es bienvenido aquí.")
            break

        else:
            print ("Ingrese solo (SI/NO).")

            while Monedas > 0:

                compras_de_frascos = int(input("¿Cuántos frascos vas a llevar? : "))
                print()
                print (f"-{Nombre_de_usuario}- 'Bien, creo que me llevare {compras_de_frascos} frascos.'\n")
                print (f"-{Nombre_de_usuario}- 'Bueno, ahora veamos cuantas hierbas me llevo.'\n")
                total_de_frascos = valor_frascos * compras_de_frascos
                cantidad_de_frascos = cantidad_de_frascos + compras_de_frascos
                

                compras_de_hierbas = int(input("¿Cuántas hierbas te vas a llevar? : "))
                print()
                print (f"-{Nombre_de_usuario}- 'Me llevare unas {compras_de_hierbas} hierbas.'")
                print (f"-{Nombre_de_usuario}- 'Ahora a pagar mis cosas.'\n")
                total_de_hierbas = valor_hierba * compras_de_hierbas
                cantidd_de_hierbas = cantidd_de_hierbas + compras_de_hierbas
                total_de_compras = total_de_frascos + total_de_hierbas

                if total_de_compras > Monedas :
                    print ("Saldo insuficiente, por favor vuelva a comprar.\n")

                    continue
                    
                Monedas -= total_de_compras

                print ("CAMINO AL CAJERO...")
                time.sleep(3)
                print ()
                print (f"-Maga de la tienda- 'Y bien, ya tienes todos tus productos {Nombre_de_usuario}'")
                print (f"-{Nombre_de_usuario}- 'Sí, ya tengo todo.'")
                print ("-Maga de la tienda- 'Excelente, ahora espere un momento que cuento todo.'\n")
                print()
                print ("COMPROBANDO COMPRAS...\n")
                time.sleep(3)
                print()
                print ("RESUMEN DE LAS COMPRAS.\n")
                print()
                print (f"Frascos : {compras_de_frascos} --> ${compras_de_frascos}.")
                print (f"Hierbas : {compras_de_hierbas} --> ${compras_de_hierbas}.\n")

                print (f"-Maga de la tienda- 'Bien, en total debes de pagar {total_de_compras}.'\n")
                print (f"-{Nombre_de_usuario}- 'bien, ahora lo pago...'\n")
                print()
                if Monedas == 0:
                    print ("Muchas, gracias que tenga un buen día.")
                    break
                elif Monedas > 0:
                    print (f"Muchas gracias, aquí tiene su vuelto {Monedas}.")
                    print ("Que tenga un buen día.")
                    break
            
            print ("SALIENDO DE LA TIENDA...")
            time.sleep(3)
        print ()
        print (f"-{Nombre_de_usuario}- 'Es momento de crear mis pociones.'")
        print ("Así que vamos caminando hacía mi zona de creación.\n")
        
        print ("DE CAMINO...\n")
        time.sleep(2)

        print (f"-{Nombre_de_usuario}- 'Ya he llegado, veamos que tenemos.'\n")
        inventario = cantidad_de_frascos + cantidd_de_hierbas

        print (f"-{Nombre_de_usuario}- 'Nada mal, cuento con {inventario} articulos creo que con esto sera suficiente.'")
        print (f"-{Nombre_de_usuario}- dentro de ellos tengo, {compras_de_frascos} frascos y {compras_de_hierbas} hierbas.")
        print (f"-{Nombre_de_usuario}- 'es mi momento de trabajar.'\n")

        print ("CARGANDO TERRENO...\n")
        time.sleep(3)
        print ("PONIENDO LOS ARTICULOS EN LA MESA...\n")
        time.sleep(3)

        print (f"-{Nombre_de_usuario}- 'Veamos que tal.' \n")

        while inventario >= 0:
            print ("¿desea frabricar los articulos? (SI/NO) \n")
            frabricar = str(input("Confirmar acción : ")).lower()
            if frabricar == "si":
                print ()
                print ("Ya veo, primero debo de moler las hierbas, luego encenderas y ponerlas en el frasco.")
                print ("Pan comido.\n")

                print ("FABRICANDO...")
                time.sleep(5)
                compras_de_frascos -= 1
                compras_de_hierbas -= 2
                inventario -= compras_de_hierbas and compras_de_frascos
                pociones_hechas += 1
                print()
                print ("Bien, termine mi primera poción\n")

                print (f"Articulos restantes {inventario}")
                print (f"Hierbas restantes {compras_de_hierbas}.")
                print (f"Frascos restantes {compras_de_frascos}.")

                if compras_de_frascos < 0:
                    print ("Te has quedado sin frascos.")
                    print (f"-{Nombre_de_usuario}- 'Maldición solo me alcanzo para {pociones_hechas} pociones.'")
                    print (f"-{Nombre_de_usuario}- 'Espero que con esto me alcance para ganar o si quiera eso.'\n")

                    print ("FIN DEL JUEGO...")
                    break

                elif compras_de_hierbas < 2 :
                    print (f"-{Nombre_de_usuario}- 'Maldición solo me alcanzo para {pociones_hechas} pociones.'")
                    print (f"-{Nombre_de_usuario}- 'Espero que con esto me alcance para ganar o si quiera eso.'\n")
                    print ("FIL DEL JUEGO...")
                    break

    elif eleccion_de_usuario == 2:
        print ("Opciones en mantención...")
        print ("Escoga otra opción.")
        if eleccion_de_usuario == 2:
            break

    elif eleccion_de_usuario == 3:
        break

    else:
        print ("Escoga solo 1, 2 y 3...")
    
print ("Muy cobarde de tu parte alquimista...")













    






