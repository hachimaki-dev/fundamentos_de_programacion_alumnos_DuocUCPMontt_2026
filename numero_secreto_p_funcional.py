from random import randint

# ==========================================
# 1. FUNCIONES PURAS (Lógica y cálculos)
# ==========================================

def ajustar_a_par(numero: int, lim_superior: int) -> int:
    """Ajusta un número para que sea par basándose en las reglas del juego."""
    if numero % 2 == 0:
        return numero
    return numero + 1 if (numero + 1) <= lim_superior else numero - 1

def evaluar_cercania(numero_secreto: int, intento1: int, intento2: int) -> str:
    """Calcula qué intento estuvo más cerca y devuelve el mensaje correspondiente."""
    distancia1 = abs(intento1 - numero_secreto)
    distancia2 = abs(intento2 - numero_secreto)
    
    if distancia1 < distancia2:
        return f"Estuviste más cerca en el primer intento ({intento1})"
    return f"Estuviste más cerca en el segundo intento ({intento2})"

def obtener_pista_direccion(adivinanza: int, numero_secreto: int) -> str:
    """Devuelve si el número secreto es mayor o menor."""
    return "El numero es menor" if adivinanza > numero_secreto else "El numero es mayor"

# ==========================================
# 2. FUNCIONES IMPURAS (Recursión y Estado de E/S)
# ==========================================

def jugar_turno(numero_secreto: int, intento_actual: int = 1, max_intentos: int = 3, historial: tuple = ()) -> None:
    """Función recursiva que maneja el ciclo principal del juego sin usar loops (while/for)."""
    
    adivinanza = int(input("ADIVINA EL NUMERO: "))
    
    # Caso Base 1: El jugador adivina correctamente
    if adivinanza == numero_secreto:
        print("FELICITACIONES, PUDISTE ADIVINAR")
        return # Termina la recursión
        
    # Caso Base 2: El jugador se queda sin intentos
    if intento_actual >= max_intentos:
        print("PERDISTE")
        print("EL NUMERO CORRECTO ERA:", numero_secreto)
        return # Termina la recursión
    
    # Si no ganó ni perdió definitivamente, el juego sigue
    print(obtener_pista_direccion(adivinanza, numero_secreto))
    
    # Actualizamos el historial de forma inmutable creando una nueva tupla
    nuevo_historial = historial + (adivinanza,)
    
    # Lógica condicional para el turno 2 (pista de cercanía)
    if intento_actual == 2:
        print("Te daré una pista:")
        print(evaluar_cercania(numero_secreto, nuevo_historial[0], nuevo_historial[1]))
    
    # Llamada recursiva para el siguiente turno, aumentando el contador inmutablemente
    jugar_turno(numero_secreto, intento_actual + 1, max_intentos, nuevo_historial)

def iniciar_juego() -> None:
    """Función principal que arranca la aplicación (Shell Impuro)."""
    lim_inferior = int(input("Ingrese límite inferior: "))
    lim_superior = int(input("Ingrese límite superior: "))
    
    numero_base = randint(lim_inferior, lim_superior)
    numero_secreto = ajustar_a_par(numero_base, lim_superior)
    
    print("JUGUEMOS ENTONCES....")
    
    # Inicia la recursión
    jugar_turno(numero_secreto)

# Ejecución del programa
if __name__ == "__main__":
    iniciar_juego()