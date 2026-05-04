personas = 5
pichangas = 2
valor_pichanga = 15000
schops = 5
valor_schops = 3500
cuenta = valor_pichanga*pichangas + valor_schops*schops

propina = cuenta/100*10
final = cuenta + propina
monto_cada_uno = final/personas
print(monto_cada_uno)