"""
Ejercicio 15: Envíos MercadoLibre (Zonas Extremas)
Calcula cuánto debe pagar un cliente por el envío de su compra.

Datos Iniciales: El cliente compró 25000 en productos y vive en la región de 'Magallanes'.

Reglas de Negocio: Si la compra es mayor a 20000, el envío normal es gratis (0). Si es menor,
cuesta 3000. Pero OJO: si el destino es 'Magallanes' o 'Aysen', siempre se suman 2000 extra al 
envío por ser zona extrema (incluso si era gratis).

Restricciones: Haz un `if/else` para el costo base, y luego un `if` SEPARADO (no anidado) para 
sumar el recargo de zona extrema. Imprime solo el costo total del envío.

Resultado esperado en consola:
2000
"""

productos = 25000
region = "Magallanes"

if productos > 20000:
    costo_envio = 0
else:
    costo_envio = 3000

if region in ["Magallanes", "Aysen"]:
    costo_envio = costo_envio + 2000

print(f"Costo envio ${costo_envio} por ser zona extrema")
