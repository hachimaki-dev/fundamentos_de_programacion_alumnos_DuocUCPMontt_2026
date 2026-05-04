#Un diccionario NO ES UNA LISTA

#estudiantes = ["Benjamín", "Caromona", "Su casita", 19, "+569 89548525", "001D", "Fundamentos de Programacion", "Julian", "Navarro" , "Casita de julian"]
#
#print( estudiantes[9] )


alumno = {
    "nombre" : "Benajmín", 
    "apellido_1" : "Carmona",
    "apellido_2" : "Pino",
    "edad" : 19,
    "direccion" : "Su casita",
    "curso" : "001D",
    "materias" : ["Fundamentos", "Cloud", "Mate 1", "COmuni", "innovación"],
    "hermanos" : [
        {
            "nombre" : "HErmano de Benaja",
            "edad" : 30
        },
         {
            "nombre" : "HErmano de Benaja numero 2",
            "edad" : 15
        }
    ],
    "estatura" : 1.72
}

#print(f"  { alumno["hermanos"][0]["nombre"]  }  ")

#print(f"{alumno["nombre"]}  {alumno["apellido_1"]}")
#
#for materia in alumno["materias"]:
#    print(materia)



alumno = {
    "nombre" : "Benjita", 
    "apellido_1" : "Carmona"
}

print(f"  { alumno["nombre"] }  ")

alumno["nombre"] = input("")

print(f"  { alumno["nombre"] }  ")


