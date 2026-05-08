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
        if nivel in range(1,2):
            descuento = 0.2
        elif     
