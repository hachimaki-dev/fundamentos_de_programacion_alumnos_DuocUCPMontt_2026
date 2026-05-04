cliente="Postpago"
plan_en_gigas=15
gasto_de_gigas=18
gasto_total=0
if cliente=="Postpago":
    if gasto_de_gigas>plan_en_gigas:
        gasto_total= (gasto_de_gigas-plan_en_gigas)*1000
elif cliente=="Prepago":
    if gasto_de_gigas>plan_en_gigas:
        print("Sin saldo")
print(gasto_total)