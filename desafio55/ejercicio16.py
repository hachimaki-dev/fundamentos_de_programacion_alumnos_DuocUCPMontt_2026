tipo_cliente = "Postpago"
gb_plan = 15
gb_gastados = 18
monto_a_pagar = 0

if tipo_cliente == "Postpago":
    print("Vamos a revisar tu consumo de gb")
    if gb_gastados > gb_plan:
        print("Consumiste 3 gb extra, recuerda que cada gb fuera del plan vale $1000 extra")
        monto_a_pagar += 3000
        print(f"Tienes que pagar ${monto_a_pagar} por tu sobreconsumo de datos")
    else:
        print("No habrá ningún cobro extra.")
else:
    print("Al ser un cliente Prepago no se le cobrara ningún extra, solo se le cortara el servicio.")
    print("Debido a que se quedo sin saldo.")