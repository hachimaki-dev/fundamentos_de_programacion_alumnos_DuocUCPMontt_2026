medicameto_mensual = 60000
despacho_a_domicilio = 8000


 

calculo_descuento = 0

edad = int(input("inresa tu edad"))
tramo = input("inresa tu tramo A/B/C/D")


if( edad <= 30 ) or ( tramo == "A" or tramo == "B"): 
        calculo_descuento = medicameto_mensual - ( medicameto_mensual * 0.18)
elif edad <= 30 or (tramo == "c" or tramo == "D"): 
            calculo_descuento = medicameto_mensual -  (medicameto_mensual * 0.12)
elif (31 <= edad and edad <= 60) or  (tramo == "A" and tramo == "B"):
                calculo_descuento = medicameto_mensual -  (medicameto_mensual * 0.12)
elif (31 <= edad or edad <= 60) or (tramo == "C" or tramo == "D"): 
                calculo_descuento = medicameto_mensual -   (medicameto_mensual * 0.08)
else:
    print("sin descuento")
                  
if  tramo == "A" and tramo == "B" :
           calculo_envio = despacho_a_domicilio -  ( despacho_a_domicilio * 0.1)
elif edad > 55:
      calculo_envio = despacho_a_domicilio -   (despacho_a_domicilio * 0.05)
else:
        print("sin descuento")

  