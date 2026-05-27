from random import randint
while True:
    try:
        rango1= int(input('Ingrese un numero porfavor: '))
        break
    except ValueError:
        print("Valor no es combertible a numero")
    except:
        print("Otro Error")     
while True:
    try:
        rango2= int(input('Ingrese un numero mayor que el anterior porfavor: '))
        if rango2 <= rango1:
            raise Exception
        if rango2 > rango1:
            break
    except ValueError:
        print("Valor no es combertible a numero")
    except Exception:
        print('Numero no valido')
    except:
        print("Otro Error") 
    
        
        

numero= randint(rango1,rango2)
if numero%2 != 0:
    if numero + 1 in range(rango1,rango2):
        numero += 1
    else:
        numero -= 1

intentos=0

while intentos < 3:
    intentoadivinar1= int(input("Intente adivinar el numero secreto: "))
    if intentoadivinar1 == numero:
        print ('Felicidades has adivinado al primer intento')
        break
    else:
        print ('Lo siento, ese no es.')
        intentos += 1    
    if intentoadivinar1 > numero:
        print('Pista el numero secreto es menor al introducido en el intento 1')
    elif intentoadivinar1 < numero:
        print('Pista el numero secreto es mayor al introducido en el intento 1')    
    intentoadivinar2=int(input("Intente adivinar de nuevo: "))
    if intentoadivinar2 == numero:
        print ('Felicidades has adivinado al segundo intento')
        break
    else:
        print('Lo siento, eso tampoco es')
        intentos +=1
    print('Esta vez te dare dos pistas')
    if intentoadivinar2 > numero:
        print('Pista el numero secreto es menor al introducido en el intento 2')
    elif intentoadivinar2 < numero:
        print('Pista el numero secreto es mayor al introducido en el intento 2') 
    diferenciaintento1= abs(numero - intentoadivinar1)
    diferenciaintento2= abs(numero - intentoadivinar2)
    if diferenciaintento1 > diferenciaintento2:
        print(f'El numero que buscas está más cerca de {intentoadivinar2} que de {intentoadivinar1}')
    elif diferenciaintento1 < diferenciaintento2:
        print(f'El numero que buscas está más cerca de {intentoadivinar1} que de {intentoadivinar2}')
    elif diferenciaintento1 == diferenciaintento2:
        print(f'{intentoadivinar1} y {intentoadivinar2} estan igual de cerca al numero que buscas')
    intentoadivinar3=int(input("Intente adivinar por ultima vez: "))
    if intentoadivinar3==numero:
        print('Felicidades, has adivinado el numero secreto')
        break
    else:
        print('Lo siento, has perdido.')
        print(f'El numero secreto era: {numero}')
        intentos+=1                    