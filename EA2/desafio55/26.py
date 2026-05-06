'''Ejercicio 26: Procesar Cola de Impresión
Controla cuántas hojas le quedan a la impresora antes de imprimir un documento.

Datos Iniciales: A la impresora le quedan 5 hojas. Mandaste a imprimir esto: `['TEXTO', 'FOTO', 'TEXTO', 'FOTO']`.

Reglas de Negocio: Imprimir un 'TEXTO' gasta 1 hoja. Imprimir una 'FOTO' gasta 3 hojas. Antes de imprimir cada cosa, la impresora revisa si tiene hojas suficientes. Si se queda sin hojas, cancela todo y tira el mensaje 'Sin papel'.

Restricciones: Resta las hojas que vas usando. Usa `break` para abortar la impresión si las hojas que te quedan son menos de las que necesitas. Imprime 'Imprimiendo [documento]' cuando sí alcance.'''

hojas = 5
impresion = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

for i in impresion:
    if i == 'TEXTO' and hojas >= 1:
        print(f"imprimiendo {i}")
        hojas -= 1
    elif i == 'FOTO' and hojas >= 3:
        print(f"imprimiendo {i}")
        hojas -= 3
    else:
        print("Sin Papel")
        break