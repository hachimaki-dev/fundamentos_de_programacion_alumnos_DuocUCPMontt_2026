cuenta_mensual = 45000
cargo_medicion = 6000
opciones = ['A','B','C','D']
while True:
    consumo = int(input('INGRESE SU CONSUMO EN kWh: '))
    tarifa = input('Ingrese su Tarifa (A,B,C,D)')
    if consumo < 0 or tarifa not in opciones:
        print('Opcion no valida')
        continue
    if consumo >= 500:
        if tarifa == 'A' or tarifa == 'B':
            cuenta_mensual = cuenta_mensual - cuenta_mensual*0.2
        elif tarifa == 'C' or tarifa == 'D':
            cuenta_mensual = cuenta_mensual - cuenta_mensual*0.14
    elif 499 >= consumo  >= 200:
        if tarifa == 'A' or tarifa == 'B':
            cuenta_mensual = cuenta_mensual - cuenta_mensual*0.12
        elif tarifa == 'C' or tarifa == 'D':
            cuenta_mensual = cuenta_mensual - cuenta_mensual*0.08
    elif consumo < 200:
        cuenta_mensual= cuenta_mensual
    #cargo de medicion
    if tarifa == 'A' or tarifa == 'B':
        if consumo >= 400:
            cargo_medicion = cargo_medicion - cargo_medicion*0.15
        else:
            cargo_medicion = cargo_medicion - cargo_medicion*0.1             
    print(f'Su cuenta mensual es ${int(cuenta_mensual)}') 
    print(f'Su cargo de medicion es ${int(cargo_medicion)}')
    break         

