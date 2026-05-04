tipo_cliente = "Postpago"
gigas_plan = 15
gigas_usados = 18
cobro_extra = 0

if tipo_cliente == "Postpago":
    if gigas_usados > gigas_plan:
        cobro_extra += (gigas_usados - gigas_plan) * 1000 # 1000 pesos por giga extra
        print(cobro_extra)
    else:
        print(cobro_extra)
elif tipo_cliente == "Prepago":
    if gigas_usados > gigas_plan:
        print("Sin saldo")
    else:
        pass
else:
    print("Tipo de cliente desconocido")
