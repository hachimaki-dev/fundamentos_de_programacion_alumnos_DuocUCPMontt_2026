import random

# ═══════════════════════════════════════════
# CONSTANTES DEL JUEGO
# ═══════════════════════════════════════════
HP_INICIAL    = 20
ATK_INICIAL   = 5
SALAS_TOTALES = 3

# ═══════════════════════════════════════════
# FUNCIONES DE CREACIÓN
# ═══════════════════════════════════════════

def crear_jugador(nombre):
    """
    Recibe un nombre (string) y devuelve un diccionario
    con todos los datos iniciales del jugador.
    """
    print(f"[DEBUG] Creando jugador con nombre: {nombre}")

    jugador = {
        "nombre":    nombre,
        "hp":        HP_INICIAL,
        "hp_max":    HP_INICIAL,
        "atk":       ATK_INICIAL,
        "oro":       0,
        "inventario": ["Poción"]
    }

    print(f"[DEBUG] Jugador creado → {jugador}")
    return jugador


# ═══════════════════════════════════════════
# PRUEBA TEMPORAL (lo borraremos después)
# ═══════════════════════════════════════════
nombre_ingresado = input("¿Cómo se llama tu héroe? ")
mi_jugador = crear_jugador(nombre_ingresado)
print("\n[INFO] Resultado final:")
print(mi_jugador)