cliente = "Postpago"
plan = 15
gasto = 18
deuda = 0

if cliente == "Postpago":
    if gasto > plan:
        deuda =(gasto - plan) * 1000
        print(deuda)
    else:
        plan = plan - gasto
        print(f"{plan}Gb disponibles")
elif cliente == "Prepago":
    if gasto > plan:
        print("Sin saldo")
    else:
        plan = plan - gasto
        print(f"{plan}Gb disponibles")