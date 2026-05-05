cliente = "Postpago"
plan = 15
cliente_gasto = 18
diferencia = cliente_gasto - plan
post_pago = 1000

if cliente == "Postpago" :

    if cliente_gasto > plan :
        post_pago = post_pago*diferencia
        print(post_pago)

else: 
    print("sin saldo")

        





