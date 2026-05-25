medicamentos = 60000
despacho_domicilio = 8000

tramo = str(input("Ingrese su tramo: "))
edad = int(input("Ingrese su edad: "))

if edad <= 30:
    if tramo == "A" or tramo == "B":
        descuento_edad = medicamentos * 0.18
    
    elif tramo == "C" or tramo == "D":
        descuento_edad = medicamentos * 0.12
        
elif 31 <= edad <= 60:
    if tramo == "A" or tramo == "B":
        descuento_edad = medicamentos * 0.12
    
    elif tramo == "C" or tramo == "D":
        descuento_edad = medicamentos * 0.8
       
else:
    descuento_edad = 0

if tramo == "A" or tramo == "B":
    descuento_despacho = despacho_domicilio * 0.1
    if edad >= 55:
        descuento_despacho = despacho_domicilio * 0.6

else:
    descuento_despacho = 0

valor_total_medicamento = medicamentos - descuento_edad 
valor_total_despacho = despacho_domicilio - descuento_despacho
print(f"El valor de medicamento es: {valor_total_medicamento}")
print(f"El valor de despacho es: {valor_total_despacho}")