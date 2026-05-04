'''Ejercicio 15: Envíos MercadoLibre (Zonas Extremas)
Calcula cuánto debe pagar un cliente por el envío de su compra.

Datos Iniciales: El cliente compró 25000 en productos y vive en la región de 'Magallanes'.

Reglas de Negocio: Si la compra es mayor a 20000, el envío normal es gratis (0). Si es menor, cuesta 3000. Pero OJO: si el destino es 'Magallanes' o 'Aysen', siempre se suman 2000 extra al envío por ser zona extrema (incluso si era gratis).

Restricciones: Haz un `if/else` para el costo base, y luego un `if` SEPARADO (no anidado) para sumar el recargo de zona extrema. Imprime solo el costo total del envío.'''

compra = 25000
lugar = "Magallanes"

if compra > 20000:
    envio = 0
else: 
    envio = 3000

if lugar == "Magallanes" or lugar == "Aysen":
    envio += 2000

print(f"costo envio: {envio}")
