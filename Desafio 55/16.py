tipo_cliente="Prepago"
gigas_del_plan=15
costo_extra=1000 #por cada giga usado

gasto_gigas_mes=18

if tipo_cliente=="Postpago":
    cobro_extra=0
    if gasto_gigas_mes>gigas_del_plan:
        cobro_extra=costo_extra*(gasto_gigas_mes-gigas_del_plan)
        print(f"${cobro_extra} tendras que pagar extra")
    else:
        print("No hay cobro extra")
elif tipo_cliente=="Prepago":
    if gasto_gigas_mes >= gigas_del_plan:
        print("Sin Saldo")
    else:
        print("Aun tienes datos disponibles"
)
              