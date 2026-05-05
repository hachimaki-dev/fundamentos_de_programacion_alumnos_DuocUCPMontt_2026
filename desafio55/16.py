#Ejercicio 16: Plan de Datos WOM con Penalización

cliente = "Postpago"
plan_cliente = 15
gasto_cliente = 18
gasto_extra = 1000

if cliente == "Postpago":
    Cargo_extra = gasto_cliente - plan_cliente 
    if Cargo_extra > 1:
        cargo_final = Cargo_extra * gasto_extra

        print(cargo_final)
elif cliente == "Prepago":
    Cargo_extra = gasto_cliente - plan_cliente 
    if Cargo_extra > 1:
        print("sin saldo")