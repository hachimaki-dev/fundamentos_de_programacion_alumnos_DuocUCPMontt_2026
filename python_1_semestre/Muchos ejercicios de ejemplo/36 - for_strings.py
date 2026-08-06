# ============================================
# 36 - CICLO FOR (CON STRINGS)
# Tema: Recorrer texto carácter por carácter
# Nivel: ⭐⭐ Medio
# ============================================
# El for puede recorrer directamente un string.
# Cada iteración toma un carácter.

# --- Recorrer un string ---
print("=== RECORRER STRING ===")
texto_simple = input("Escribe una palabra: ")

print("Letra por letra:")
for car in texto_simple:
    print(f"  → {car}")

print()

# --- Contar vocales ---
print("=== CONTAR VOCALES ===")
frase_vocal = input("Escribe un texto: ").lower()
lista_vocales = "aeiouáéíóú"
total_vocales = 0

for v_char in frase_vocal:
    if v_char in lista_vocales:
        total_vocales += 1

print(f"El texto tiene {total_vocales} vocales")

print()

# --- Invertir texto ---
print("=== INVERTIR TEXTO ===")
txt_original = input("Texto a invertir: ")
txt_invertido = ""

for char_inv in txt_original:
    txt_invertido = char_inv + txt_invertido  # agrega al inicio

print(f"Original:  {txt_original}")
print(f"Invertido: {txt_invertido}")

# ¿Es palíndromo?
clean_orig = txt_original.lower().replace(" ", "")
clean_inv = txt_invertido.lower().replace(" ", "")
if clean_orig == clean_inv and len(clean_orig) > 0:
    print("🔄 ¡Es un palíndromo!")

print()

# --- Censurar palabras ---
print("=== CENSURAR LETRAS ===")
msg_input = input("Escribe un mensaje: ")
chars_censura = input("¿Qué letras censurar? ")

msg_final = ""
for c_msg in msg_input:
    if c_msg.lower() in chars_censura.lower():
        msg_final += "*"
    else:
        msg_final += c_msg

print(f"Censurado: {msg_final}")

print()

# --- Recorrer con índice ---
print("=== CON ÍNDICE ===")
palabra_idx = input("Palabra: ")

for pos in range(len(palabra_idx)):
    print(f"  Índice {pos}: '{palabra_idx[pos]}'")

