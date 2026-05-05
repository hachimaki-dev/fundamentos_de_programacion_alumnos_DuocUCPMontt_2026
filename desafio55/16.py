plan = 15
usados = 18
postpago = "postpago"
prepago = "prepago"
cobro = 0
extra = 1000


cliente = input("¿Que tipo de cliente es?")
if cliente == postpago:
    gb = usados - plan
    cobro = extra * gb
else:
    cliente == prepago
    cobro = cobro + 0
    

print(f"La recarga final es de: {cobro}")
