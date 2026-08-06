# ============================================
# 30 - CICLO WHILE (BREAK Y CONTINUE)
# Tema: Controlar el flujo del bucle
# Nivel: ⭐⭐⭐ Intermedio
# ============================================
# break    = sale del bucle inmediatamente
# continue = salta al siguiente ciclo (no ejecuta lo que sigue)
# else     = se ejecuta si el while terminó normalmente (sin break)

# --- BREAK: salir del bucle ---
print("=== BREAK ===")
print("Escribe palabras. Escribe 'salir' para terminar.")

while True:  # bucle "infinito" controlado con break
    palabra = input("> ")
    if palabra.lower() == "salir":
        print("👋 ¡Hasta luego!")
        break
    print(f"  Escribiste: '{palabra}' ({len(palabra)} caracteres)")

print()

# --- CONTINUE: saltar iteración ---
print("=== CONTINUE ===")
print("Números del 1 al 10, saltando los múltiplos de 3:")

i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue  # salta el print, vuelve al inicio del while
    print(i, end=" ")

print()  # nueva línea
print()

# --- Ejemplo combinado: filtrar números ---
print("=== FILTRAR NÚMEROS ===")
print("Ingresa números. Solo sumaré los positivos. Escribe -999 para terminar.")

suma_positivos = 0
negativos_saltados = 0

while True:
    num = int(input("Número: "))
    
    if num == -999:
        break           # señal de salida
    
    if num < 0:
        negativos_saltados += 1
        continue        # no sumar negativos
    
    suma_positivos += num

print(f"\nSuma de positivos: {suma_positivos}")
print(f"Negativos ignorados: {negativos_saltados}")

print()

# --- WHILE...ELSE ---
print("=== WHILE...ELSE ===")
print("Buscando el primer múltiplo de 7 entre tus números...")
print("(Ingresa 0 para dejar de buscar)")

encontrado = False
while True:
    n = int(input("Número: "))
    if n == 0:
        break
    if n % 7 == 0:
        print(f"¡Encontrado! {n} es múltiplo de 7")
        encontrado = True
        break

if not encontrado:
    print("No se encontró ningún múltiplo de 7")

