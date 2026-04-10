print("selecciona que deseas hacer en la Mesa de Crafteo")



while True:
    print ("1. Craftear Espada de Diamante")
    print ("2. Craftear Pico")
    print ("3. Salir de la Mesa de Crafteo")
    
    opcion_de_crafteo = int(input("¿Que deseas hacer?"))
    if opcion_de_crafteo == 1:
        print ("¡Espada Crafteada!")
    
    elif opcion_de_crafteo == 2:
        print ("¡Pico Listo!")
        
    elif opcion_de_crafteo != 1 and opcion_de_crafteo != 2 and opcion_de_crafteo != 3:
        print("Receta desconocida. Intenta nuevamente.")
        continue
    
    elif opcion_de_crafteo == 3:
        print ("Ha Salida de la mesa de Crafteo")
        break
    
 
        