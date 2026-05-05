cantidad_de_bitcoin = 0.05
precio_antiguo = 50000
precio_hoy = 62000 
bitcoin_antiguo = precio_antiguo * cantidad_de_bitcoin
bitcoin_hoy = precio_hoy * cantidad_de_bitcoin
diferencia = (precio_hoy - precio_antiguo)
total_ganado_dolares = diferencia * cantidad_de_bitcoin
conversion = total_ganado_dolares * 900
print (conversion)