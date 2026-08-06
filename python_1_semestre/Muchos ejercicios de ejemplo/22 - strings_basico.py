# ============================================
# 22 - STRINGS (BÁSICO)
# Tema: Creación y operaciones básicas con texto
# Nivel: ⭐ Básico
# ============================================
# Un string (cadena) es una secuencia de caracteres.
# Se puede crear con comillas simples '' o dobles "".

# --- Crear strings ---
nombre = "Carlos"
apellido = 'González'
frase = "Hola, estoy aprendiendo Python"

print(nombre)
print(apellido)
print(frase)

print()

# --- Concatenación (unir textos con +) ---
nombre_completo = nombre + " " + apellido
print("Nombre completo:", nombre_completo)

print()

# --- Longitud de un string con len() ---
mensaje = "Python es genial"
print(f"Mensaje: '{mensaje}'")
print(f"Largo: {len(mensaje)} caracteres")

print()

# --- Acceder a caracteres individuales (índices) ---
# Los índices empiezan en 0
palabra = "Python"
print(f"Palabra: {palabra}")
print(f"Primer carácter:  palabra[0]  = '{palabra[0]}'")
print(f"Segundo carácter: palabra[1]  = '{palabra[1]}'")
print(f"Último carácter:  palabra[-1] = '{palabra[-1]}'")
print(f"Penúltimo:        palabra[-2] = '{palabra[-2]}'")

print()

# --- Repetir un string ---
linea = "=-" * 20
print(linea)
print("¡" + "ja" * 5 + "!")
print(linea)
