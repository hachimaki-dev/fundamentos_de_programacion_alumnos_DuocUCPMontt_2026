medicamentos = 60000
despacho = 8000
try:
    while True:
        edad = int(input("Ingrese su edad: "))

        tramo = input("Ingre su tramo (A,B,C o D):")
        
    if edad <= 30:
        if tramo == 'A' or tramo == 'B':
            medicamentos *= 0.82
        elif tramo == 'C' or tramo == 'D': 
            medicamentos *= 0.88
    elif 30 <= edad <= 60:
            if tramo == 'A' or tramo == 'B':
                medicamentos *= 0.88
            elif tramo == 'C' or tramo == 'D':
                medicamentos *= 0*92
            
    if tramo == 'A' or tramo == 'B':
        despacho *= 0.90
    if edad >= 55:
        despacho *= 0.95
    else:
        despacho = despacho
        

        
except:
    print("ingrese un numero valido")
        
    print(f"El valor de los medicamentos es {medicamentos}")
    print(f"El valor de despacho es {despacho}")
