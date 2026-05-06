#Controla cuántas hojas le quedan a la impresora antes de imprimir un documento.
#Datos Iniciales: A la impresora le quedan 5 hojas. Mandaste a imprimir esto: `['TEXTO', 'FOTO', 'TEXTO', 'FOTO']`.
#Reglas de Negocio: Imprimir un 'TEXTO' gasta 1 hoja. Imprimir una 'FOTO' gasta 3 hojas. Antes de imprimir cada cosa, la impresora revisa si tiene hojas suficientes. Si se queda sin hojas, cancela todo y tira el mensaje 'Sin papel'.
#Restricciones: Resta las hojas que vas usando. Usa `break` para abortar la impresión si las hojas que te quedan son menos de las que necesitas. Imprime 'Imprimiendo [documento]' cuando sí alcance.

hojas_impresora = 5
Imprimir = ["TEXTO", "FOTO", "TEXTO", "FOTO"]

for documento in Imprimir:
    if hojas != 0
        if documento == "TEXTO":    
            hojas = hojas - 1
            print(f"imprimiendo {documento}")
        elif documento == "FOTO":
            if hojas >= 2
                 hojas = hojas - 2
                 print(f"imprimiendo {documento}")
    else:
        print("Sin papel")
        break
