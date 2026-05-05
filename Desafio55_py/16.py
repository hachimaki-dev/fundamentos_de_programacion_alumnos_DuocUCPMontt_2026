plan = 15
gasto = 18
gb_extras = 3
cliente_tipo = "postpago"

if cliente_tipo == "postpago":
    gb_extras = gb_extras * 1000
    print(f"LO QUE DEBES DE PAGAR ES {gb_extras}")
elif cliente_tipo == "prepago":
    print("SIN SALDO")


