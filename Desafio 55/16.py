tipo_cliente = "Postpago"
gb_de_plan = 15
gb_gastados = 18

gb_de_diferencia = gb_gastados - gb_de_plan

cobro_extra_por_cada_gb = 1000
cobro_total = 0

if tipo_cliente == "Postpago" :
    if gb_de_diferencia > 0 :
        cobro_total += gb_de_diferencia * cobro_extra_por_cada_gb
elif tipo_cliente == "Prepago" :
    print("Sin saldo")

print(cobro_total)