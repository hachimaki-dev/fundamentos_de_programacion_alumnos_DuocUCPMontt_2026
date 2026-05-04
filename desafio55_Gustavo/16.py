tipo = "Potspago"
plan = 15
gasto = 18

if tipo == "Potspago":
    cuanto_queda = plan - gasto
    if cuanto_queda < 0 :
        total = cuanto_queda * -1000
        print(total)
elif tipo == "Prepago":
    print("Sin saldo")

else :
    print("Invalido")
