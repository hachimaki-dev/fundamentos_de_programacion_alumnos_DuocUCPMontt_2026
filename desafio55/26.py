#Controla cuántas hojas le quedan a la impresora antes de imprimir un documento.
#Datos Iniciales: A la impresora le quedan 5 hojas. Mandaste a imprimir esto: `['TEXTO', 'FOTO', 'TEXTO', 'FOTO']`.
#Reglas de Negocio: Imprimir un 'TEXTO' gasta 1 hoja. Imprimir una 'FOTO' gasta 3 hojas. 
#Antes de imprimir cada cosa, la impresora revisa si tiene hojas suficientes. Si se queda sin hojas, cancela todo y tira el mensaje 'Sin papel'.
#Restricciones: Resta las hojas que vas usando. Usa `break` para abortar la impresión si las hojas que te quedan son menos de las que necesitas.
#Imprime 'Imprimiendo [documento]' cuando sí alcance. Imprimiendo TEXTO\nImprimiendo FOTO\nImprimiendo TEXTO\nSin papel
imprimir = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
hojas_impresora = 5
for hoja in imprimir:
    if hoja == "TEXTO":
        hojas_ocupadas = 1
    elif hoja == "FOTO":
        hojas_ocupadas = 3
    if hojas_impresora < hojas_ocupadas:
        print("Sin papel")
        break
    print("Imprimiendo " + hoja)
    hojas_impresora -= hojas_ocupadas
