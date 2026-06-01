Python

import random

limite_inferior_rango = int(input("Ingrese límite inferior del rango: "))
limite_superior_rango = int(input("Ingrese límite superior del rango: "))

numero_aleatorio_generado = random.randint(limite_inferior_rango, limite_superior_rango)
numero_secreto_par = numero_aleatorio_generado

# Ajuste lógico para asegurar que el número secreto sea siempre par
if numero_secreto_par % 2 != 0:  # Si es impar
    if numero_secreto_par + 1 <= limite_superior_rango:
        numero_secreto_par = numero_secreto_par + 1
    else:
        numero_secreto_par = numero_secreto_par - 1

A continuación, las 3 lógicas replanteadas con nombres altamente descriptivos:
Lógica 1: Ciclo for (Enfoque clásico y estructurado)

Aquí nombraremos claramente el número de la ronda actual y el valor que se debe guardar del primer intento.
Python

valor_ingresado_primer_intento = 0

for numero_de_intento_actual in range(1, 4):
    valor_ingresado_por_usuario = int(input(f"\nRonda {numero_de_intento_actual} - Ingresa un número: "))
    
    # 1. Caso de éxito
    if valor_ingresado_por_usuario == numero_secreto_par:
        print(f"Felicitaciones, pudiste adivinar en tu intento número {numero_de_intento_actual}.")
        break 
        
    # 2. Caso de fallo en la última ronda posible
    elif numero_de_intento_actual == 3:
        print(f"Perdiste. El número era: {numero_secreto_par}")
        
    # 3. Casos de fallo en rondas 1 y 2 (Retroalimentación)
    else:
        if valor_ingresado_por_usuario > numero_secreto_par:
            print("El número secreto es menor al que ingresaste.")
        else:
            print("El número secreto es mayor al que ingresaste.")
            
        # Pista especial: Guardar dato en ronda 1, mostrar pista en ronda 2
        if numero_de_intento_actual == 1:
            valor_ingresado_primer_intento = valor_ingresado_por_usuario
            
        elif numero_de_intento_actual == 2:
            print(f"Pista: El número secreto está más cerca de {valor_ingresado_por_usuario} (tu intento actual) que de {valor_ingresado_primer_intento} (tu primer intento).")

Lógica 2: Ciclo while apoyado en Listas (Enfoque de historial)

Llamaremos a la lista como un "historial" y dejaremos claro cuántos intentos se han consumido.
Python

cantidad_de_intentos_consumidos = 0
historial_de_valores_ingresados = []

while cantidad_de_intentos_consumidos < 3:
    numero_de_ronda_actual = cantidad_de_intentos_consumidos + 1
    valor_ingresado_por_usuario = int(input(f"\nIntente adivinar (Ronda {numero_de_ronda_actual}): "))
    
    historial_de_valores_ingresados.append(valor_ingresado_por_usuario)
    cantidad_de_intentos_consumidos = cantidad_de_intentos_consumidos + 1
    
    if valor_ingresado_por_usuario == numero_secreto_par:
        print("Felicitaciones, pudiste adivinar.")
        break
        
    if cantidad_de_intentos_consumidos == 3:
        print(f"Perdiste. El número secreto era: {numero_secreto_par}")
    else:
        # Pistas de mayor o menor
        if valor_ingresado_por_usuario < numero_secreto_par:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")
            
        # La posición 0 de la lista es el intento 1, la posición 1 es el intento 2
        if cantidad_de_intentos_consumidos == 2:
            valor_intento_uno = historial_de_valores_ingresados[0]
            valor_intento_dos = historial_de_valores_ingresados[1]
            print(f"Pista: El número que buscas está más cerca de {valor_intento_dos} que de {valor_intento_uno}.")

Lógica 3: Enfoque Modular (Funciones secuenciales explícitas)

Al hacer el código verboso y explícito, esta versión evita los ciclos por completo y trata cada intento como un bloque de código separado dentro de una función con un nombre descriptivo.
Python

def ejecutar_juego_de_adivinanza(valor_numero_secreto_par):
    valor_ingresado_primer_intento = 0
    
    # --- RONDA 1 ---
    valor_ingresado_por_usuario = int(input("Intento 1 - Adivina el número: "))
    if valor_ingresado_por_usuario == valor_numero_secreto_par:
        print("Felicitaciones, adivinaste en tu primer intento.")
        return # Termina la ejecución de la función
    
    if valor_ingresado_por_usuario < valor_numero_secreto_par:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
        
    valor_ingresado_primer_intento = valor_ingresado_por_usuario
    
    # --- RONDA 2 ---
    valor_ingresado_por_usuario = int(input("Intento 2 - Adivina el número: "))
    if valor_ingresado_por_usuario == valor_numero_secreto_par:
        print("Felicitaciones, adivinaste en tu segundo intento.")
        return 
    
    if valor_ingresado_por_usuario < valor_numero_secreto_par:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
        
    print(f"Pista: El número que buscas está más cerca de {valor_ingresado_por_usuario} que de {valor_ingresado_primer_intento}.")
    
    # --- RONDA 3 ---
    valor_ingresado_por_usuario = int(input("Intento 3 - Adivina el número: "))
    if valor_ingresado_por_usuario == valor_numero_secreto_par:
        print("Felicitaciones, adivinaste en tu tercer intento.")
        return
        
    # Si llega hasta aquí, agotó sus tres rondas sin entrar a ningún 'return'
    print(f"Perdiste. El número secreto era: {valor_numero_secreto_par}")

# Se llama a la función pasándole el número generado en el código base
ejecutar_juego_de_adivinanza(numero_secreto_par)