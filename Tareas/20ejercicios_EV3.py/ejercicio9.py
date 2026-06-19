aprobado = 0
revicion = 0
rechazado = 0

for i in range(8):

    while True:
        try:
            score = int(input(f'Score de solicitud (0-1000) {i + 1}: '))
            if score >= 0 and score <= 1000:
                break
            else:
                print('Error el score debe estar entre 0 y 1000')
        except ValueError:
            print('Error ingresa un numero entero') 

    if score > 750:
        print('Aprovado automaticamente') 
        aprobado += 1
    elif score >= 500:                  
        print('Revición manual')
        revicion += 1
    else:
        print('Rechazado')   
        rechazado += 1
print('------------')  
print('Resumen') 
print('Aprovados automaticamente: ', aprobado)  
print('En revicion manual       : ', revicion) 
print('Rechazados               : ', rechazado)     