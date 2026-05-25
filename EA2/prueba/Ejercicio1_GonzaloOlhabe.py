medicamentos=60000
despacho=8000

while True:
    edad=int(input("Ingrese su edad: "))
    if edad >= 0:
        break
    else:
        print('Opción Invalida')

while True:
    tramo=input('Ingrese su tramo: (A,B,C o D)')
    if tramo in ['A','B','C','D']:
        break
    else:
        print('Opcion Invalida')

if edad <= 30:
    if tramo == 'A' or tramo == 'B':
        medicamentos -= medicamentos*0.18
    elif tramo == 'C' or tramo == 'D':
        medicamentos -= medicamentos*0.12

elif 31 <= edad <= 60:
    if tramo == 'A' or tramo == 'B':
        medicamentos -= medicamentos*0.12
    elif tramo == 'C' or tramo == 'D':
        medicamentos -= medicamentos*0.08


#despacho
if tramo == 'A' or tramo == 'B':
    despacho -= despacho*0.1
    if edad >= 55:
        despacho -= despacho*0.05

print(f'El valor de medicamentos es ${int(medicamentos)}')
print(f'El valor de despacho es {int(despacho)}')        
        