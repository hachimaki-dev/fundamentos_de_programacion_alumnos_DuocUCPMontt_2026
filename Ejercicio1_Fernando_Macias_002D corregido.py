descuento = 0
descuento_despacho = 0
while True:
    edad = int(input("Ingrese su edad :"))
    tramo = input("Ingrese su tramo (A, B , C , D) : ").upper
    medicamentos_mensual = int(input("Ingrese el valor de sus medicamentos : "))
    despacho_domicilio = int(input("Ingrese el valor del despacho a domicilio : "))
    if (edad <= 30) and (tramo == "A" or tramo == "B"):
        descuento = int(medicamentos_mensual * 0.82)
        descuento_despacho = int(despacho_domicilio * 0.10 - despacho_domicilio)
        print(f"Se le ha aplicado un descuento del 18% de sus medicamentos ({descuento}) y del 10% en su despacho total ({descuento_despacho})")
    elif (edad <= 30) and (tramo == "C" or tramo == "D"):
        descuento = int(medicamentos_mensual * 0.88)
        descuento_despacho = int(despacho_domicilio * 0.10 - despacho_domicilio)
        print(f"Se le ha aplicado un descuento del 12% de sus medicamentos ({descuento}) y del 10% en su despacho total ({descuento_despacho})")
    elif (edad <= 31 and edad <= 60) and (tramo == "A" or  tramo == "B"):
        descuento = int(medicamentos_mensual * 0.88)
        descuento_despacho = int(despacho_domicilio * 0.15 - despacho_domicilio)
        print(f"Se le ha aplicado un descuento del 10% en sus medicamentos ({descuento}) y del 15% en su despacho total ({descuento_despacho})")
    elif (edad <= 31 and edad <= 60) and (tramo == "C" or tramo == "D"):
        descuento = int(medicamentos_mensual * 0.92)
        descuento_despacho = int(despacho_domicilio * 0.15 - despacho_domicilio)
        print(f"Se le ha aplicado un descuento del 8% en sus medicamentos ({descuento}) y del 15% en su despacho total ({descuento_despacho}) ")
    elif (edad >= 60) and (tramo == "A" or tramo == "B" or tramo == "C" or tramo == "D"):
        print(f"Por su edad no se le ha aplicado ningun descuento , el valor de sus medicamentos son {medicamentos_mensual} y su despacho sigue normal {despacho_domicilio}")
    else :
        print("Opcion invalida , ingrese opcion correcta!")