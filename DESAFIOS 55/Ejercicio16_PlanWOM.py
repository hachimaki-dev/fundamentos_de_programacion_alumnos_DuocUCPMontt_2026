tipo_cliente='Postpago'
gbs_usados= 18

if tipo_cliente=='Postpago':
    if gbs_usados > 15:
        costogbsextras= 1000 * (gbs_usados-15)
        print(costogbsextras)
if tipo_cliente=='Pregrado':
    if gbs_usados > 15:
        print ('Sin Saldo')