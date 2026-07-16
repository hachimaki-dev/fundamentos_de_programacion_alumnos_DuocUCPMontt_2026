Tipo_cliente = "Postpago"
plan_cliente = 15 #GB
consumo_cliente = 18
cargo_extra_cliente = 0 #pesos
if Tipo_cliente == "Postpago":
    if consumo_cliente > plan_cliente:
        cargo_extra_cliente = (consumo_cliente - plan_cliente) * 1000
        print(f"El cargo extra es de {cargo_extra_cliente}")
    else:
        print(f"Cargo extra 0 pesos")
else:
    print("Se quedó sin saldo X__X")