tipo_cliente = "Postpago"
Plan_cliente = 15
Gigas_usadas = 18
if tipo_cliente == "Postpago":
    if Gigas_usadas > Plan_cliente:
        recargo = (Gigas_usadas - Plan_cliente)*1000
        print("El cliente tiene un recargo de:", recargo)
else:
    print("Sin saldo.")