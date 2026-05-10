membresia = 35000
casillero = 4500

opciones = [1,2,3,4]
while True:
    meses = int(input('Ingrese cantidad de meses de membresia: '))
    plan= int(input('Ingrese plan (Opciones 1,2,3 o 4)'))
    if plan not in opciones or meses < 1:
        print('Opcion invalida')
        continue
    if meses >= 12:
        if plan  == 1 or plan == 2:
            membresia -= membresia*0.22
        elif plan == 3 or plan == 4:
            membresia -= membresia*0.15
    elif 6 <= meses < 12:
        if plan  == 1 or plan == 2:
            membresia -= membresia*0.12
        elif plan == 3 or plan == 4:
            membresia -= membresia*0.07
    else:
        membresia=membresia
    if plan  == 1 or plan == 2:
        casillero -= casillero*0.15
        if meses >= 9:
            casillero -= casillero*0.05
            
        
    print(f'El valor de su membresia es: ${int(membresia)}\nEl precio de su casillero es: {int(casillero)}')
    break                            
