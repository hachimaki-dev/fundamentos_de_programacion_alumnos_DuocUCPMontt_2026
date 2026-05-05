#Ejercicio 15: Envíos MercadoLibre (Zonas Extremas)


productos_compra = 19000
lugar = "Magallanes"
envio_normal = 0
envio_porpagar = 3000
envio_zonaextrema = 2000
costo_total = 0

if productos_compra > 20000:
    costo_total = 0 
    
else:
    #print("3000 de envio")
    costo_total += envio_porpagar


if lugar == "Magallanes" or  lugar == "Aysen":
    #print("2000 extra en envio por zona extrema")
    costo_total += envio_zonaextrema


print(costo_total)


