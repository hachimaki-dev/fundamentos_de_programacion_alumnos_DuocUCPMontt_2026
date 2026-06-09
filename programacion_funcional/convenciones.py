import logging
logging.basicConfig(level=logging.DEBUG)# log es registro/s es archivo o mensaje que documenta eventos y actividades en la exe del programa

nombre_jugador = "ana"# snake case es cuando separas los strs con guiones/bajos (_)
vida_maxima = 20
def crear_jugador():
    pass

HP_INICIAL = 20 #CONSTANTES EN UPPER_SNAKE_CASE strs mayus con (_)
SALAS_TOTALES = 20
DANO_DRUIDA = 2

""" 
1. Misión del logging (DEBUG, INFO, ERROR)Su objetivo es la observabilidad y auditoría del sistema 
[2]:Rastreo de fallos: Saber exactamente qué línea falló y por qué (ERROR/CRITICAL) 
[2, 3].Historial de actividad: Registrar acciones importantes, como "Usuario X inició sesión" (INFO) [2, 3].Depuración técnica: Ver el valor de variables internas mientras desarrollas (DEBUG) [2, 3].
"""

# ✅ Prints con etiqueta — fácil de identificar y borrar después
# print("[DEBUG] Entrando a la función atacar")
# print(f"[DEBUG] Valor de dano calculado: {dano}")
# print("[INFO] Jugador creado correctamente")
# print("[ERROR] El inventario está vacío cuando no debería")

logging.debug("mensaje")
