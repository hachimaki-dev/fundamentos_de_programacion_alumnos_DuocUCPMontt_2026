tipo_cliente = 'Postpago'
plan_gb = 15
uso_gb = 18

if tipo_cliente == 'Postpago':
    if uso_gb > plan_gb:
        recargo = (uso_gb - plan_gb) * 1000
    else:
        recargo = 0

    print(recargo)
else:
    print('Sin saldo')