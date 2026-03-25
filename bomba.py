
import random


errores = 0
maximo_de_errores = 5
combinacion = random.randint (1, 20)
menu = True
esta_jugando = True

while menu :
    print("Bienvenido a DESACTIVA LA BOMBA")

    print(".1 Jugar")
    print(".2 Reglas")
    print(".0 Cerrar juego")
    
    eleccion = int(input(""))


    if eleccion == 1 :

        menu = False
        
        while esta_jugando :
            eleccion_de_número = int(input("Elige el número que desactiva la bomba :v : "))
            if eleccion_de_número == combinacion :
                esta_jugando = False
                print("Felicidades la desactivaste y nos salvaste a todos :)))))))")
                
            else:
                errores = errores + 1
                print(f"Cuidado llevas {errores} error ")
            if errores >= maximo_de_errores: 
                esta_jugando = False

                print("BOOOOOOMMMMMMMMM")
                
