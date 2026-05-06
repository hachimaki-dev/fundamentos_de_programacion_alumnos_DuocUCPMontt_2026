"""Ejercicio 26: Procesar Cola de Impresión
Controla cuántas hojas le quedan a la impresora antes de imprimir un documento.

Datos Iniciales: A la impresora le quedan 5 hojas. Mandaste a imprimir esto: `['TEXTO', 'FOTO', 'TEXTO', 'FOTO']`.

Reglas de Negocio: Imprimir un 'TEXTO' gasta 1 hoja. Imprimir una 'FOTO' gasta 3 hojas. 

Antes de imprimir cada cosa, la impresora revisa si tiene hojas suficientes. Si se queda sin hojas, cancela todo y tira el mensaje 'Sin papel'.

Restricciones: Resta las hojas que vas usando. Usa `break` para abortar la impresión si las hojas que te quedan son menos de las que necesitas. 

Imprime 'Imprimiendo [documento]' cuando sí alcance."""
import time
Imprimir = ["TEXTO", "FOTO", "TEXTO", "FOTO"]

Hojas = 5

for impresion in Imprimir:
    if impresion == "TEXTO":
        Hojas -= 1
        if Hojas > -1:
            time.sleep(0.5)
            print(f"Imprimiendo: {impresion}")
        else:
            break
    if impresion == "FOTO":
        Hojas -=3
        if Hojas > -1:
            time.sleep(0.5)
            print(f"Imprimiendo: {impresion}")
        else:
            break
if Hojas < 0:
    time.sleep(0.5)
    print("Se acabo el papel")