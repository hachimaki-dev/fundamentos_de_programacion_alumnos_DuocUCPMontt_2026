despacho_a_domicilio = 8000


edad = int(input("ingrese su edad: "))
tramo = input("a que tramo eres :   ")


if tramo == "A" or tramo == "B" :
        descuento_despacho = despacho_a_domicilio * 0.10
        descuento_despacho = despacho_a_domicilio - descuento_despacho
        if edad >= 55:
            descuento_despacho = descuento_despacho * 0.05
            descuento_despacho = despacho_a_domicilio - descuento_despacho


print(f"{descuento_despacho}")
print()
print(f"{despacho_a_domicilio}")