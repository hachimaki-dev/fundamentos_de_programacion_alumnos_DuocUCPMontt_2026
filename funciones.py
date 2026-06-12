#Sin retorno 

def saludarCompa():
    print("Hola")

def saludarCompaConParametro(nombre_del_compi):
    print(f"Hola {nombre_del_compi}.")

opcion_user = input("1 o 2: ")
if opcion_user == "1":
    saludarCompa()
elif opcion_user == "2":
    nombre = input("Ingrese su nombre: ")
    saludarCompaConParametro(nombre)