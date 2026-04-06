print("Bienvenido a la calculadora de gastos")

almuerzo= 0
contadorfotocopias = 0
valorfotocopias = 0
contadordedias = 0
dia = ""
valortotalfotocopias = 0
valortotalalmuerzo = 0

if contadordedias == 0:
    dia = "Lunes"
elif contadordedias == 1:
    dia = "Martes"
elif contadordedias == 2:
    dia = "Miercoles"  
elif contadordedias == 3:
    dia = "Jueves"
elif contadordedias == 4: 
    dia = "Viernes"                 

while contadordedias < 5:
    if contadordedias == 0:
        dia = "Lunes"
    elif contadordedias == 1:
        dia = "Martes"
    elif contadordedias == 2:
        dia = "Miercoles"  
    elif contadordedias == 3:
        dia = "Jueves"
    elif contadordedias == 4: 
        dia = "Viernes"      
    print(dia)
    valorfotocopias = 0
    fotocopias = 0
    contadorfotocopias = 0
    almuerzo = int(input("Ingrese cuanto dinero gasto en su Almuerzo: "))
    fotocopias =int(input("Ingrese cuantas fotocopias utiliza el dia de hoy: "))
    
    while contadorfotocopias < fotocopias:
        valorfotocopias = valorfotocopias + 50
        contadorfotocopias += 1
    
    print (f"Dinero gastado en fotocopias el {dia} = ${valorfotocopias}")
    
    valortotalalmuerzo = valortotalalmuerzo + almuerzo
    valortotalfotocopias = valortotalfotocopias + valorfotocopias
    
    contadordedias += 1   

print(f"Valor total fotocopias ${valortotalfotocopias}")
print(f"Valor total almuerzo ${valortotalalmuerzo}")

 

valortotalsemanal = valortotalalmuerzo + valortotalfotocopias
print (f"Presupuesto semanal = ${valortotalsemanal}")
if valortotalsemanal > 20000:
        print ("Presupuesto semanal muy alto :c")
else:
      print ("Presupuesto semanal moderado c:")
