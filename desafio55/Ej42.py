#💀 Rango: Infernal
#Ejercicio 42: Actualización de Puntos (Wallet)
#Súmale puntos de regalo a la cuenta de un cliente fiel.

#Datos Iniciales: El cliente tiene un diccionario con sus datos: `{'puntos': 1500}`.

#Reglas de Negocio: Por comprar hoy, el cliente se ganó 300 puntos extra. Tienes que sumárselos a los que ya tiene.

#Restricciones: No escribas el resultado final mentalmente (eso es trampa). Dile a Python que vaya a la llave `'puntos'` y le sume `+ 300` a lo que sea que haya adentro. Imprime el diccionario completo para ver el cambio.

datos_cliente = {
    "puntos_cliente": 1500,
    }

for i in datos_cliente :
    datos_cliente[i] += 300

print(datos_cliente)
