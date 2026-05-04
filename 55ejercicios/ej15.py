# Ejercicio 15: Envíos MercadoLibre (Zonas Extremas)

total_compras_cliente = 250000
destino_origen_cliente = "Magallanes"
destino_origen_cliente = "Aysen"

total_costo_envio = 0
costo_envio_zona_extrema = 2000


if total_compras_cliente > 20000 and destino_origen_cliente == "Magallanes" or destino_origen_cliente == "Aysen":
    total_costo_envio = 2000

elif total_compras_cliente <= 20000 and destino_origen_cliente == "Magallanes" or destino_origen_cliente == "Aysen":
    total_costo_envio = 3000 + 2000

elif total_compras_cliente > 2000 and destino_origen_cliente != "Magallanes" and destino_origen_cliente != "Aysen":
    total_compras_cliente = 3000

print("El costo del envio es de:", total_costo_envio)