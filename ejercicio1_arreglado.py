import time

espada_diamante = 1
pico_diamante = 2
salir = 3

print("¡Bienvenido a tu mesa de crafteo!")

while True:
    try:
        print("\n¿Qué quieres hacer?")
        print(f"{espada_diamante}. Craftear Espada de Diamante")
        print(f"{pico_diamante}. Craftear Picota de Diamante")
        print(f"{salir}. Salir de la mesa de crafteo")
        
        opcion = int(input("Elige tu opción: "))

        if opcion == 1:
            print("Crafteando...")
            time.sleep(2)    
            print("¡Has crafteado una espada de diamante!")
        
        elif opcion == 2:
            print("Crafteando...")
            time.sleep(2)
            print("¡Has crafteado una picota de diamante!")
            
        elif opcion == 3:
            print("SALIENDO DE LA MESA DE CRAFTEO...")
            break 
            
        else:
            print("Receta desconocida. Intenta nuevamente.")
            
    except ValueError:
        print("Error: Solo puedes ingresar números.")