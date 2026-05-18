valor_mensual_medicamentos = 60000
valor_despacho_domicilio = 8000

def pedirDatosUsuario():
    global edad_usuario, tramo_usuario
    edad_usuario = int(input("Ingrese su edad: "))
    tramo_usuario = input("Ingrese su tramo (A, B, C o D): ")
    tramo_usuario = tramo_usuario.upper()

def conseguirDescuentoMedicamentos(edad, tramo):
    if edad <= 30:
        if tramo == "A" or tramo == "B":
            return(18)
        elif tramo == "C" or tramo == "D":
            return(12)
    elif 31 <= edad <= 60:
        if tramo == "A" or tramo == "B":
            return(12)
        elif tramo == "C" or tramo == "D":
            return(8)
    else:
        return(0)

def conseguirDescuentoDespacho(edad, tramo):
    if (tramo == "A" or tramo == "B") and edad_usuario >= 55:
        return(15)
    elif tramo == "A" or tramo == "B":
        return(10)
    else:
        return(0)

def main():
    pedirDatosUsuario()

    porcentaje_descuento_medicamentos = conseguirDescuentoMedicamentos(edad_usuario, tramo_usuario)
    porcentaje_descuento_despacho = conseguirDescuentoDespacho(edad_usuario, tramo_usuario)

    total_medicamentos = valor_mensual_medicamentos - (valor_mensual_medicamentos / 100 * porcentaje_descuento_medicamentos)
    total_despacho = valor_despacho_domicilio - (valor_despacho_domicilio / 100 * porcentaje_descuento_despacho)

    print(f"El valor de medicamentos es ${total_medicamentos}")
    print(f"El valor del despacho es ${total_despacho}")



main()
