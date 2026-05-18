medicameto_mensual = 60000
despacho_a_domicilio = 8000
calculo_descuento = 0
edad = int(input("inresa tu edad"))
tramo = input(" A/B/C/D")
if edad <= 30 :
    if tramo == "A" or tramo == "B" :
        calculo_descuento = medicameto_mensual - ( medicameto_mensual * 0.18)
elif edad <= 30 :
    if tramo == "c" or tramo == "D":
        calculo_descuento = medicameto_mensual - (medicameto_mensual * 0.12)
elif 31 <= edad or edad <= 60:
    if tramo == "A" or tramo == "B":
        calculo_descuento = medicameto_mensual - (medicameto_mensual * 0.12)
elif 31 <= edad or edad <= 60 :
        if tramo == "C" or tramo == "D": 
            calculo_descuento = medicameto_mensual - (medicameto_mensual * 0.08)
else:
    print("sin descuento")
if tramo == "A" or tramo == "B" :
    calculo_envio = despacho_a_domicilio - ( despacho_a_domicilio * 0.1)
elif edad > 55:
    calculo_envio = despacho_a_domicilio - (despacho_a_domicilio * 0.05)


print(f"total a pgar es {calculo_descuento} y de despacho es {calculo_envio}") 
