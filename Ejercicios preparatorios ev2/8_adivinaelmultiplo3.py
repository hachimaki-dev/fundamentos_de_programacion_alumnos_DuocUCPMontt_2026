import random
rango1=0
rango2=10
numerorandom=random.randint(rango1,rango2)
ajustado=(numerorandom//3)*3
if ajustado not in range(rango1,rango2):
    ajustado=rango1
numerorandom = ajustado
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

        
    
    
