#Controla cuántas hojas le quedan a la impresora antes de imprimir un documento.

#Datos Iniciales: A la impresora le quedan 5 hojas. Mandaste a imprimir esto: `['TEXTO', 'FOTO', 'TEXTO', 'FOTO']`.

#Reglas de Negocio: Imprimir un 'TEXTO' gasta 1 hoja. Imprimir una 'FOTO' gasta 3 hojas. Antes de imprimir cada cosa, la impresora revisa si tiene hojas suficientes. Si se queda sin hojas, cancela todo y tira el mensaje 'Sin papel'.

#Restricciones: Resta las hojas que vas usando. Usa `break` para abortar la impresión si las hojas que te quedan son menos de las que necesitas. Imprime 'Imprimiendo [documento]' cuando sí alcance.
impresora = ["TEXTO" , "FOTO" , "TEXTO" , "FOTO"]
for hojas in impresora:
    if hojas == "FOTO":
        print("impresora gasto 5 hojas")
        print("se acabaron las hojas!")
        break
    elif hojas == "TEXTO":
        print("impresora gasto 2 hojas")
#hojas_disponbiles = 5
#cola_impresion = ["TEXTO" , "FOTO" , "TEXTO" , "FOTO"]
#for documento in cola_impresion:
    #if documento == "TEXTO" and hojas_disponbiles >= 1:
    #hoja_disponibles = hojas_disponibles - 1
    #print(imprimiento texto)
    #elif documento == "FOTO" and hojas_disponbibles >= 3:
    #hojas_disponibles = hojas_disponible - 3
    #print("imprimiendo foto")
    #else:
        #print("sin hojas")