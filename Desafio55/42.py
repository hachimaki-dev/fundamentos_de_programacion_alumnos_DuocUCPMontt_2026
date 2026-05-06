cliente = {'puntos': 1500}

cliente.update({"puntos": cliente.get("puntos") + 300})

print(cliente)