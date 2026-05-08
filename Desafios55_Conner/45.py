#Ejercicio 45: Validación de Existencia (Criptos)
#Evita que la aplicación explote revisando si el usuario tiene una criptomoneda antes de cobrarle.

#Datos Iniciales: El usuario tiene: `{'BTC': 0.5, 'ETH': 2.0}`.

#Reglas de Negocio: El usuario quiere comprar algo pagando con Solana ('SOL').
#Si le intentas cobrar algo que no existe en su diccionario, Python tirará un error feo y la app se cerrará. Tienes que revisar primero.

#Restricciones: Usa la palabra mágica `in` dentro de un `if` para preguntar si `'SOL'` existe en las llaves del diccionario.
#Si está, imprime 'Procesando'. Si no, imprime 'Moneda no soportada'.

usuario={
    "BTC": 0.5,
    "ETH": 2.0,
    #"SOL": 1.0
}

if "SOL" in usuario:
    print("Procesando")
else:
    print("Moneda no soportada")
