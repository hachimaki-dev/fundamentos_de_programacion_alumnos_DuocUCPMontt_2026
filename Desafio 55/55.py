dinero_a_retirar = 37000

billetes_entregados = {20000 : 0,
                       10000 : 0,
                       5000 : 0,
                       1000 : 0}

for key, value in billetes_entregados.items() :
    cantidad_billete = dinero_a_retirar // key
    dinero_a_retirar -= key

    billetes_entregados.update({key : cantidad_billete})

print(billetes_entregados)

