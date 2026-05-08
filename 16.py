#Calcula cuánto debe pagar un cliente por el envío de su compra


# Datos Iniciales
compra = 25000
destino = 'Magallanes'
envio = 0

# 1. Reglas de Negocio: Costo Base (if/else)
if compra > 20000:
    envio = 0
else:
    envio = 3000

# 2. Reglas de Negocio: Zona Extrema (if SEPARADO)
if destino == 'Magallanes' or destino == 'Aysen':
    envio = envio + 2000

# Imprimir solo el costo total del envío
print(envio)


