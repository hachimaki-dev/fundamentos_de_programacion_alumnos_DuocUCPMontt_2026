#Ejercicio : Ejercicio 15: Envíos MercadoLibre (Zonas Extremas)
#MEDIUM
#Calcula cuánto debe pagar un cliente por el envío de su compra.[cite: 2]

#Datos Iniciales: El cliente compró 25000 en productos y vive en la región de 'Magallanes'.[cite: 2]

#Reglas de Negocio: Si la compra es mayor a 20000, el envío normal es gratis (0). Si es menor, cuesta 3000. Pero OJO: si el destino es 'Magallanes' o 'Aysen', siempre se suman 2000 extra al envío por ser zona extrema (incluso si era gratis).[cite: 2]

#Restricciones: Haz un if/else para el costo base, y luego un if SEPARADO (no anidado) para sumar el recargo de zona extrema. Imprime solo el costo total del envío.[cite: 2]

total_carrito = 25000
vivienda_comprador = "Magallanes"
valor_envio_gratis = 20000

if total_carrito > valor_envio_gratis :
    costo_envio = 0
    if vivienda_comprador != "Magallanes" and vivienda_comprador != "Aysen" :
        print("El valor de su envio es 0")
    elif vivienda_comprador == "Magallanes" or vivienda_comprador == "Aysen" :
        costo_envio = costo_envio + 2000
        print(f"El valor de su envio es {costo_envio}")
elif total_carrito < valor_envio_gratis :
    costo_envio = 3000
    if vivienda_comprador == "Magallanes" or vivienda_comprador == "Aysen" :
        costo_envio = costo_envio + 2000
        print(f"El costo de su envio es {costo_envio} pesos")
    else :
        print("El costo de envio es 3000 pesos chilenos")
    