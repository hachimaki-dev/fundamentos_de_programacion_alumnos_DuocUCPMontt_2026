Compra_cliente = 25000 
zona = "Magallanes"
costo_de_envio = 0
costo_de_zona = 2000

if Compra_cliente > 20000 :
    print (f"Debido a su compra con un precio de ${Compra_cliente} Su envío sera completamente gratis.")

else :
    print (f"Debido a su compra con un precio de $17000 Su en envío tendra un costo de $3000")
    

if zona == "Magallanes":

    Valor_Total = costo_de_envio + costo_de_zona

    print (f"Debido a la zona donde se encuentra, que es {zona} Debemos de cobrarle un total de ${costo_de_zona} Por lo tanto todo saldria ${Valor_Total}")