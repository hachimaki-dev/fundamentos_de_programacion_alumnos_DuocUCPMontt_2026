valor_compra_cliente = 25000
región_cliente = "Magallanes"
coste_envío = 0


if valor_compra_cliente > 20000:
    coste_envío = 0
else:
    coste_envío = 3000

if región_cliente == "Magallanes" or región_cliente == "Aysen":
    coste_envío = coste_envío + 2000
    valor_compra_cliente = valor_compra_cliente + coste_envío
    print(f"Valor final del envío: {coste_envío} pesos")
else:
    coste_envío = coste_envío
    valor_compra_cliente = valor_compra_cliente + coste_envío
    print(f"Valor final del envío: {coste_envío} pesos")
