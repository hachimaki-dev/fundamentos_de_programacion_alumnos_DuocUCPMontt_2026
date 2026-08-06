#DICCIONARIOS:
#no tiene que ver con posiciones numericas si no con claves, y asi se accede,
#acceso por clave no por indice numerico.

#estructura: se abre  con llaves {} y pares "clave":"valor" ej:
diccionario = {
    "nombre": "juan",
    "edad": "20",
    "pasatiempo": "jugar_pelota",
    "juguetes": ["auto","camion"]
}
#en los diccionarios accedes a la posicion de etiqueta descriptiva usando las []. ej: 
print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["pasatiempo"])
print(diccionario["juguetes"])

#agregar una par: (clave:valor) es directo al diccionario . ej:
diccionario["mas_cosas"] = "otras_cosas", "meh", "mas datos"
print(diccionario["mas_cosas"])
#incluso agregando una lista o diccionario completo.

#no se puede acceder a claves que no existen.

# agregar o modificar diccionario : diccionario["clave"] = "dato" | 
#si la clave no existe la crea , si existe puedes reescribir el valor de la clave ej:
diccionario["clave"] = "valor"
print(diccionario["clave"])
#asignacion de nuevo valor a clave:
diccionario["clave"] = "otro valor de ejemplo"
print(diccionario["clave"])


# .get(clave,defecto) ej : diccionario.get("calve", 1) busca en el diccionario sin 
#romper el programa con error. y si no existe devuelve el valor que eligas ej:
dato_quebusco_noExiste = diccionario.get("dato_que_no_existe", 3)
print(dato_quebusco_noExiste)

#.keys() / .values() / .items()
#Los 3 mosqueteros: .keys() devuelve solo las claves, .values() solo los valores, 
# y .items() devuelve pares (clave, valor) — perfecto para recorrer con for.ej:
#for clave, valor in diccionario.items(): print(clave, valor)

#se usa en for y se aplica al diccionario.keys() y devuelve solo las claves
for clave in diccionario.keys():
    print(clave)


for valor in diccionario.values():
    print(valor)
#devuele solo los valores de las calves

for clave , valor in diccionario.items():
    print(clave,valor)
#devuelve todo clave : valor

#del diccionario['clave']  |  diccionario.pop('clave') elimina pares .
# "del"  borra directamente. ej:
del diccionario["nombre"]
print(diccionario)
# .pop("clave") borra y además te devuelve el valor eliminado. ej:

diccionario.pop("pasatiempo")
print(diccionario.pop("edad")) # aca devuelve el valor eliminado

#FOR DICCIONARIOS : 

#modo claves por defecto. al iterar sobre un diccionario , solo recorre las claves.ej:
for clave in diccionario:
    print(clave)

#mode for con clave : item :
#saca del diccionario las claves y el valor del diccionario ej : 
#aca itera a la par con dos valores las claves y los valores , se tiene que usar el 
#diccionario.items para que extraiga del diccionario los dos datos:
for clave , valor in diccionario.items():
    print(f"las clave es: {clave} sumando sus valores con: {valor}")