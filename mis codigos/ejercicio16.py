tipo = "postpago"
gastado = 18
plan = 15
pago = 0
pagar = 0

if tipo == "postpago":

    if gastado > plan:
        extra = gastado - plan
        pagar = extra * 1000

    else:
        pagar = 0

else:
    print("Sin saldo")

print(pagar)

        

