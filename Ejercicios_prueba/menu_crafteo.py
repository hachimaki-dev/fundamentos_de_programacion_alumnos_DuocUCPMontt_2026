print("HAZ ENTRADO A TU MESA DE CRAFTEO")
while True:
    eleccion_usuario= input("QUE DESEAS CRAFTEAR? (1. PICO/2. ESPADA/3. SALIR): ")
    if eleccion_usuario == "1":
        print("PICO CRAFTEADO!")
        seguir_crafteando= input("DESEA CRAFTEAR ALGO MÁS? (SI/NO)").lower()
        if seguir_crafteando == "si":
            continue
        elif seguir_crafteando == "no":
            break
        else:
                print("INGRESA UNA OPCION VALIDA")
    elif eleccion_usuario == "2":
        print("ESPADA CRAFTEADA!") 
        seguir_crafteando= input("DESEAS CRAFTEAR ALGO MÁS? (SI/NO)").lower()
        if seguir_crafteando == "si":
            continue
        else:
            print("INGRESA UNA OPCION VALIDA")
            break
    elif eleccion_usuario == "3":
        print("SALIENDO DE LA MESA DE CRAFTEO")
        break
    else:
        print("INGRESE UNA OPCION VALIDA")
        continue


print("GRACIAS POR JUGAR")