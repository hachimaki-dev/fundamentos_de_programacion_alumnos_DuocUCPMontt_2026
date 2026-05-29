def descuento_18_medicamento(plata):
    return plata * 0.82
def descuento_12_medicamento(plata):
    return plata * 0.88
def descuento_8_medicamento(plata):
    return plata * 0.92
def edad_y_tramo(edad, tramo):
    edad = int(input("Ingrese su edad"))
    tramo = input("Ingrese su tramo")
    return edad, tramo
def descuento_despacho(edad, tramo):
    descuento_desp = 1.0
    if tramo == "A" or tramo == "B":
        descuento_desp = descuento_desp - 0.10
    if edad >= 55:
        descuento_desp = descuento_desp - 0.05
    return descuento_desp     


        
    