codigos = []
turno_extra = 0
turno_normal = 0

while True:
    try:
        enfermeras = int(input("Ingrese el numero de enfermeras que se registraran: "))
        if enfermeras > 0:
            break
        else:
            print("Tiene que ser mayor a cero")
    except ValueError:
        print("Tiene que ser un numero")
        
for i in range (enfermeras):
    while True:
        codigo_enfermera = input("Ingrese codigo: ")
        if len(codigo_enfermera) >= 6 and not " " in codigo_enfermera:
            codigos.append(codigo_enfermera)
            break
        else:
            print("codigo no valido debe tener como minimo 6 caracteres y sin espacios")
    while True:
        try:
            turno =int(input("Ingrese sus horas de turno: "))
            if turno > 0:
                if turno > 40:
                    turno_extra+=1
                    break
                else:
                    turno_normal+=1
                    break
                
            else:
                print("Tiene que ser mayor a 0")            
        except ValueError:
            print("Tiene que ser un numero")    
            
print(f"El hospital registro {turno_extra} enfermeras en turno entra y {turno_normal} en turno normal. Registro completo")    
                     
            