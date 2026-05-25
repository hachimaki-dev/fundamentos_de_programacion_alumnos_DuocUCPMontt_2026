def descuento_medicamentos(tramo, edad):
    if edad <= 30:
        if tramo == "A" or tramo == "B":
            descuento_medicamentos = 0.18
        else:
            descuento_medicamentos = 0.12
    elif 31 <= edad <= 60:
        if tramo == "A" or tramo == "B":
            descuento_medicamentos = 0.12
        else:
            descuento_medicamentos = 0.08
    else:
        descuento_medicamentos = 0
    return descuento_medicamentos



valor_medicamentos = 60000
despacho_a_domicilio = 8000
edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A/B/C/D): ").upper()
descuento_medicamentos = 0
descuento_despacho = 0
total_medicamentos = 0
total_despacho = 0



if tramo == "A" or tramo == "B":
    descuento_despacho = 0.1
    if edad >= 55:
        descuento_despacho += 0.05

total_medicamentos = valor_medicamentos - (valor_medicamentos * descuento_medicamentos)
total_despacho = despacho_a_domicilio - (despacho_a_domicilio * descuento_despacho)

print(f"El valor de los medicamentos es: {total_medicamentos}")
print(f"El total del despacho es: {total_despacho}")