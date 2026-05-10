#Ejercicio 47: Sistema de Daño Condicional RPG
#Programa la vida y la muerte de un jefe de videojuego usando un diccionario.

#Datos Iniciales: El jefe es `boss = {'hp': 100, 'estado': 'vivo'}`.

#Reglas de Negocio: Le pegaste un golpe crítico de 150 de daño (réstaselo a su 'hp').
#El problema es que en matemáticas eso daría -50 de vida, pero en un juego no puedes tener vida negativa.
#Si la vida baja de 0, tienes que dejarla en exactamente 0 y cambiar su 'estado' a 'muerto'.

#Restricciones: Resta la vida. Luego usa un `if` para revisar si la vida quedó en menos de cero.
#Si es así, sobreescribe las dos llaves del diccionario con los nuevos valores. Imprime al jefe.

final_boss={
    "hp": 100,
    "estado": "vivo"
}

mi_daño=100
critico=mi_daño+50

final_boss["hp"]=final_boss["hp"]-critico
if final_boss["hp"]<=0:
    final_boss["hp"]=0
    final_boss["estado"]="muerto"

print(final_boss)