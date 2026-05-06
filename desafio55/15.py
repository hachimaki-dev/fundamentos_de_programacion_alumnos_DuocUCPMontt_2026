####Ejercicio 15: Envíos MercadoLibre (Zonas #Extremas#)
#Calcula cuánto debe pagar un cliente por #el envío de su comp#ra.###

#Datos Iniciales: El cliente compró 25000 en productos y vive en la región de 'Magallane#s'.##

#Reglas de Negocio: Si la compra es mayor a 20000, el envío normal es gratis (0).
#  Si es menor, cuesta 3000. Pero OJO: si el destino es 'Magallanes' o 'Aysen', 
# siempre se suman 2000 extra al envío por ser zona extrema (incluso si era grati#s).#

#Restricciones: Haz un `if/else` para el costo base, y luego un `if` SEPARADO 
# (no anidado) para sumar el recargo de zona extrema. Imprime solo el costo total del env#ío.

#Resultado esperado en consola:
#2000

compra_productos_cliente = 25000
region_residencia = "magallanes"
valor_envio = 0


if compra_productos_cliente >= 20000:
    print("envio gratis")
else:
    valor_envio += 3000
    print(f"el costo de envio es de , ${valor_envio}pesos")

if region_residencia == "magallanes" or "aysen":
        valor_envio = valor_envio + 2000
        print(f" total envio por zona extema ${valor_envio} ")   