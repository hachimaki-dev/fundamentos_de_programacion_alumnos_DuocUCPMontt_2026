#Ejercicio 15: Envíos MercadoLibre (Zonas Extremas)
#Calcula cuánto debe pagar un cliente por el envío de su compra.

#Datos Iniciales: El cliente compró 25000 en productos y vive en la región de 'Magallanes'.

#Reglas de Negocio: Si la compra es mayor a 20000, el envío normal es gratis (0). Si es menor, cuesta 3000. Pero OJO: si el destino es 'Magallanes' o 'Aysen', siempre se suman 2000 #extra al envío por ser zona extrema (incluso si era gratis).

#Restricciones: Haz un `if/else` para el costo base, y luego un `if` SEPARADO (no anidado) para sumar el recargo de zona extrema. Imprime solo el costo total del envío.

gasto_cliente_producto = 250000
destino_cliente = "magallanes"
if gasto_cliente_producto > 20000:
    costo_envio = 0
elif gasto_cliente_producto <= 20000:
    costo_envio = 3000
if destino_cliente == "magallanes" or destino_cliente == "aysen":
    costo_envio += 2000
    print(F"el costo total de envio es {costo_envio}")


