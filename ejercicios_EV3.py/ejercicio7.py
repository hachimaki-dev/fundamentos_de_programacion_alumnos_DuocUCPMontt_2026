criticas = 0
normales = 0
bajas = 0
for c in range(5):
    temperatura = float(input(f'Ingresa la temperatura del sensor {c + 1}: '))
    if temperatura > 80:
        print('Alerta de temperatura')
        criticas += 1
    elif temperatura >= 50:
        print('Normal de temperatura')  
        normales += 1  
    else:
        print('Temperatura baja')    
        bajas +=1

print('Temperatura criticas: ', criticas)
print('Temperatura normales: ', normales)
print('Temperatura bajas: ', bajas )