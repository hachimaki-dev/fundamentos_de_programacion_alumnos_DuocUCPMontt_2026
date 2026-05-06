tipo_plan = "postpago"
tipo_plan1 = "postpago"
tipo_plan2 = "prepago"

plan = 15

gasto = 18

if tipo_plan == tipo_plan1:
    if gasto > plan:
        calculo = gasto - plan
        total = calculo * 1000
else:
    print("Sin saldo")

print(total)        