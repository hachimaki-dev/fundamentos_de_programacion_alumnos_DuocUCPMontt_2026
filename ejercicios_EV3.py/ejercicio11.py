while True:
    try:
        numeros = int(input('Cantidad de paquetes que se van a despachar: '))
        if numeros > 0:
            break
        else:
            print('Error el numero deveser positivo entero')
    except ValueError:
        print('Error el numero deveser positivo entero')    

pesados = 0
normales = 0
peso_total = 0

for i in range(numeros):
    print('Paquetes', i + 1)

    while True:
        try: 
            peso = int(input('Peso en kg: '))
            if peso > 0:
                break
            else:
                print('Error el numero debe ser entero positivo')
        except ValueError:
            print('Error el numero debe ser entero positivo')   
    
    while True:
        codigo = input('Ingresa el codigo del paquete: ').strip()
        if len(codigo) >= 6 and ' ' not in codigo:
            break
        print('Tie ne que tener un minimo de 6 caracters')  

    peso_total += peso   
    if peso >= 20:
        print('carga pesada')
        pesados += 1
    else:
        print('Carga normal')
        normales += 1

print('---------')
print("Resumen del día ")
print("Carga pesada:", pesados, "paquetes")
print("Carga normal:", normales, "paquetes")
print("Peso total despachado:", peso_total, "kg")
