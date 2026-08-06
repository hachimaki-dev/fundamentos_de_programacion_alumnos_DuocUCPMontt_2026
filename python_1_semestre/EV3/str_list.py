# MÉTODOS DE STRINGS (CADENAS DE TEXTO) EN PYTHON
# --- 1. capitalize() ---
# Descripción: Convierte el primer carácter del texto a mayúscula.
texto = "hola mundo"
print("Resultado capitalize():", texto.capitalize())  # Salida: "Hola mundo"

# --- 2. casefold() ---
# Descripción: Convierte el texto a minúsculas de forma más estricta que lower() (ideal para comparar textos).
texto = "Guten TAG"
print("Resultado casefold():", texto.casefold())  # Salida: "guten tag"

# --- 3. center() ---
# Descripción: Devuelve un texto centrado rellenando los lados con un carácter (por defecto espacios).
texto = "Python"
print("Resultado center():", texto.center(12, "-"))  # Salida: "---Python---"

# --- 4. count() ---
# Descripción: Devuelve cuántas veces aparece un valor específico en el texto.
texto = "banana"
print("Resultado count():", texto.count("a"))  # Salida: 3

# --- 5. encode() ---
# Descripción: Devuelve una versión codificada en bytes del texto.
texto = "Café"
print("Resultado encode():", texto.encode("utf-8"))  # Salida: b'Caf\xc3\xa9'

# --- 6. endswith() ---
# Descripción: Devuelve True si el texto termina con el valor especificado.
archivo = "foto.jpg"
print("Resultado endswith():", archivo.endswith(".jpg"))  # Salida: True

# --- 7. expandtabs() ---
# Descripción: Define el tamaño de los espacios para los caracteres de tabulación (\t).
texto = "H\te\ty"
print("Resultado expandtabs():", texto.expandtabs(4))  # Salida: "H   e   y"

# --- 8. find() ---
# Descripción: Busca un valor y devuelve la posición donde inicia. Devuelve -1 si no lo encuentra.
texto = "Hola amigos"
print("Resultado find():", texto.find("amigos"))  # Salida: 5

# --- 9. format() ---
# Descripción: Formatea y reemplaza variables dentro de un texto.
texto = "Hola {nombre}, tienes {edad} años"
print("Resultado format():", texto.format(nombre="Luis", edad=20))

# --- 10. format_map() ---
# Descripción: Formatea elementos de un texto usando un diccionario directamente.
datos = {"x": 10, "y": 20}
texto = "Coordenadas: {x}, {y}"
print("Resultado format_map():", texto.format_map(datos))

# --- 11. index() ---
# Descripción: Busca un valor y devuelve su posición. Da error (ValueError) si no lo encuentra.
texto = "Hola amigos"
print("Resultado index():", texto.index("amigos"))  # Salida: 5

# --- 12. isalnum() ---
# Descripción: Devuelve True si todos los caracteres son alfanuméricos (letras o números, sin espacios).
texto = "Python3"
print("Resultado isalnum():", texto.isalnum())  # Salida: True

# --- 13. isalpha() ---
# Descripción: Devuelve True si todos los caracteres pertenecen al alfabeto (solo letras).
texto = "Hola"
print("Resultado isalpha():", texto.isalpha())  # Salida: True

# --- 14. isascii() ---
# Descripción: Devuelve True si todos los caracteres son caracteres ASCII.
texto = "Hello123"
print("Resultado isascii():", texto.isascii())  # Salida: True

# --- 15. isdecimal() ---
# Descripción: Devuelve True si todos los caracteres son números decimales (0-9).
texto = "123"
print("Resultado isdecimal():", texto.isdecimal())  # Salida: True

# --- 16. isdigit() ---
# Descripción: Devuelve True si todos los caracteres son dígitos (incluye superíndices ²).
texto = "50"
print("Resultado isdigit():", texto.isdigit())  # Salida: True

# --- 17. isidentifier() ---
# Descripción: Devuelve True si el texto es un nombre válido para variables en Python.
texto = "mi_variable"
print("Resultado isidentifier():", texto.isidentifier())  # Salida: True

# --- 18. islower() ---
# Descripción: Devuelve True si todas las letras del texto están en minúscula.
texto = "hola"
print("Resultado islower():", texto.islower())  # Salida: True

# --- 19. isnumeric() ---
# Descripción: Devuelve True si todos los caracteres son numéricos (incluye fracciones como ½).
texto = "100"
print("Resultado isnumeric():", texto.isnumeric())  # Salida: True

# --- 20. isprintable() ---
# Descripción: Devuelve True si todos los caracteres se pueden imprimir en pantalla (falso para \n).
texto = "Hola Mundo"
print("Resultado isprintable():", texto.isprintable())  # Salida: True

# --- 21. isspace() ---
# Descripción: Devuelve True si el texto contiene únicamente espacios en blanco.
texto = "   "
print("Resultado isspace():", texto.isspace())  # Salida: True

# --- 22. istitle() ---
# Descripción: Devuelve True si el texto sigue las reglas de un título (palabras inician con mayúscula).
texto = "Hola Mundo"
print("Resultado istitle():", texto.istitle())  # Salida: True

# --- 23. isupper() ---
# Descripción: Devuelve True si todas las letras del texto están en mayúscula.
texto = "HOLA"
print("Resultado isupper():", texto.isupper())  # Salida: True

# --- 24. join() ---
# Descripción: Une los elementos de una lista/iterable al final de la cadena de texto separadora.
elementos = ["Juan", "Ana", "Luis"]
print("Resultado join():", ", ".join(elementos))  # Salida: "Juan, Ana, Luis"

# --- 25. ljust() ---
# Descripción: Devuelve el texto justificado a la izquierda rellenando los espacios faltantes a la derecha.
texto = "Hola"
print("Resultado ljust():", texto.ljust(10, "."))  # Salida: "Hola......"

# --- 26. lower() ---
# Descripción: Convierte todas las letras del texto a minúsculas.
texto = "HOLA"
print("Resultado lower():", texto.lower())  # Salida: "hola"

# --- 27. lstrip() ---
# Descripción: Elimina los espacios en blanco o caracteres indicados únicamente a la izquierda del texto.
texto = "   hola"
print("Resultado lstrip():", texto.lstrip())  # Salida: "hola"

# --- 28. maketrans() ---
# Descripción: Crea una tabla de traducción para ser utilizada por el método translate().
tabla = str.maketrans("aeiou", "12345")

# --- 29. partition() ---
# Descripción: Divide el texto en tres partes usando un separador y devuelve una tupla.
texto = "quiero-aprender-python"
print("Resultado partition():", texto.partition("-"))  # Salida: ('quiero', '-', 'aprender-python')

# --- 30. replace() ---
# Descripción: Reemplaza un valor específico por otro valor dentro del texto.
texto = "Me gusta Java"
print("Resultado replace():", texto.replace("Java", "Python"))  # Salida: "Me gusta Python"

# --- 31. rfind() ---
# Descripción: Busca un valor de derecha a izquierda y devuelve la última posición donde fue encontrado.
texto = "casa verde, casa azul"
print("Resultado rfind():", texto.rfind("casa"))  # Salida: 12

# --- 32. rindex() ---
# Descripción: Busca un valor de derecha a izquierda y devuelve su última posición (da error si no existe).
texto = "casa verde, casa azul"
print("Resultado rindex():", texto.rindex("casa"))  # Salida: 12

# --- 33. rjust() ---
# Descripción: Devuelve el texto justificado a la derecha rellenando los espacios faltantes a la izquierda.
texto = "Hola"
print("Resultado rjust():", texto.rjust(10, "."))  # Salida: "......Hola"

# --- 34. rpartition() ---
# Descripción: Divide el texto en tres partes usando la última coincidencia del separador de derecha a izquierda.
texto = "quiero-aprender-python"
print("Resultado rpartition():", texto.rpartition("-"))  # Salida: ('quiero-aprender', '-', 'python')

# --- 35. rsplit() ---
# Descripción: Divide el texto empezando desde la derecha usando un separador y devuelve una lista.
texto = "manzana, pera, uva"
print("Resultado rsplit():", texto.rsplit(", ", 1))  # Salida: ['manzana, pera', 'uva']

# --- 36. rstrip() ---
# Descripción: Elimina los espacios en blanco o caracteres indicados únicamente a la derecha del texto.
texto = "hola   "
print("Resultado rstrip():", texto.rstrip())  # Salida: "hola"

# --- 37. split() ---
# Descripción: Divide el texto usando un separador específico y los guarda dentro de una lista.
texto = "Python es genial"
print("Resultado split():", texto.split(" "))  # Salida: ['Python', 'es', 'genial']

# --- 38. splitlines() ---
# Descripción: Divide el texto en los saltos de línea (\n) y devuelve una lista.
texto = "Línea 1\nLínea 2"
print("Resultado splitlines():", texto.splitlines())  # Salida: ['Línea 1', 'Línea 2']

# --- 39. startswith() ---
# Descripción: Devuelve True si el texto comienza con el valor especificado.
texto = "Bienvenidos"
print("Resultado startswith():", texto.startswith("Bien"))  # Salida: True

# --- 40. strip() ---
# Descripción: Elimina todos los espacios en blanco sobrantes tanto al inicio como al final del texto.
texto = "  hola mundo  "
print("Resultado strip():", texto.strip())  # Salida: "hola mundo"

# --- 41. swapcase() ---
# Descripción: Intercambia mayúsculas por minúsculas y viceversa en todo el texto.
texto = "PyThOn"
print("Resultado swapcase():", texto.swapcase())  # Salida: "pYtHoN"

# --- 42. title() ---
# Descripción: Convierte la primera letra de cada palabra del texto a mayúscula.
texto = "hola mundo de python"
print("Resultado title():", texto.title())  # Salida: "Hola Mundo De Python"

# --- 43. translate() ---
# Descripción: Traduce o reemplaza caracteres usando la tabla generada previamente por maketrans().
texto = "hola mundo"
# Usamos la tabla del paso 28 que cambia vocales por números
print("Resultado translate():", texto.translate(tabla))  # Salida: "h4l1 m5nd4"

# --- 44. upper() ---
# Descripción: Convierte todas las letras del texto a mayúsculas completas.
texto = "python"
print("Resultado upper():", texto.upper())  # Salida: "PYTHON"

# --- 45. zfill() ---
# Descripción: Rellena el texto agregando una cantidad específica de ceros (0) al principio.
texto = "75"
print("Resultado zfill():", texto.zfill(5))  # Salida: "00075"