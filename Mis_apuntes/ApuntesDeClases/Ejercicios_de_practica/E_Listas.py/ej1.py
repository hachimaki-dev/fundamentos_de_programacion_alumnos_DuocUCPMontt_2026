###persona = {
###    "nombre": "Ana",
###    "edad": 20,
###    "carrera": "Programación"
###}
###
###for clave, valor in persona.items():        #IMPRIME CLAVES Y SU VALOR
###    print(clave, valor)
###
###for valor in persona.values():              #IMPRIME SOLO EL VALOR DE LA CLAVE
###    print(valor)
libro = {
    "titulo" : "One Piece: Arco de Elbaf",
    "autor" : "Eiichiro Oda",
    "año" : "2009"
}
for clave, valor in libro.items():
    print(clave, valor)
libro["año"] = int(input("Actualiza el año"))
print(libro["año"])
libro ["Editorial"] = "IVREA"
print(libro)
print(libro["Editorial"])