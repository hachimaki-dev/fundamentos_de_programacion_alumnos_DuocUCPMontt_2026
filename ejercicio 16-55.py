#Su plan le da 15 GB,
# pero gastó 18 GB.
#clientes 'Postpago' se les cobra 1000 pesos por cada giga extra que usen.
#Si el cliente fuera 'Prepago', no se le cobra nada extra, 
# solo se le corta el internet (mensaje 'Sin saldo').

cliente_postpago = "postapago"
plan_gigas = 15
gigas_gastados = 18

if cliente_postpago == "postapago":
    if gigas_gastados > plan_gigas:
        extra_gigas = gigas_gastados - plan_gigas
        cobro = extra_gigas * 1000
        print(cobro)

else:
    print("sin saldo")