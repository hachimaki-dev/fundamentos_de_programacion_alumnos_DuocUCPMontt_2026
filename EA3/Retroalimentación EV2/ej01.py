#Variables pedidas en el ejercicio
medicamentos = 60000
despacho = 8000

#Se le pide información al usuario
edad_usuario = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo: ").upper()

#Reglas del descuento en medicamentos
if (edad_usuario <= 30) and (tramo == 'A' or tramo == 'B'):
    medicamentos = medicamentos * 0.82
    despacho = despacho * 0.9    #Reglas del despacho
elif (edad_usuario <= 30) and (tramo == 'C' or tramo == 'D'):
    medicamentos = medicamentos * 0.88
elif (31 <= edad_usuario <= 60) and (tramo == 'A' or tramo == 'B'):
    if edad_usuario >= 55 and edad_usuario <= 60:
        medicamentos = medicamentos * 0.88
        despacho = despacho * 0.85    #Reglas del despacho si la edad del usuario es >= 55
    else:
        medicamentos = medicamentos * 0.82
        despacho = despacho * 0.9    #Reglas del despacho
elif (31 <= edad_usuario <= 60) and (tramo == 'C' or tramo == 'D'):
    medicamentos = medicamentos * 0.92

print(f"El valor de medicamentos es: ${medicamentos}")
print(f"El valor del espacho es: ${despacho}")