lista_de_todos_los_animales = []

def MostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Registrar animal")
    print("2. Buscar animal")
    print("3. Eliminar animal")
    print("4. Actualizar alertas")
    print("5. Mostrar animales")
    print("6. Salir")
    print("=====================================")


def OpcionMenuElejida():
    opcion_elejida = input("que opcion quieres elegir: ")
    if opcion_elejida in ["1","2","3","4","5","6"]:
        return opcion_elejida
    else:
        print("error eliga una de las 6 opciones")

def RegistrarNombreAnimal():
    while True:
        NombreAnimal = input("cual es el nombre de su animal")
        if len (NombreAnimal.strip) <= 0:
                print("nombre invalido")
        else:
            return NombreAnimal
        
def RegistrarRazaAnimal():
    while True:
        RazaAnimal = input("cual es la raza del animal?: ")
        if len (RazaAnimal.strip) <= 0:
            print("nombre invalido")
        else:
            return RazaAnimal
def PesoAnimal():
    while True:
        try:
            PesoAnimal = float(input("cuanto pesa el animal"))
            if PesoAnimal <= 0:
                print("tienes que ser un numero mayor a cero y positivo")
            else:
                return PesoAnimal
        except:
            print("es solo numeros positivos y mayores a 0")

def AgregarAnimal():
   NombreValido = RegistrarNombreAnimal
   RazaValido = RegistrarRazaAnimal
   PesoValido = PesoAnimal
   AnimalAgregado = {
        "nombre": NombreValido,
        "raza": RazaValido,
        "peso": PesoValido,
        "alesta": False

    }
