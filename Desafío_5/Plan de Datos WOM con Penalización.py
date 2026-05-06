Cliente = "postpago"
costo_de_plan = 15
gasto_de_plan = 18
Cobro = 0
gb_extras = 1000

if Cliente == "Postpago":
    print (f"\n Usted ha consumido un total de {gasto_de_plan} GB de los {costo_de_plan} GB que tenia.")
    print ("Por lo tanto se le cobrara $2000 pesos por los GB extras que uso.\n")
    cobro = (gb_extras * 3)
    print (f"Usted debe de pagar un total de {cobro}")


elif Cliente == "prepago" :
    print ("Se le corto el internet")



