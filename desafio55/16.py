cliente = "postpago"
plan = 15
gasto_de_plan = 18
precio_gb_extras = 1000
if cliente == "postpago":
    if gasto_de_plan > plan:
        gb_extras = gasto_de_plan - plan
        cobro = gb_extras * precio_gb_extras
        print(cobro)
        