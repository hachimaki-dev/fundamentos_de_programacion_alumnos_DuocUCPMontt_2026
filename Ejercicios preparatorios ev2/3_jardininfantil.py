mensualidad = 85000
kit= 18000
descuento = 0
while True:
    edad_niñx= int(input('Ingrese la edad del infante (en Meses)'))
    nivel=int(input('Ingrese el nivel del infante(Opciones 1,2,3 o 4): '))
    if edad_niñx < 0 or 1 > nivel > 4: 
        print('Opcion no valida')
        continue
    if edad_niñx <= 18:
        if nivel == 1 or nivel == 2:
            descuento = 0.2
        elif nivel == 3 or nivel == 4:
            descuento = 0.14
    elif 18 < edad_niñx  <= 36:
        if nivel == 1 or nivel == 2:
            descuento = 0.12
        elif nivel == 3 or nivel == 4:
            descuento = 0.07
  
    mensualidad = mensualidad - (mensualidad*descuento)
    # kit
    if nivel == 1 or nivel == 2:
        kit = kit - (kit*0.1)
        if edad_niñx <= 12:
            kit = kit - (kit*0.05)
        
    print(f'Su mensualidad es ${int(mensualidad)}') 
    print(f'El costo de los materiales es ${int(kit)}')
    break                     
            
                      
