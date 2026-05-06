tipo_cliente = 'Postpago'
gigas_plan = 15
gigas_usados = 18
recargo = 0


if tipo_cliente == 'Postpago':

    if gigas_usados > gigas_plan:
        gigas_extra = gigas_usados - gigas_plan
        recargo = gigas_extra * 1000
    
    print(recargo)

else:

    print('Sin saldo')