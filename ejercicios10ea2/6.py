from random import randint

limite_superior = int(input("ingrese liimte superior: "))
limite_inferior = int(input("ingrese limite inferior: "))

numero_generado = randint(limite_superior, limite_inferior)

if numero_generado % 2 != 0:
    if numero_generado + 1 <= limite_superior:
        numero_generado += 1
        
    else:
        numero_generado -= 1
        
intentos = 3

while intentos > 0:
    adivinar = int(input("intente adivinar: "))
    
    if adivinar == numero_generado:
        print("felicidades adivinaste a la primera")
        break
    
    else:
        if intentos == 3:
            if adivinar > numero_generado:
                print("el numero es menor")
                
            else:
                print("el numero es mayor")
                
        elif intentos == 2:
            if adivinar == numero_generado:
                print("felicidades adivinaste a la segunda")
                
            if adivinar > numero_generado:
                print("el numero es menor")
                
            else:
                print("el numero es menor")
                
                pista = "MAYOR" if adivinar > 5 else "MENOR"
                print(f"te doy una pista, es {pista} a 5")
                
        elif intentos == 1:
            print(f"fallaste el numero era {numero_generado}")
            
    intentos -= 1
                      
                      
        
                      
        
    
    
        