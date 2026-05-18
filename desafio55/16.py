tipo_cliente = "Postpago"
gigas_plan = 15
gigas_gastados = 18
precio_GB_extra = 1000
if tipo_cliente == "Postpago":
    if gigas_gastados > gigas_plan:
        GB_extras = gigas_gastados- gigas_plan
        recargo = GB_extras * precio_GB_extra
        print(recargo)

    else:
        print("El cliente no supero su plan de GB")
elif tipo_cliente == "Prepago":
    print("Sin saldo, Internet cortado")
else:
    print("cliente no reconocido..")

