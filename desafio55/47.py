#Programa la vida y la muerte de un jefe de videojuego usando un diccionario.

#Datos Iniciales: El jefe es `boss = {'hp': 100, 'estado': 'vivo'}`.

#Restricciones: Resta la vida. Luego usa un `if` para revisar si la vida quedó en menos de cero. Si es así, sobreescribe las dos llaves del diccionario con los nuevos valores. Imprime al jefe
boss = {"hp" : 100, "estado" : "vivo"}
boss["hp"] -= 150
if boss["hp"] <= 0:
    boss["hp"] = 0
    boss["estado"] = "muerto"
print(boss)