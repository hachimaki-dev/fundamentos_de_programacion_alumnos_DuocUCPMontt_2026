import random


"""tragamonedas().     [ ]"""
dinero = int(input("ingrese dinero a jugar:"))

print(f"tienes {dinero} disponible")

print("BLACKJACK press s to continue ")

desicion_de_jugar1 = input("quieres jugar ?:")


while desicion_de_jugar1 == "s":
    print("BIENVENIDO AL BLACKJACK\n las reglas son:\n 1.el numero mas cercano a 21 gana\n 2.si te pasa de 21 pierdes\n 3.si superas la mano de la casa ganas\n DISFRUTA C:")
    print(" apreta (s) para si\n apreta (n) para no")
    desicion_de_jugar = input("quires  continuar ?:")
    
    if desicion_de_jugar == "s":
        print(f"tienes tanto {dinero}, para apostar")
        dinero_a_jugar  = int(input("cuanto apuestas ?"))
        
        
        if dinero_a_jugar <= dinero and dinero_a_jugar > 0:
        
            carta1casa = random.randint(1,13)
            carta2casa = random.randint(1,13) 

            carta1 = random.randint(1,13) 
            carta2 = random.randint(1,13)
        
            cartas1y2 = carta1 + carta2
            cartacasa1y2 = carta1casa + carta2casa 
        
            print(f" carta 1 casa: {carta1casa}")
            print(f" carta 2 casa: {carta2casa}")
            print(f" la casa tiene: {cartacasa1y2}") 
        
            print(f" tu carta 1: {carta1}")  
            print(f" tu carta 2: {carta2}")
            print(f" tienes: {cartas1y2}")

        
            if cartacasa1y2 >21 and cartas1y2 <= 21:
                print("la casa pierde. tu Ganas")
                dinero = dinero + dinero_a_jugar 
                print(f"te quedas con {dinero}")
                break
                
            
            elif cartas1y2 >21:
                print("perdiste")
                dinero = dinero - dinero_a_jugar
                print(f"te quedas con:{dinero}")
                break
            
            elif cartas1y2 > 21 and cartacasa1y2 > 21:
                print("empate")
                print(f"te quedas con: {dinero}")
                break
        
            elif cartas1y2 > cartacasa1y2 and cartas1y2 <= 21:
                dinero = dinero_a_jugar + dinero
                print(f"te quedas con:{dinero}")
                print("Ganaste")
                break
        
            elif cartas1y2 < cartacasa1y2 and cartas1y2 <=21:
                print("perdiste")
                dinero = dinero - dinero_a_jugar
                print(f"te quedas con: {dinero}")
                break
        
            elif cartas1y2 == cartacasa1y2:
                print(f"te quedas con: {dinero}")
                print("VAYA EMPATE")
                break

            elif cartas1y2 < 21 and cartas1y2 < cartacasa1y2:
            
                print(" apreta: (s) para otra carta  o  apreta: (n) para jugar " )
            
                desicion  = input("una carta mas o juegas ?:")
            
                if desicion == "s":
                    #joker = 1
                    carta3 = random.randint(1,13)

                    carta123 = cartas1y2 + carta3
                    print(f" tienes un total de: {carta123}") 
    
                    if carta123 >=  21 and carta123 > cartacasa1y2:
                        print("ganaste")
                        dinero = dinero + dinero_a_jugar
                        print(f"te quedas con: {dinero}")
                        break
            
                    elif carta123 < 21 and carta123 < cartacasa1y2:
                        print("perdiste")
                        dinero = dinero + dinero_a_jugar
                        print(f"te quedas con: {dinero}")
                        break
                    else:
                        print("perdiste")
                        dinero = dinero - dinero_a_jugar
                        print(f"te quedas con: {dinero}")
                        break
                
    
                elif desicion == "n":
                    continue
        else:
            print("no valido")     
            continue
    elif desicion_de_jugar == "n":
        print("es una pena adios ")
        break

    else:
        print("no valido empieza de nuevo")
        continue         
        