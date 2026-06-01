// ═══════════════════════════════════════════════════════════════
//  📚 Datos de Ejercicios — Patrones y Estructuras de Datos
//  ─────────────────────────────────────────────────────────────
//  Variables globales consumidas por patrones-y-estructuras.html
// ═══════════════════════════════════════════════════════════════

// ── SELECCIÓN MÚLTIPLE ──
const patronesChoiceExercises = [
  {
    title: "Validación de Entradas",
    question: "¿Por qué es importante colocar la conversión `int(input())` dentro de un bloque `try`?",
    options: [
      "Porque acelera la velocidad de ejecución de Python.",
      "Para capturar un potencial ValueError y evitar que el programa se caiga (crash) si el usuario escribe letras.",
      "Porque es la única forma en que Python lee números enteros.",
      "Para forzar que el número ingresado sea siempre par de forma automática."
    ],
    correct: 1,
    explanation: "¡Exacto! Si un usuario escribe texto en lugar de un número, `int()` genera una excepción `ValueError`. El bloque `try/except` captura este error y nos permite controlarlo elegantemente en lugar de que el programa aborte."
  },
  {
    title: "Control de Menús",
    question: "En un menú interactivo con `while True`, ¿cuál es la mejor práctica para leer la opción seleccionada?",
    options: [
      "Convertir siempre la entrada a float con `float(input())` obligatoriamente.",
      "Usar `break` justo antes de leer la opción para evitar bucles infinitos.",
      "Leer la opción como string (`op = input()`) y compararla con texto (ej: `op == '1'`). Así evitamos caídas por ValueError sin necesitar try/except.",
      "Crear un nuevo ciclo `for` que itere la cantidad de opciones del menú."
    ],
    correct: 2,
    explanation: "Leer la opción como string (`input()`) es un excelente truco de simplicidad, ya que comparar strings nunca arrojará un error de tipo numérico, eliminando la necesidad de bloques `try/except` adicionales para la selección del menú."
  },
  {
    title: "Listas de Diccionarios",
    question: "Si declaramos `pacientes = []` y en cada iteración del bucle hacemos `pacientes.append({'nombre': nom, 'edad': ed})`, ¿qué estructura de datos estamos construyendo?",
    options: [
      "Un diccionario de listas.",
      "Una lista de diccionarios (cada elemento de la lista representa una ficha o registro individual).",
      "Una tupla inmutable de conjuntos.",
      "Una lista simple de strings planos."
    ],
    correct: 1,
    explanation: "Se trata de una **lista de diccionarios**. Es la estructura clásica para bases de datos sencillas en memoria, donde la lista almacena la colección general de registros y cada diccionario contiene los atributos con etiquetas (claves) de una entidad."
  },
  {
    title: "El operador 'not in'",
    question: "¿Qué evalúa la expresión `\" \" not in codigo`?",
    options: [
      "Evalúa si el string `codigo` tiene exactamente un espacio en blanco.",
      "Lanza un error si el usuario no ingresa su nombre completo.",
      "Devuelve `True` si el string `codigo` NO contiene ningún espacio en blanco en su interior.",
      "Reemplaza todos los espacios de `codigo` por guiones bajos."
    ],
    correct: 2,
    explanation: "`\" \" not in codigo` verifica que no existan espacios en blanco en la cadena. Es muy útil para validar nombres de usuario o códigos de producto simples que deban ser una sola palabra continua."
  },
  {
    title: "Búsqueda con Normalización",
    question: "Dado `pacientes = [{'nombre': 'Ana', 'edad': 25}]`, ¿cuál es la forma correcta de comparar un nombre ingresado por el usuario con el guardado en la lista sin importar mayúsculas?",
    options: [
      "`if p['nombre'] == busqueda:`",
      "`if p['nombre'].upper() == busqueda.lower():`",
      "`if p['nombre'].lower() == busqueda.lower():`",
      "`if p['nombre'] in busqueda.lower():`"
    ],
    correct: 2,
    explanation: "Ambos textos deben ser convertidos al mismo formato. Usar `.lower()` en ambos lados de la comparación (`p['nombre'].lower() == busqueda.lower()`) garantiza que 'ana', 'Ana', 'ANA' y 'aNa' den coincidencia positiva."
  },
  {
    title: "La regla de oro de .pop()",
    question: "Al realizar una operación de eliminación en una lista por su índice (`lista.pop(i)`) dentro de un ciclo `for` de búsqueda, ¿por qué es crítico ejecutar un `break` inmediatamente después?",
    options: [
      "Porque `.pop()` devuelve el elemento y el programa fallará si no se guarda.",
      "Porque al eliminar un elemento, los índices de los elementos restantes se desplazan a la izquierda, lo que arruina el orden de iteración del bucle activo y causa errores o saltos de elementos.",
      "Para que el sistema operativo libere memoria RAM de inmediato.",
      "Para obligar a Python a ordenar la lista alfabéticamente."
    ],
    correct: 1,
    explanation: "Modificar el tamaño de una lista mientras se itera sobre sus índices usando un `for` regular cambia la estructura de la lista en vivo. Usar `break` detiene el recorrido justo después de la eliminación del elemento encontrado, evitando errores de desborde de índice (`IndexError`)."
  }
];

// ── VERDADERO O FALSO ──
const patronesTfExercises = [
  {
    title: "Doble validación isalnum y espacios",
    statement: "Si utilizas `codigo.isalnum()` para validar una entrada, la validación `\" \" not in codigo` es técnicamente redundante porque los espacios en blanco no son caracteres alfanuméricos.",
    correct: true,
    explanation: "¡Verdadero! Los caracteres alfanuméricos en Python son únicamente letras (a-z, A-Z) y números (0-9). Un espacio en blanco ' ' no es alfanumérico, por lo que `isalnum()` ya garantiza que no habrá espacios."
  },
  {
    title: "El error KeyError con variables no inicializadas",
    statement: "Intentar acceder a `paciente['nom']` cuando la clave fue guardada como `{'nombre': nom}` generará un error de tipo `KeyError` que detendrá el programa si no se maneja.",
    correct: true,
    explanation: "¡Verdadero! Python es estricto con las claves de los diccionarios. Si intentas buscar una etiqueta que no existe exactamente con corchetes, lanza un `KeyError`. Es por ello que debemos cuidar la consistencia en el uso de los nombres de claves (por ejemplo, usar siempre `'nombre'`)."
  },
  {
    title: "Diferencia lógica entre biblioteca y estacionamiento",
    statement: "En el sistema de biblioteca (Ejercicio 5) y el de estacionamiento (Ejercicio 6), registrar un préstamo de libro y registrar una entrada de auto tienen comportamientos opuestos sobre la variable de stock disponible.",
    correct: false,
    explanation: "¡Falso! Ambos eventos disminuyen el stock disponible. El préstamo reduce los libros disponibles en biblioteca y la entrada de un auto reduce los espacios de estacionamiento libres. Tienen exactamente la misma lógica de negocio respecto a las unidades de stock."
  },
  {
    title: "Validación de try/except externa",
    statement: "Si un bloque `try` está ubicado afuera del bucle `while True` de validación (por ejemplo, envolviendo al bucle entero), el programa se mantendrá preguntando en caso de error de entrada.",
    correct: false,
    explanation: "¡Falso! Si el `try-except` envuelve al `while True` por fuera, cuando ocurra un error el flujo saltará al bloque `except` y se saldrá permanentemente del bucle. Para repetir la pregunta, el `try-except` debe ir **dentro** del bucle."
  },
  {
    title: "Actualización de listas con enumerate",
    statement: "Al usar `for i, p in enumerate(productos):`, la variable `i` guarda la posición del elemento actual en la lista, permitiéndonos realizar modificaciones directas como `productos[i]['stock'] = nuevo_value`.",
    correct: true,
    explanation: "¡Verdadero! `enumerate()` es la herramienta ideal para CRUD en listas, ya que nos entrega el índice numérico `i` que necesitamos para reescribir o borrar elementos específicos usando índices."
  },
  {
    title: "Acumuladores vs Contadores",
    statement: "Un contador suma valores variables a lo largo de un bucle (como sumarle el precio de cada producto al total), mientras que un acumulador siempre incrementa en una cantidad fija como +1.",
    correct: false,
    explanation: "¡Falso! Es exactamente al revés. Un **contador** incrementa en una cantidad fija (habitualmente +1 para llevar un conteo de ítems), mientras que un **acumulador** suma valores variables (como acumular montos de compras u horas trabajadas)."
  }
];

// ── DEPURACIÓN (ENCUENTRA EL ERROR) ──
const patronesErrorExercises = [
  {
    title: "El KeyError en Búsquedas",
    code: `pacientes = [
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Pedro", "edad": 30}
]

busq = input("Nombre a buscar: ").lower()
encontrado = False

for p in pacientes:
    # Intento de comparación
    if p["nom"].lower() == busq:
        print(f"Encontrado! Edad: {p['edad']}")
        encontrado = True
        break

if not encontrado:
    print("Paciente no encontrado.")`,
    question: "¿Qué error ocurrirá en tiempo de ejecución al buscar un paciente con este código?",
    options: [
      "El programa funcionará, pero siempre dirá 'Paciente no encontrado'.",
      "Ocurrirá un `KeyError: 'nom'` debido a que los diccionarios tienen la clave 'nombre' y no 'nom'.",
      "Ocurrirá un `ValueError` porque no se puede convertir un diccionario a lower.",
      "El programa entrará en un bucle infinito en el ciclo for."
    ],
    correct: 1,
    explanation: "¡Exacto! Los diccionarios en la lista tienen la clave `'nombre'`. Al intentar acceder a `p['nom']`, Python lanza un `KeyError` y detiene el script. Para corregirlo, se debe cambiar a `p['nombre']`."
  },
  {
    title: "Bucle de Validación Roto",
    code: `try:
    while True:
        edad = int(input("Ingresa tu edad: "))
        if edad > 0:
            print(f"Edad registrada: {edad}")
            break
        else:
            print("Entrada inválida.")
except ValueError:
    print("Entrada inválida. Ingresa un número entero.")`,
    question: "¿Qué sucede en este código si el usuario ingresa letras (por ejemplo, 'hola') en el primer intento?",
    options: [
      "Muestra el mensaje del except y vuelve a pedir la edad inmediatamente.",
      "El programa se cae con un error en pantalla.",
      "Muestra el error y termina el programa, sin dar la oportunidad de reintentar.",
      "Se ejecuta el print('Edad registrada: hola')."
    ],
    correct: 2,
    explanation: "Como el bloque `try/except` está **fuera** del bucle `while True`, la excepción `ValueError` hace que el flujo del programa salte directamente al `except` saliendo del bucle. El programa imprime el mensaje de error y finaliza. Para que vuelva a preguntar, el `try` debe estar **dentro** del `while`."
  },
  {
    title: "Eliminación Insegura",
    code: `productos = [
    {"nombre": "Arroz", "stock": 50},
    {"nombre": "Aceite", "stock": 20}
]

eliminar = "Arroz"

for i, p in enumerate(productos):
    if p["nombre"] == eliminar:
        productos.pop(i)
        # Falta algo aquí...

print("Lista actualizada:", productos)`,
    question: "Si tuviéramos una lista muy larga de productos y elimináramos elementos iterando sin un `break` justo después de `productos.pop(i)`, ¿qué problema severo podría ocurrir?",
    options: [
      "Se duplicará el producto eliminado.",
      "La lista se vaciará por completo de forma aleatoria.",
      "Se producirá un `IndexError: pop index out of range` o se omitirá la validación del siguiente elemento debido al desplazamiento de índices.",
      "El programa guardará el cambio en el disco duro automáticamente."
    ],
    correct: 2,
    explanation: "Al usar `.pop(i)`, los elementos restantes de la lista se mueven una posición a la izquierda. Si el ciclo `for` continúa iterando con el índice viejo, podría saltarse elementos o arrojar un `IndexError` por desborde. El `break` es crucial tras el `.pop()`."
  },
  {
    title: "El Menú Inalcanzable",
    code: `total = 0
while True:
    print("1. Sumar 2. Salir")
    op = input("Elige: ")
    
    if op == 1:
        num = int(input("Número: "))
        total += num
    elif op == 2:
        print("Adiós!")
        break`,
    question: "Si el usuario elige la opción '2', ¿por qué el programa no sale del bucle?",
    options: [
      "Porque el `break` no funciona dentro de sentencias if/elif.",
      "Porque `op` se lee con `input()` como texto ('2'), pero el condicional lo compara con el número entero `2` (`op == 2` es falso).",
      "Porque la variable `total` debe ser global.",
      "Porque falta definir un `except ValueError` para la opción."
    ],
    correct: 1,
    explanation: "En Python, el string `'2'` y el entero `2` son tipos distintos y su comparación devuelve `False`. Como `op` se almacena como string mediante `input()`, las condiciones debieron ser `op == '1'` y `op == '2'`."
  }
];

// ── COMPLETAR CÓDIGO (FILL IN THE BLANKS) ──
const patronesCompleteExercises = [
  {
    title: "Validar código de atleta",
    code: `def validar_codigo(codigo):
    # Validar mínimo 5 caracteres, sin espacios y alfanumérico
    if len(codigo) >= 5 and " " ________ codigo and codigo.________():
        return True
    return False`,
    question: "¿Qué operadores y métodos completan la validación correcta del código según los requisitos?",
    options: [
      "`in` / `isdigit`",
      "`not in` / `isalnum`",
      "`==` / `isalpha`",
      "`not in` / `isspace`"
    ],
    correct: 1,
    explanation: "Usar `' ' not in codigo` asegura que no contenga espacios, y `codigo.isalnum()` valida que contenga solo letras y números de forma conjunta."
  },
  {
    title: "Validación Robusta",
    code: `while True:
    try:
        edad = int(input("Ingresa edad: "))
        if edad > 0:
            ________  # Entrada válida, romper ciclo
        else:
            print("Debe ser mayor a 0")
    ________ ValueError:
        print("Ingresa un número válido")`,
    question: "¿Qué palabras clave de control de flujo completan el bucle de validación infinita?",
    options: [
      "`continue` / `catch`",
      "`break` / `except`",
      "`return` / `except`",
      "`break` / `error`"
    ],
    correct: 1,
    explanation: "`break` interrumpe el ciclo `while True` cuando la edad es válida, y `except ValueError` captura el error si la conversión `int()` falla."
  },
  {
    title: "CRUD - Modificar Stock",
    code: `productos = [{"nombre": "Pan", "stock": 10}]
buscar = "Pan"
nuevo_stock = 15

for i, p in ________(productos):
    if p["nombre"] == buscar:
        ________[i]["stock"] = nuevo_stock
        break`,
    question: "¿Qué funciones y variables completan la modificación de inventario?",
    options: [
      "`range` / `p`",
      "`enumerate` / `productos`",
      "`enumerate` / `p`",
      "`list` / `productos`"
    ],
    correct: 1,
    explanation: "Usamos `enumerate(productos)` para obtener el índice `i`, y luego modificamos la lista original directamente en `productos[i]['stock']`."
  },
  {
    title: "Límite superior de devolución",
    code: `libros_disponibles = 25
CAPACIDAD_MAX = 30

devolucion = int(input("Devolver cuántos: "))
# Evitar superar la capacidad máxima de la biblioteca
if devolucion > 0 and libros_disponibles + devolucion ________ CAPACIDAD_MAX:
    libros_disponibles += devolucion
    print("Devolución exitosa!")
else:
    print("Error de capacidad.")`,
    question: "¿Qué operador de comparación lógica asegura que el stock no exceda la capacidad máxima?",
    options: [
      "`>`",
      "`==`",
      "`<=`",
      "`>=`"
    ],
    correct: 2,
    explanation: "El operador menor o igual (`<=`) asegura que la suma de los libros actuales y los devueltos no sea mayor a la capacidad máxima de 30 libros."
  }
];

// ── TABLAS DE RECORRIDO (TRAZAR CÓDIGO) ──
const patronesTraceExercises = [
  {
    title: "Promedio de Membresía",
    code: `miembros = [
    {"nombre": "A", "meses": 12},
    {"nombre": "B", "meses": 4},
    {"nombre": "C", "meses": 8}
]
suma = 0
for m in miembros:
    suma += m["meses"]
prom = suma / len(miembros)`,
    question: "¿Cuál es el valor final de la variable `prom` y cuántas iteraciones hizo el bucle?",
    options: [
      "prom = 8.0, iteraciones = 3",
      "prom = 7.33, iteraciones = 3",
      "prom = 24.0, iteraciones = 3",
      "prom = 8.0, iteraciones = 2"
    ],
    correct: 0,
    explanation: "La suma de los meses es `12 + 4 + 8 = 24`. La longitud es `3` (tres miembros en la lista). Así, `24 / 3 = 8.0`. El bucle realiza exactamente 3 iteraciones (una por miembro)."
  },
  {
    title: "Filtrar Voluntarios",
    code: `voluntarios = [
    {"nom": "Alpha", "horas": 10},
    {"nom": "Beta", "horas": 25},
    {"nom": "Gamma", "horas": 30}
]
dedicados = 0
for v in voluntarios:
    if v["horas"] > 20:
        dedicados += 1`,
    question: "¿Cuál es el valor de la variable `dedicados` al finalizar el código?",
    options: [
      "dedicados = 0",
      "dedicados = 1",
      "dedicados = 2",
      "dedicados = 3"
    ],
    correct: 2,
    explanation: "El condicional evalúa si `horas > 20`. Para 'Alpha' es `10 > 20` (Falso). Para 'Beta' es `25 > 20` (Verdadero). Para 'Gamma' es `30 > 20` (Verdadero). Por lo tanto, `dedicados` se incrementa dos veces y su valor final es 2."
  }
];
