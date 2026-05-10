'''Ejercicio 45: Validación de Existencia (Criptos)
Evita que la aplicación explote revisando si el usuario tiene una criptomoneda antes de cobrarle.

Datos Iniciales: El usuario tiene: `{'BTC': 0.5, 'ETH': 2.0}`.

Reglas de Negocio: El usuario quiere comprar algo pagando con Solana ('SOL'). 

Si le intentas cobrar algo que no existe en su diccionario, Python tirará un error feo y la app se cerrará. Tienes que revisar primero.

Restricciones: Usa la palabra mágica `in` dentro de un `if` para preguntar si `'SOL'` existe en las llaves del diccionario. 

Si está, imprime 'Procesando'. Si no, imprime 'Moneda no soportada'.'''
Sistema_de_comprobacion_existencia_SOL = False

Monedas_del_Usuario = {

            'BTC' : 0.5,

            'ETH' : 2.0

                      }

print("Vas a intentar pagar con la Moneda: SOL")

for X in Monedas_del_Usuario:
    if X == 'SOL':
        print('Procesando')
        Sistema_de_comprobacion_existencia_SOL = True
        continue
    
if Sistema_de_comprobacion_existencia_SOL == False:
    print('Moneda no soportada')