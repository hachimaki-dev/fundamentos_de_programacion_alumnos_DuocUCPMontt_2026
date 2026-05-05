#Calcula cuánto debe pagar un cliente por el envío de su compra.

#Datos Iniciales: El cliente compró 25000 en productos y vive en la región de 'Magallanes'.

#Reglas de Negocio: Si la compra es mayor a 20000, el envío normal es gratis (0). Si es menor, cuesta 3000. Pero OJO: si el destino es 'Magallanes' o 'Aysen', siempre se suman 2000 extra al envío por ser zona extrema (incluso si era gratis).

#Restricciones: Haz un `if/else` para el costo base, y luego un `if` SEPARADO (no anidado) para sumar el recargo de zona extrema. Imprime solo el costo total del envío.
costo_envio = 3000
zona_extrema_cobro = 2000
cliente_compra = 25000
region = "Magallanes" 
if cliente_compra >= 20000 and region == "Magallanes" or region == "Aysen":
    print(f"usted debe pagar {zona_extrema_cobro}")
elif cliente_compra <= 20000:
    print(f"usted debe pagar{costo_envio}")
elif cliente_compra >= 20000 and region == "Magallanes" or region == "Aysen":
    print(f"usted debe pagar {zona_extrema_cobro}")
elif cliente_compra <= 20000 and region == "Magallanes" or region == "Aysen":
    print(f"su envio total es {costo_envio + zona_extrema_cobro}")