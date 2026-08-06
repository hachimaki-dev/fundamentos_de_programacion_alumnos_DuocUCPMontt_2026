opcion_elegida = 0

print("=== BIENVENIDO AL SISTEMA CAZABICHOS! ===")

def mostrar_menu():
    print("\nMENÚ")
    print("1.- AGREGAR BICHO")
    print("2.- BUSCAR BICHO")
    print("3.- ELIMINAR BICHO")
    print("4.- ACTUALIZAR ESTADOS")
    print("5.- MOSTRAR BICHOS")
    print("6.- SALIR")

def seleccionar_opcion():
    while True:
        try:
            opcion_elegida = int(input("\nSeleccione una opcion: "))
        except ValueError:
            print("ERROR, ingrese numeros enteros positivos")
        if opcion_elegida <= 0:
            print("ERROR, ingrese numero mayores que 0")



