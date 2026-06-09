import random 

print( "lugar = mazmorra divina".lower())
print("heroe = el heroe que es el jugador es un antiheroe / destructor (se hace el malo, sindrome chunnibyou)".upper()) 
print("enemigos = puras westes angelicales ".upper())
print("# 05/06/2026")


HP_INICIAL    = 20
ATK_INICIAL   = 5
SALAS_TOTALES = 3

def crear_jugador (nombre ,profesion,apodo ):
    """ 
    recibe un nombre (string) y devuelve el diccionario con todos los datos del personaje iniciales.
    """
    print(f"[DEBUG] aca se esta creando el personaje con nombre {nombre}")
    jugador = {
        "nombre":    nombre,
        "hp":       HP_INICIAL,
        "hp_max":    HP_INICIAL,
        "atk":       ATK_INICIAL,
        "oro":       0,
        "inventario": ["Poción"],
        "profesion" : profesion,
        "apodo": apodo
    }

    print(f"[DEBUG] creando un apodo al jugador -> {profesion}\n[DEBUG] asignando profesion -> {profesion}\n[DEBUG] creando un apodo al jugador -> {apodo}") 
   
    return jugador
    
nombre_jugador = input("ingresa u nombre a tu heroe: ").upper()
profesion_del_jugador = input("ingresa la profesion de tu heroe y tendras una caracteristica especial. : ")
apodo_del_jugador = input("agrega el apodo que quieres que se refieran a ti : ").lower()

el_jugador = crear_jugador(nombre_jugador, profesion_del_jugador, apodo_del_jugador)

def mostrar_estado_jugador(jugador):
    return jugador

print("\n[INFO] Mostrando estado inicial:")
mostrar_estado_jugador(mi_jugador)











