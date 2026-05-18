edad = 0
medicamento = 60000
despacho_domicilio = 8000
descuento_medicina = 0
descuento_despacho = 0
descuento_despacho = 0
boleta_medicina = 0
boleta_despacho = 0
edad = int(input("que edad tienes: "))
tramo = (input("que tramo eres: "))
if edad <= 30:
    if tramo in ["a","b"]:
        descuento_medicina = medicamento * 0.18
        boleta_medicina = medicamento - descuento_medicina
        descuento_despacho = despacho_domicilio * 0.10
        boleta_despacho = despacho_domicilio - descuento_despacho
        print(f"tu valor de medicamento es {boleta_medicina}")
        print(f"tu valor de despacho es de {boleta_despacho}")
    elif tramo in ["c", "d"]:
        descuento_medicina = medicamento * 0.12
        boleta_medicina = medicamento - descuento_medicina
        print(f" tu valor de medicametno es de {boleta_medicina}")
        print(f"tu valor de despacho es de {despacho_domicilio}")
elif 31 <= edad and edad <= 60:
    if tramo in ["a", "b"]:
        descuento_medicina = medicamento * 0.12
        boleta_medicina = medicamento - descuento_medicina
        descuento_despacho = despacho_domicilio * 0.10
        boleta_despacho = despacho_domicilio - descuento_despacho
        print(f"tu valor de medicina es de {boleta_medicina}")
        print(f"tu valor de despacho es de {boleta_despacho}")

    elif tramo in ["c", "d"]:
        descuento_medicina = medicamento * 0.08
        boleta_medicina = medicamento - descuento_medicina
        print(f"tu valor de medicina es de {boleta_medicina}")
        print(f"tu valor de despacho es de {despacho_domicilio}")
else:
    print("no tienes descuento")
    print(f"valor de medicina {medicamento}")
    print(f"valor de despacho {despacho_domicilio}")