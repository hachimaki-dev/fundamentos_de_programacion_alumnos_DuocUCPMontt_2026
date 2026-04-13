import time
espada_diamante = 1
pico_diamante = 2
salir = 3
    
print("¡Bienvenido a tu mesa de crafteo!")

while True:
    try:
        
        print("¿Que quieres hacer?")
        print(f"Craftear Espada de Diamante: {espada_diamante}")
        print(f"Craftear Picota de Diamante: {pico_diamante}")
        print(f"Salir de la mesa de crafteo: {salir}")
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
            print("SALIENDO DE LA MESA DE CRAFTEO.")
            break

    
        else:
            print("Receta desconocida. Intenta nuevamente.")
        
    except ValueError:
        print("Solo puedes ingresar numeros.")
        
    