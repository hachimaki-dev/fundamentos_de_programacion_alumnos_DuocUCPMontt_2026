class Persona:
    def __init__(self, nombre, estatura, edad):
        self.nombre = nombre
        self.estatura = estatura
        self.edad = edad

    def MostrarDescripcion(self):
        print(f"Hola, mis datos son: \nNombre: {self.nombre} \nEstatura: {self.estatura} \nEdad: {self.edad}")

def MultiplicarNumeros(num1, num2):
    result = num1 * num2
    return result

def MostrarDescripcionDeTodos():
    for p in personas:
        p.MostrarDescripcion()
        print("")

def AddPerson(person):
    personas.append(person)

personas = []

p1 = Persona("Camilo", 1.76, 27)
p2 = Persona("Cristian", 1.74, 27)

AddPerson(p1)
AddPerson(p2)

MostrarDescripcionDeTodos()