#Define la lista precios = [1000, 2500, 500]. Crea una variable total_pagar con valor 0. 
# Recorre la lista con un ciclo for, suma cada precio a total_pagar e imprime el resultado final.
precios = [1000, 2500, 500]
total_pagar = 0 
for precio in precios:
    total_pagar = precio + total_pagar
print(total_pagar)

