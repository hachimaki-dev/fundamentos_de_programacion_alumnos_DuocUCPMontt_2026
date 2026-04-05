# Título de la trivia
print("--- BIENVENIDO A LA TRIVIA DE PYTHON ---")

# --- PREGUNTA 1 ---
error_pregunta1 = True

while error_pregunta1:
    respuesta1 = input("\n1. ¿Cuál es el símbolo para comentarios en Python? (# o //): ")
    
    if respuesta1 == "#":
        print("¡Correcto!")
        error_pregunta1 = False  # Cambiamos a False para SALIR del bucle
    else:
        print("Incorrecto. Pista: Es el que usas para 'comentar' líneas.")

# --- PREGUNTA 2 ---
error_pregunta2 = True

while error_pregunta2:
    respuesta2 = input("\n2. ¿Cómo se llama el bucle que se repite 'mientras' algo es verdad?: ")
    
    if respuesta2.lower() == "while":
        print("¡Exacto!")
        error_pregunta2 = False  # Se abre la compuerta
    else:
        print("Casi... empieza con 'w'.")

# --- FINAL ---
print("\n¡Felicidades! Pasaste todas las compuertas de la trivia.")
