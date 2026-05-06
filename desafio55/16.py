tipo_cliente = "postpago"
plan_cliente = 15
consumo_cliente = 18
gigas_extras_usadas = 0
cargo_gigas_extras = 1000

if tipo_cliente == "postpago":
    if consumo_cliente > plan_cliente:
        gigas_extras_usadas = consumo_cliente - plan_cliente
        cargo_gigas_extras = cargo_gigas_extras * gigas_extras_usadas
        print(cargo_gigas_extras)

else:
    print("sin cargo adicional")

