seleccion_menu = 0

print("Finalmente estas en tu hogar y abres tu mesa de crafteo para crear un par de cosas")
while True :
    seleccion_menu = int(input("¿Qué deseas craftear?: 1.- Espada De Diamante | 2.- Pico De Diamante | 3.- Salir del menú de crafteo"))
    
    if seleccion_menu == 1 :
        print("Espada de Diamante crafteada y agregada a tu inventario")
    elif seleccion_menu == 2 :
        print("Pico de Diamante crafteado y añadido a tu inventario")
    elif seleccion_menu == 3 :
        print("Decides no craftear nada y abandonas el menú")
        break
    else :
        print("Receta Inválida") 


