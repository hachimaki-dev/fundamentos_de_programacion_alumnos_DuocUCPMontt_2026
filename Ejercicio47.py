'''Ejercicio 47: Sistema de Daño Condicional RPG
Programa la vida y la muerte de un jefe de videojuego usando un diccionario.

Datos Iniciales: El jefe es `boss = {'hp': 100, 'estado': 'vivo'}`.

Reglas de Negocio: Le pegaste un golpe crítico de 150 de daño (réstaselo a su 'hp'). El problema es que en matemáticas eso daría -50 de vida, 
pero en un juego no puedes tener vida negativa. Si la vida baja de 0, tienes que dejarla en exactamente 0 y cambiar su 'estado' a 'muerto'.

Restricciones: Resta la vida. Luego usa un `if` para revisar si la vida quedó en menos de cero. 

Si es así, sobreescribe las dos llaves del diccionario con los nuevos valores. Imprime al jefe.'''

BOSS = {
    'HP': 100, 
    'Estado': 'Vivo'
        }

print('Atacas al jefe realizando 150 de ataque')
BOSS['HP'] -= 150
if BOSS['HP'] <= 0:
    BOSS['HP'] = 0
    BOSS['Estado'] = 'Muerto'

print(f'El BOSS tiene {BOSS["HP"]} de vida y se encuentra {BOSS["Estado"]}')