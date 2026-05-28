Medicamentos_Mensual = 60000
Despacho_a_Domicilio = 8000
descuento = 0 
descuento_despacho = 0 
Edad = int(input("Ingrese su edad: ")) 
Tramo = input("Ingrese su tramo: ").upper()
if Edad <= 30:
    descuento = 0.82
if Tramo == "A":
    descuento_despacho = 0.9
elif Tramo == "B":
    descuento_despacho = 0.9
elif Tramo == "C":
    descuento = 0.88
    descuento_despacho = descuento_despacho
elif Tramo == "D":
    descuento = 0.88
    descuento_despacho = descuento_despacho
elif 31 <= Edad <= 60:
    descuento = 0.88
if Tramo == "A":
    descuento_despacho = 0.9
if Edad >= 55:
    descuento_despacho = descuento_despacho + 0.95
else: 
    descuento_despacho = descuento_despacho
if Tramo == "B":
    descuento_despacho = 0.9
if Edad >= 55:
    descuento_despacho = descuento_despacho + 0.95
else: descuento_despacho = descuento_despacho
if Tramo == "C":
    descuento_despacho = 0.92
elif Tramo == "D":
    descuento_despacho = 0.92
elif Edad > 60:
    descuento = descuento + 1
    descuento_despacho = descuento_despacho + 1
print(f"El valor de su medicamento es: ${Medicamentos_Mensual * descuento}")
print(f"El valor del despacho es: ${Despacho_a_Domicilio * descuento_despacho}")