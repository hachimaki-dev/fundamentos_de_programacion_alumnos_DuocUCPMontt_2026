import random
rango1=int(input('INGRESE UN NUMERO: '))
rango2=int(input('INGRESE OTRO NUMERO: '))
numerorandom=random.randint(rango1,rango2)
if numerorandom % 2 != 0:
    if numerorandom + 1 in range(rango1,rango2):
        numerorandom += 1
    else:
        numerorandom -=1
intentos = 0
while intentos < 3:
    adivanza=int(input('ADIVINA EL NUMERO SECRETO: '))
    if adivanza == numerorandom:
        print('ADIVINASTE FELICIDADES')
        break
    else:
        print('ups, ese no es')
        intentos +=1
    if intentos==1:
        if adivanza > numerorandom:
            print('EL NUMERO SECRETO ES MENOR AL ADMINASTRADO')
        elif adivanza < numerorandom:
            print('EL NUMERO SECRETO ES MAYOR AL ADMINISTRADO')
    if intentos==2:
        diferencia= abs(numerorandom - adivanza)
        print(f'ESTAS {diferencia} LEJOS DEL NUMERO CORRECTO')
    
    if intentos==3:
        print(f'Que mal, no pudiste adivinar\n El numero secreto era: {numerorandom}')                    

        
    
