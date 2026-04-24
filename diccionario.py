#Ejemplo del Profe
alumno = {
    "nombre" : "Benjamin",
    "apellido_1" : "Carmona",
    "apellido_2" : "Pino",
    "edad" : 19,
    "direccion" : "Su casita",
    "curso" : "001D",
    "materias" : ["Fundamentos", "Cloud", "Innovacion"],
    "tiene_hermanos" : True,
    "estatura" : 1.72
}

print(alumno["nombre"])
print(alumno["apellido_1"])

for materia in alumno["materias"]:
    print(materia)

#Ejercicio 1
libro = {
    "titulo": "El nombre del viento",
    "autor": "Patrick Rothfuss",
    "año": "2007"
}

print("Titulo: ", libro["titulo"])
print("Autor: ", libro["autor"])
print("Año: ", libro["año"])

##Ejercicio 2
productos = [{
    "Nombre" : "Baraja de cartas",
    "precio" : "2500",
    "stock" : "50",
}, {
    "Nombre" : "Fichas de poker",
    "precio" : "5000",
    "stock" : "32",
}, {
    "Nombre" : "Abre cartas",
    "precio" : "6000",
    "stock" : "15",
}]

for producto in productos:
    print(Nombre, precio)
