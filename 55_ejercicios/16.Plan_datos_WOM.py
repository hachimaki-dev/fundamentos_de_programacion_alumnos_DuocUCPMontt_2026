tipo_de_servicio = 'Postpago'
gb_plan_contratado = 15
gb_usados = 18
cobro_extra = 0
if tipo_de_servicio == 'Postpago':
    if gb_usados > gb_plan_contratado:
        cobro_extra = (gb_usados - gb_plan_contratado) * 1000
        print(cobro_extra)
elif tipo_de_servicio == 'Prepago':
    if gb_usados > gb_plan_contratado:
        print("Sin saldo")