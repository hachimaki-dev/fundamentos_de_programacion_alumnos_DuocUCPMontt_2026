# Ejercicio 26: Procesar Cola de Impresión
# Controla cuántas hojas le quedan a la impresora antes de imprimir un documento.

# Datos Iniciales: A la impresora le quedan 5 hojas. Mandaste a imprimir esto: `['TEXTO', 'FOTO', 'TEXTO', 'FOTO']`.

# Reglas de Negocio: Imprimir un 'TEXTO' gasta 1 hoja. Imprimir una 'FOTO' gasta 3 hojas. Antes de imprimir cada cosa, la impresora revisa si tiene hojas suficientes. 
# Si se queda sin hojas, cancela todo y tira el mensaje 'Sin papel'.

# Restricciones: Resta las hojas que vas usando. Usa `break` para abortar la impresión si las hojas que te quedan son menos de las que necesitas. 
# Imprime 'Imprimiendo [documento]' cuando sí alcance

hojas_restantes = 5
cola_de_impresion = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

for documento in cola_de_impresion:
    if documento == 'FOTO' and hojas_restantes >= 3:
        hojas_restantes -= 3
        print(f"Imprimiendo {documento}")
    elif documento == 'TEXTO' and hojas_restantes >= 1:
        hojas_restantes -= 1
        print(f"Imprimiendo {documento}")
    else:
        print("Sin papel")