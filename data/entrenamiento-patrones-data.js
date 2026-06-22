// ═══════════════════════════════════════════════════════════════
//  🎮 Datos — Entrenamiento Progresivo de Patrones
//  ─────────────────────────────────────────────────────────────
//  7 niveles, ~65 ejercicios interactivos.
//  Temática: Sistema de Pociones Mágicas (nombre, poder, activa)
//  Patrones que preparan para la Evaluación Parcial 4.
// ═══════════════════════════════════════════════════════════════

// ── NIVEL 1 — Lista vacía + append de diccionarios ──────────

const nivel1Lesson = {
  title: 'Lista vacía + diccionarios',
  emoji: '📦',
  intro: 'Todo sistema de gestión comienza con una <strong>lista vacía</strong> que se va llenando con <strong>diccionarios</strong>. Cada diccionario es un "registro" o "ficha" con campos etiquetados.',
  code: `pociones = []  # lista vacía — aquí se guardarán todas las pociones

# Crear un diccionario (una ficha de poción)
pocion = {
    "nombre": "Elixir de Fuego",
    "poder": 8,
    "activa": False
}

# Agregar el diccionario a la lista
pociones.append(pocion)

print(pociones)
# [{"nombre": "Elixir de Fuego", "poder": 8, "activa": False}]
print(len(pociones))  # 1`,
  keyPoints: [
    '<code>[]</code> crea una lista vacía, <code>{}</code> crea un diccionario vacío — ¡no confundir!',
    'Cada diccionario tiene pares <strong>clave: valor</strong> (ej: <code>"nombre": "Elixir"</code>)',
    '<code>.append()</code> agrega un elemento al final de la lista',
    'El campo <code>"activa": False</code> lo asigna el sistema, no el usuario'
  ]
};

const nivel1Tf = [
  {
    title: 'Lista vs Diccionario',
    code: 'pociones = {}',
    question: '¿La línea anterior crea una lista vacía para guardar pociones?',
    correct: false,
    explanation: '<strong>Falso.</strong> <code>{}</code> crea un <strong>diccionario vacío</strong>, no una lista. Para crear una lista vacía se usa <code>[]</code>. Es una trampa clásica: <code>pociones = []</code> es lo correcto.'
  },
  {
    title: 'Append y diccionarios',
    code: `pociones = []
pocion = {"nombre": "Veneno", "poder": 3, "activa": False}
pociones.append(pocion)
print(len(pociones))`,
    question: '¿Este código imprime <code>1</code>?',
    correct: true,
    explanation: '<strong>Verdadero.</strong> Se crea una lista vacía, luego se agrega UN diccionario con <code>.append()</code>. La lista ahora tiene 1 elemento, así que <code>len(pociones)</code> retorna <code>1</code>.'
  },
  {
    title: 'Campo automático',
    code: `pocion = {"nombre": "Curación", "poder": 5}`,
    question: '¿Este diccionario tiene el campo <code>"activa"</code>?',
    correct: false,
    explanation: '<strong>Falso.</strong> El diccionario solo tiene las claves que tú le pongas. Si necesitas que tenga <code>"activa": False</code> debes incluirlo explícitamente al crear el diccionario.'
  }
];

const nivel1Choice = [
  {
    title: '¿Qué estructura estamos construyendo?',
    code: `pociones = []
pociones.append({"nombre": "Fuego", "poder": 8, "activa": False})
pociones.append({"nombre": "Hielo", "poder": 5, "activa": False})`,
    question: '¿Qué tipo de estructura de datos es <code>pociones</code> después de ejecutar este código?',
    options: [
      'Un diccionario de listas',
      'Una lista de diccionarios — cada elemento es un registro individual',
      'Una tupla de strings',
      'Un diccionario con dos claves: "Fuego" y "Hielo"'
    ],
    correct: 1,
    explanation: '<code>pociones</code> es una <strong>lista de diccionarios</strong>. La lista actúa como la colección general, y cada diccionario es un registro individual (una poción) con sus campos etiquetados.'
  },
  {
    title: 'Agregar correctamente',
    question: '¿Cuál línea agrega correctamente una poción a la lista?',
    options: [
      '<code>pociones.add({"nombre": "Rayo", "poder": 6, "activa": False})</code>',
      '<code>pociones.append({"nombre": "Rayo", "poder": 6, "activa": False})</code>',
      '<code>pociones.insert({"nombre": "Rayo", "poder": 6, "activa": False})</code>',
      '<code>pociones + {"nombre": "Rayo", "poder": 6, "activa": False}</code>'
    ],
    correct: 1,
    explanation: 'El método correcto para agregar al final de una lista es <code>.append()</code>. Python no tiene <code>.add()</code> para listas (eso es de conjuntos). <code>.insert()</code> necesita una posición como primer argumento.'
  },
  {
    title: 'Acceder a un campo',
    code: `pociones = [{"nombre": "Fuego", "poder": 8, "activa": False}]
print(pociones[0]["nombre"])`,
    question: '¿Qué imprime este código?',
    options: [
      '<code>{"nombre": "Fuego", "poder": 8, "activa": False}</code>',
      '<code>Fuego</code>',
      '<code>0</code>',
      'Da error porque no se puede usar <code>[0]</code> con <code>["nombre"]</code>'
    ],
    correct: 1,
    explanation: '<code>pociones[0]</code> obtiene el primer diccionario de la lista. Luego <code>["nombre"]</code> accede al valor de la clave "nombre" dentro de ese diccionario. Resultado: <code>Fuego</code>.'
  }
];

const nivel1Trace = [
  {
    title: '¿Cuántos elementos?',
    code: `pociones = []
pociones.append({"nombre": "A", "poder": 1, "activa": False})
pociones.append({"nombre": "B", "poder": 2, "activa": False})
pociones.append({"nombre": "C", "poder": 3, "activa": False})
print(len(pociones))`,
    question: '¿Qué imprime este código?',
    options: ['<code>0</code>', '<code>1</code>', '<code>3</code>', '<code>9</code>'],
    correct: 2,
    explanation: 'Se agregan 3 diccionarios a la lista con <code>.append()</code>. <code>len(pociones)</code> retorna <code>3</code>.'
  },
  {
    title: 'Completar el registro',
    code: `def crear_pocion(nombre, poder):
    pocion = {
        "nombre": _____,
        "poder": _____,
        "activa": _____
    }
    return pocion`,
    question: '¿Qué va en los espacios <code>_____</code> para crear correctamente el diccionario?',
    options: [
      '<code>nombre</code>, <code>poder</code>, <code>True</code>',
      '<code>"nombre"</code>, <code>"poder"</code>, <code>False</code>',
      '<code>nombre</code>, <code>poder</code>, <code>False</code>',
      '<code>input()</code>, <code>int(input())</code>, <code>False</code>'
    ],
    correct: 2,
    explanation: 'Los valores deben ser las <strong>variables</strong> (sin comillas): <code>nombre</code> y <code>poder</code>, que son los parámetros de la función. El campo <code>"activa"</code> siempre inicia en <code>False</code>.'
  }
];


// ── NIVEL 2 — Validar nombre (no vacío, no solo espacios) ───

const nivel2Lesson = {
  title: 'Validar nombre',
  emoji: '✍️',
  intro: 'Cuando el usuario ingresa un nombre, debemos verificar que <strong>no esté vacío</strong> y que <strong>no sea solo espacios en blanco</strong>. El método <code>.strip()</code> es tu aliado.',
  code: `# .strip() elimina espacios al inicio y al final
print("  Ragnar  ".strip())   # "Ragnar"
print("   ".strip())          # "" (string vacío)
print("".strip())             # "" (sigue vacío)

# Función de validación — retorna True o False
def validar_nombre(nombre):
    return nombre.strip() != ""

# Uso en el programa
print(validar_nombre("Ragnar"))   # True
print(validar_nombre("   "))      # False
print(validar_nombre(""))         # False`,
  keyPoints: [
    '<code>.strip()</code> retorna una copia SIN espacios al inicio ni al final',
    '<code>"   ".strip()</code> → <code>""</code> (string vacío)',
    'La función de validación solo dice <strong>True o False</strong> — no imprime mensajes de error',
    'Los mensajes de error van en la función que <strong>llama</strong> a la validación (separación de responsabilidades)'
  ]
};

const nivel2Tf = [
  {
    title: 'El truco de strip()',
    code: '"   ".strip()',
    question: '¿<code>"   ".strip()</code> retorna <code>"   "</code> (los mismos 3 espacios)?',
    correct: false,
    explanation: '<strong>Falso.</strong> <code>.strip()</code> elimina TODOS los espacios del inicio y final. <code>"   ".strip()</code> retorna <code>""</code> (string vacío), porque el string era solo espacios.'
  },
  {
    title: 'Validación incompleta',
    code: `nombre = "   "
if nombre != "":
    print("Nombre válido")`,
    question: '¿Este código imprime <code>"Nombre válido"</code> cuando el nombre es solo espacios?',
    correct: true,
    explanation: '<strong>Verdadero</strong> (¡y eso es un BUG!). <code>"   " != ""</code> es <code>True</code> porque el string tiene 3 caracteres (espacios). Sin <code>.strip()</code>, la validación no detecta nombres que son solo espacios.'
  },
  {
    title: 'Validación correcta',
    code: `def validar_nombre(nombre):
    return nombre.strip() != ""

print(validar_nombre("  Lyra  "))`,
    question: '¿Este código imprime <code>True</code>?',
    correct: true,
    explanation: '<strong>Verdadero.</strong> <code>"  Lyra  ".strip()</code> retorna <code>"Lyra"</code>, que NO es igual a <code>""</code>. Entonces <code>"Lyra" != ""</code> es <code>True</code>.'
  }
];

const nivel2Choice = [
  {
    title: '¿Cuál condición es correcta?',
    question: '¿Cuál condición detecta correctamente un nombre vacío O que sea solo espacios?',
    options: [
      '<code>nombre == ""</code>',
      '<code>nombre.strip() != ""</code> — retorna <code>True</code> si es válido',
      '<code>len(nombre) > 0</code>',
      '<code>nombre != " "</code>'
    ],
    correct: 1,
    explanation: '<code>nombre.strip() != ""</code> es la forma correcta. <code>.strip()</code> elimina espacios → si el resultado es <code>""</code>, entonces el nombre era vacío o solo espacios. Las otras opciones no detectan strings de puros espacios.'
  },
  {
    title: '¿Dónde va el mensaje de error?',
    code: `def validar_nombre(nombre):
    if nombre.strip() == "":
        print("Error: nombre vacío")  # ← ¿aquí?
        return False
    return True`,
    question: '¿Es correcto poner el <code>print("Error...")</code> dentro de la función de validación?',
    options: [
      'Sí, la función debe informar del error inmediatamente.',
      'No — la función de validación solo debe retornar <code>True</code> o <code>False</code>. El mensaje de error debe ir en la función que llama a la validación.',
      'Da igual, el código funciona de ambas formas.',
      'No, el mensaje debe ir dentro de un <code>try/except</code>.'
    ],
    correct: 1,
    explanation: '<strong>Separación de responsabilidades:</strong> la función de validación solo responde "¿es válido?". El mensaje de error debe ir en quien la llama. Así la misma función de validación se puede reutilizar con mensajes distintos en distintas partes del programa.'
  }
];

const nivel2Trace = [
  {
    title: 'Trazar strip()',
    code: `nombres = ["  Ana  ", "", "   ", "Pedro"]
for n in nombres:
    if n.strip() != "":
        print(n.strip())`,
    question: '¿Qué imprime este código?',
    options: [
      '<code>Ana</code> y <code>Pedro</code>',
      '<code>  Ana  </code>, vacío, espacios, <code>Pedro</code>',
      '<code>Ana</code>, vacío, vacío, <code>Pedro</code>',
      'Solo <code>Pedro</code>'
    ],
    correct: 0,
    explanation: 'Recorre los 4 strings. <code>"  Ana  ".strip()</code> → <code>"Ana"</code> (válido, se imprime). <code>"".strip()</code> → <code>""</code> (inválido). <code>"   ".strip()</code> → <code>""</code> (inválido). <code>"Pedro".strip()</code> → <code>"Pedro"</code> (válido, se imprime). Resultado: <code>Ana</code> y <code>Pedro</code>.'
  },
  {
    title: 'Completar validación',
    code: `def validar_nombre(nombre):
    return _____ != ""`,
    question: '¿Qué va en <code>_____</code> para validar que el nombre no sea vacío ni solo espacios?',
    options: [
      '<code>nombre</code>',
      '<code>nombre.strip()</code>',
      '<code>nombre.lower()</code>',
      '<code>len(nombre)</code>'
    ],
    correct: 1,
    explanation: '<code>nombre.strip()</code> elimina espacios al inicio y final. Si el resultado es <code>""</code>, el nombre era vacío o solo espacios. Comparar con <code>!= ""</code> nos da el booleano que necesitamos.'
  }
];


// ── NIVEL 3 — Validar entero positivo ───────────────────────

const nivel3Lesson = {
  title: 'Validar entero positivo',
  emoji: '🔢',
  intro: 'El usuario siempre ingresa <strong>texto</strong> con <code>input()</code>. Debemos verificar que ese texto represente un número entero mayor que 0 antes de usarlo.',
  code: `# Estrategia 1: .isdigit() + int()
def validar_nivel(texto):
    if texto.isdigit() and int(texto) > 0:
        return True
    return False

# Estrategia 2: try/except
def validar_nivel_v2(texto):
    try:
        numero = int(texto)
        if numero > 0:
            return True
        return False
    except ValueError:
        return False

# Pruebas
print(validar_nivel("5"))    # True
print(validar_nivel("0"))    # False (no es > 0)
print(validar_nivel("-3"))   # False (.isdigit() falla con "-")
print(validar_nivel("abc"))  # False`,
  keyPoints: [
    '<code>input()</code> SIEMPRE retorna un <strong>string</strong>, incluso si el usuario escribe "5"',
    '<code>.isdigit()</code> retorna <code>True</code> solo si TODOS los caracteres son dígitos (no acepta "-", ".", espacios)',
    '<code>"0".isdigit()</code> es <code>True</code>, pero <code>int("0") > 0</code> es <code>False</code> — ¡ambas condiciones son necesarias!',
    '<code>try/except ValueError</code> captura el error si <code>int("abc")</code> falla'
  ]
};

const nivel3Tf = [
  {
    title: 'isdigit con cero',
    code: '"0".isdigit()',
    question: '¿<code>"0".isdigit()</code> retorna <code>True</code>?',
    correct: true,
    explanation: '<strong>Verdadero.</strong> <code>"0".isdigit()</code> retorna <code>True</code> porque "0" es un dígito. Pero cuidado: <code>int("0") > 0</code> es <code>False</code>. Por eso necesitas AMBAS condiciones: <code>.isdigit()</code> AND <code>int(texto) > 0</code>.'
  },
  {
    title: 'isdigit con negativos',
    code: '"-5".isdigit()',
    question: '¿<code>"-5".isdigit()</code> retorna <code>True</code>?',
    correct: false,
    explanation: '<strong>Falso.</strong> <code>.isdigit()</code> retorna <code>False</code> si hay CUALQUIER carácter que no sea un dígito. El guión <code>"-"</code> no es un dígito, así que <code>"-5".isdigit()</code> → <code>False</code>.'
  },
  {
    title: 'int() con letras',
    code: 'int("abc")',
    question: '¿<code>int("abc")</code> retorna <code>0</code>?',
    correct: false,
    explanation: '<strong>Falso.</strong> <code>int("abc")</code> NO retorna 0 — lanza una excepción <code>ValueError</code> y el programa se detiene (crash) a menos que esté dentro de un <code>try/except</code>.'
  }
];

const nivel3Choice = [
  {
    title: '¿Qué pasa con int("abc")?',
    question: '¿Qué ocurre al ejecutar <code>int("abc")</code> sin <code>try/except</code>?',
    options: [
      'Retorna <code>0</code>',
      'Retorna <code>None</code>',
      'Lanza una excepción <code>ValueError</code> y el programa se detiene',
      'Convierte las letras a sus códigos ASCII'
    ],
    correct: 2,
    explanation: 'Python no puede convertir <code>"abc"</code> a entero. Lanza <code>ValueError: invalid literal for int() with base 10: \'abc\'</code>. Por eso usamos <code>try/except</code> para capturarlo.'
  },
  {
    title: 'Validación combinada',
    question: '¿Cuál combinación valida correctamente que un texto sea un entero mayor que 0?',
    options: [
      '<code>texto.isdigit()</code> — solo esto basta',
      '<code>int(texto) > 0</code> — solo esto basta',
      '<code>texto.isdigit() and int(texto) > 0</code>',
      '<code>texto > 0</code>'
    ],
    correct: 2,
    explanation: 'Necesitas AMBAS: <code>.isdigit()</code> verifica que sean solo dígitos (evita crash), y <code>int(texto) > 0</code> verifica que sea mayor que 0 (porque <code>"0".isdigit()</code> es <code>True</code> pero 0 no es > 0).'
  },
  {
    title: 'Pedir hasta que sea válido',
    code: `def pedir_nivel():
    while True:
        texto = input("Nivel: ")
        if texto.isdigit() and int(texto) > 0:
            return int(texto)
        print("Nivel inválido")`,
    question: '¿Qué hace el <code>return</code> dentro del <code>while True</code>?',
    options: [
      'Solo retorna el valor, el ciclo sigue ejecutándose.',
      'Termina la función inmediatamente y entrega el valor validado al que la llamó.',
      'Guarda el valor en una variable global.',
      'Imprime el valor en pantalla.'
    ],
    correct: 1,
    explanation: '<code>return</code> hace DOS cosas: <strong>entrega el valor</strong> y <strong>termina la función inmediatamente</strong> (incluyendo cualquier ciclo). Cuando los datos son válidos, el <code>return</code> "escapa" del <code>while True</code>.'
  }
];

const nivel3Trace = [
  {
    title: 'Trazar validación',
    code: `textos = ["5", "0", "-3", "abc", "10"]
for t in textos:
    if t.isdigit() and int(t) > 0:
        print(t, "✓")
    else:
        print(t, "✗")`,
    question: '¿Cuáles textos imprimen <code>✓</code>?',
    options: [
      'Solo <code>"5"</code>',
      '<code>"5"</code> y <code>"10"</code>',
      '<code>"5"</code>, <code>"0"</code> y <code>"10"</code>',
      'Todos excepto <code>"abc"</code>'
    ],
    correct: 1,
    explanation: '<code>"5"</code>: isdigit ✓, > 0 ✓. <code>"0"</code>: isdigit ✓, pero 0 > 0 es False ✗. <code>"-3"</code>: isdigit ✗ (tiene "-"). <code>"abc"</code>: isdigit ✗. <code>"10"</code>: isdigit ✓, > 0 ✓. Solo <code>"5"</code> y <code>"10"</code> pasan.'
  },
  {
    title: 'Completar validación de nivel',
    code: `def validar_nivel(texto):
    if _____ and _____:
        return True
    return False`,
    question: '¿Qué va en los <code>_____</code> para validar que el texto sea un entero mayor a 0?',
    options: [
      '<code>texto != ""</code> y <code>texto > "0"</code>',
      '<code>texto.isdigit()</code> y <code>int(texto) > 0</code>',
      '<code>len(texto) > 0</code> y <code>texto.isnumeric()</code>',
      '<code>int(texto)</code> y <code>texto > 0</code>'
    ],
    correct: 1,
    explanation: 'Primero <code>texto.isdigit()</code> asegura que son solo dígitos (evita crash al convertir). Luego <code>int(texto) > 0</code> verifica que sea positivo. Ambas son necesarias.'
  }
];


// ── NIVEL 4 — Búsqueda: retorna posición o -1 ──────────────

const nivel4Lesson = {
  title: 'Búsqueda: posición o -1',
  emoji: '🔍',
  intro: 'Uno de los patrones más importantes. La función recorre una lista buscando un elemento. Si lo encuentra, retorna su <strong>posición</strong>. Si no, retorna <strong>-1</strong> como señal de "no encontrado".',
  code: `def buscar_pocion(lista, nombre_buscado):
    for i in range(len(lista)):
        if lista[i]["nombre"] == nombre_buscado:
            return i      # ¡encontrado! retorna la posición
    return -1             # recorrió toda la lista sin encontrar

# Ejemplo de uso
pociones = [
    {"nombre": "Fuego", "poder": 8, "activa": False},
    {"nombre": "Hielo", "poder": 5, "activa": False},
    {"nombre": "Rayo",  "poder": 7, "activa": False}
]

pos = buscar_pocion(pociones, "Hielo")
print(pos)    # 1

pos = buscar_pocion(pociones, "Veneno")
print(pos)    # -1

# El programa principal decide qué hacer con el resultado
if pos != -1:
    print(pociones[pos])   # muestra los datos
else:
    print("Poción no encontrada")`,
  keyPoints: [
    '<code>return i</code> dentro del <code>for</code> retorna la posición Y termina la función inmediatamente',
    '<code>return -1</code> va <strong>FUERA del for</strong>, al mismo nivel de indentación — solo se ejecuta si el for terminó sin encontrar nada',
    'La función NO imprime mensajes — solo retorna un número (posición o -1)',
    'El <strong>programa principal</strong> decide qué hacer según el resultado (-1 o posición válida)'
  ]
};

const nivel4Tf = [
  {
    title: 'Posición del return -1',
    code: `def buscar(lista, valor):
    for i in range(len(lista)):
        if lista[i]["nombre"] == valor:
            return i
        return -1   # ← ¿aquí está bien?`,
    question: '¿El <code>return -1</code> está en la posición correcta en este código?',
    correct: false,
    explanation: '<strong>Falso.</strong> El <code>return -1</code> está DENTRO del <code>for</code> (indentado dentro del for). Esto significa que si el PRIMER elemento no coincide, inmediatamente retorna -1 sin revisar el resto. Debe ir FUERA del <code>for</code>, al mismo nivel de indentación.'
  },
  {
    title: 'Return corta el ciclo',
    code: `def buscar(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1`,
    question: '¿Cuando se ejecuta <code>return i</code>, el ciclo <code>for</code> se detiene inmediatamente?',
    correct: true,
    explanation: '<strong>Verdadero.</strong> <code>return</code> no solo entrega un valor — <strong>termina la ejecución de la función completa</strong>. Cuando encuentra el elemento, retorna la posición y el <code>for</code> se detiene sin revisar los demás elementos.'
  },
  {
    title: 'La función imprime el resultado',
    code: `def buscar_pocion(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"] == nombre:
            print("Encontrado en posición", i)
            return i
    print("No encontrado")
    return -1`,
    question: '¿Es buena práctica que la función de búsqueda imprima mensajes como "Encontrado" o "No encontrado"?',
    correct: false,
    explanation: '<strong>Falso.</strong> La función de búsqueda debe SOLO retornar la posición o -1. Los mensajes deben ir en el programa principal. Así la misma función se puede reutilizar para buscar (mostrar datos) Y para eliminar (borrar), con mensajes diferentes en cada caso.'
  }
];

const nivel4Choice = [
  {
    title: '¿Qué retorna si no existe?',
    code: `pociones = [
    {"nombre": "Fuego", "poder": 8, "activa": False},
    {"nombre": "Hielo", "poder": 5, "activa": False}
]
resultado = buscar_pocion(pociones, "Veneno")`,
    question: '¿Qué valor tiene <code>resultado</code>?',
    options: [
      '<code>None</code>',
      '<code>0</code>',
      '<code>-1</code>',
      '<code>False</code>'
    ],
    correct: 2,
    explanation: 'Si "Veneno" no existe en la lista, el <code>for</code> termina sin ejecutar <code>return i</code>. Se ejecuta <code>return -1</code>, que es la señal convencional de "no encontrado".'
  },
  {
    title: 'Quién decide qué hacer',
    question: '¿Quién debe decidir si mostrar los datos o imprimir "no encontrado"?',
    options: [
      'La función de búsqueda — debe imprimir el mensaje adecuado.',
      'El programa principal — recibe el resultado (-1 o posición) y decide qué hacer.',
      'Python decide automáticamente.',
      'Se necesita una tercera función intermediaria.'
    ],
    correct: 1,
    explanation: '<strong>Separación de responsabilidades:</strong> la función de búsqueda solo <em>informa</em> dónde está (o que no está). El programa principal <em>decide</em> qué hacer con esa información. Esto permite reutilizar la misma búsqueda para mostrar, eliminar, actualizar, etc.'
  },
  {
    title: '¿Qué posición retorna?',
    code: `pociones = [
    {"nombre": "Fuego", "poder": 8, "activa": False},
    {"nombre": "Hielo", "poder": 5, "activa": False},
    {"nombre": "Rayo",  "poder": 7, "activa": False}
]
pos = buscar_pocion(pociones, "Rayo")`,
    question: '¿Qué valor tiene <code>pos</code>?',
    options: [
      '<code>0</code>', '<code>1</code>', '<code>2</code>', '<code>3</code>'
    ],
    correct: 2,
    explanation: '"Rayo" está en la posición 2 (las posiciones empiezan en 0). <code>buscar_pocion</code> recorre: posición 0 ("Fuego") no coincide, posición 1 ("Hielo") no coincide, posición 2 ("Rayo") ¡coincide! Retorna <code>2</code>.'
  }
];

const nivel4Trace = [
  {
    title: 'Trazar la búsqueda completa',
    code: `def buscar_pocion(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"] == nombre:
            return i
    return -1

pociones = [
    {"nombre": "A", "poder": 1, "activa": False},
    {"nombre": "B", "poder": 2, "activa": False}
]

pos = buscar_pocion(pociones, "B")
if pos != -1:
    print(f"Posición: {pos}, Poder: {pociones[pos]['poder']}")
else:
    print("No encontrada")`,
    question: '¿Qué imprime este código?',
    options: [
      '<code>Posición: 0, Poder: 1</code>',
      '<code>Posición: 1, Poder: 2</code>',
      '<code>No encontrada</code>',
      '<code>Posición: -1, Poder: 2</code>'
    ],
    correct: 1,
    explanation: 'Busca "B": posición 0 es "A" (no), posición 1 es "B" (¡sí! retorna 1). <code>pos = 1</code>, como <code>1 != -1</code> se imprime la info: <code>Posición: 1, Poder: 2</code>.'
  },
  {
    title: 'Completar función de búsqueda',
    code: `def buscar_pocion(lista, nombre):
    for i in _____:
        if lista[i]["nombre"] == nombre:
            return _____
    return _____`,
    question: '¿Qué va en los tres <code>_____</code>?',
    options: [
      '<code>lista</code>, <code>True</code>, <code>False</code>',
      '<code>range(len(lista))</code>, <code>i</code>, <code>-1</code>',
      '<code>range(lista)</code>, <code>nombre</code>, <code>0</code>',
      '<code>enumerate(lista)</code>, <code>lista[i]</code>, <code>None</code>'
    ],
    correct: 1,
    explanation: '<code>range(len(lista))</code> genera los índices 0, 1, 2... <code>return i</code> retorna la posición encontrada. <code>return -1</code> indica que no se encontró. Este es el patrón clásico de búsqueda.'
  }
];


// ── NIVEL 5 — Reutilizar búsqueda para eliminar ────────────

const nivel5Lesson = {
  title: 'Reutilizar búsqueda para eliminar',
  emoji: '🗑️',
  intro: '¿Para qué escribir otra función de búsqueda si ya tienes una? La función de eliminación <strong>reutiliza</strong> la de búsqueda: primero encuentra la posición, luego elimina con <code>.pop()</code>.',
  code: `# Función de búsqueda (ya la tenemos del nivel 4)
def buscar_pocion(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"] == nombre:
            return i
    return -1

# Función de eliminación: REUTILIZA la búsqueda
# El programa principal llama a esto — no la función de búsqueda

pociones = [
    {"nombre": "Fuego", "poder": 8, "activa": False},
    {"nombre": "Hielo", "poder": 5, "activa": False}
]

nombre = input("Poción a eliminar: ")
posicion = buscar_pocion(pociones, nombre)  # reutilizamos

if posicion != -1:
    pociones.pop(posicion)
    print(f"Poción '{nombre}' eliminada.")
else:
    print(f"La poción '{nombre}' no se encuentra registrada.")`,
  keyPoints: [
    'La función de eliminación NO tiene su propio <code>for</code> para buscar — llama a <code>buscar_pocion()</code>',
    '<code>.pop(posicion)</code> elimina el elemento en esa posición de la lista',
    'Si la posición es <code>-1</code>, el programa informa que no se encontró',
    'La misma función de búsqueda se usa para "buscar" (opción 2) y para "eliminar" (opción 3) — ¡reutilización!'
  ]
};

const nivel5Tf = [
  {
    title: 'Búsqueda duplicada',
    question: '¿La función de eliminación debe tener su propio ciclo <code>for</code> para buscar el elemento?',
    correct: false,
    explanation: '<strong>Falso.</strong> La función de eliminación debe <strong>reutilizar</strong> la función de búsqueda que ya existe. Si cada función tuviera su propio <code>for</code>, estarías duplicando código. Si mejoras la búsqueda, tendrías que actualizar dos lugares.'
  },
  {
    title: '.pop() retorna algo',
    code: `lista = ["a", "b", "c"]
eliminado = lista.pop(1)
print(eliminado)`,
    question: '¿<code>lista.pop(1)</code> retorna el elemento eliminado (<code>"b"</code>)?',
    correct: true,
    explanation: '<strong>Verdadero.</strong> <code>.pop(posicion)</code> hace dos cosas: elimina el elemento de la lista Y retorna el valor eliminado. Aunque no siempre necesitas guardar ese valor.'
  },
  {
    title: 'Eliminar con posición -1',
    code: `pociones = [{"nombre": "Fuego", "poder": 8}]
pociones.pop(-1)`,
    question: '¿<code>pociones.pop(-1)</code> no hace nada porque -1 significa "no encontrado"?',
    correct: false,
    explanation: '<strong>Falso.</strong> ¡Cuidado con esta trampa! En Python, <code>.pop(-1)</code> elimina el <strong>último elemento</strong> (posición -1 es un índice negativo válido). Por eso es CRÍTICO verificar <code>if posicion != -1</code> ANTES de llamar a <code>.pop()</code>.'
  }
];

const nivel5Choice = [
  {
    title: '¿Qué método elimina por posición?',
    question: '¿Cuál método elimina un elemento de una lista dada su posición (índice)?',
    options: [
      '<code>lista.remove(posicion)</code>',
      '<code>lista.delete(posicion)</code>',
      '<code>lista.pop(posicion)</code>',
      '<code>lista.discard(posicion)</code>'
    ],
    correct: 2,
    explanation: '<code>.pop(posicion)</code> elimina y retorna el elemento en esa posición. <code>.remove(valor)</code> elimina por VALOR (no por posición). <code>.delete()</code> y <code>.discard()</code> no existen para listas.'
  },
  {
    title: 'Flujo de eliminación',
    question: '¿Cuál es el flujo correcto para eliminar una poción?',
    options: [
      'Pedir nombre → recorrer la lista con for → eliminar dentro del for',
      'Pedir nombre → llamar a buscar_pocion() → si retorna != -1, usar .pop(posicion)',
      'Pedir nombre → usar lista.remove(nombre) directamente',
      'Pedir posición al usuario → usar lista.pop(posicion)'
    ],
    correct: 1,
    explanation: 'El flujo correcto: pedir el nombre, usar la función de búsqueda para obtener la posición (o -1 si no existe), y solo si la posición es válida (!= -1) eliminar con <code>.pop()</code>.'
  }
];

const nivel5Trace = [
  {
    title: 'Trazar eliminación completa',
    code: `def buscar_pocion(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"] == nombre:
            return i
    return -1

pociones = [
    {"nombre": "Fuego", "poder": 8},
    {"nombre": "Hielo", "poder": 5},
    {"nombre": "Rayo",  "poder": 7}
]

pos = buscar_pocion(pociones, "Hielo")
if pos != -1:
    pociones.pop(pos)
print(len(pociones))`,
    question: '¿Qué imprime este código?',
    options: [
      '<code>3</code>', '<code>2</code>', '<code>1</code>', '<code>0</code>'
    ],
    correct: 1,
    explanation: 'Busca "Hielo" → posición 1. Como <code>1 != -1</code>, ejecuta <code>pociones.pop(1)</code> que elimina "Hielo". La lista queda con 2 elementos: "Fuego" y "Rayo". <code>len(pociones)</code> → <code>2</code>.'
  },
  {
    title: 'Completar eliminación',
    code: `nombre = input("Poción a eliminar: ")
posicion = _____(pociones, nombre)
if posicion _____:
    pociones._____(posicion)
    print(f"Eliminada.")
else:
    print(f"La poción '{nombre}' no se encuentra registrada.")`,
    question: '¿Qué va en los tres <code>_____</code>?',
    options: [
      '<code>buscar_pocion</code>, <code>!= -1</code>, <code>pop</code>',
      '<code>encontrar</code>, <code>== True</code>, <code>remove</code>',
      '<code>buscar_pocion</code>, <code>> 0</code>, <code>delete</code>',
      '<code>buscar_pocion</code>, <code>!= -1</code>, <code>remove</code>'
    ],
    correct: 0,
    explanation: 'Reutilizamos <code>buscar_pocion</code> para obtener la posición. Verificamos <code>!= -1</code> (encontrado). Eliminamos con <code>.pop(posicion)</code> que usa la posición retornada por la búsqueda.'
  }
];


// ── NIVEL 6 — Recorrer y actualizar TODOS ───────────────────

const nivel6Lesson = {
  title: 'Recorrer y actualizar TODOS',
  emoji: '🔄',
  intro: 'A veces necesitas aplicar una regla a <strong>TODOS</strong> los registros de la lista sin excepción. Recorres la lista y modificas un campo de cada diccionario según una condición.',
  code: `def actualizar_activacion(lista):
    for pocion in lista:
        if pocion["poder"] >= 5:
            pocion["activa"] = True
        else:
            pocion["activa"] = False

# Ejemplo
pociones = [
    {"nombre": "Fuego", "poder": 8, "activa": False},
    {"nombre": "Agua",  "poder": 3, "activa": False},
    {"nombre": "Rayo",  "poder": 5, "activa": False}
]

actualizar_activacion(pociones)

for p in pociones:
    estado = "ACTIVA" if p["activa"] else "INACTIVA"
    print(f"{p['nombre']}: {estado}")
# Fuego: ACTIVA (8 >= 5)
# Agua: INACTIVA (3 < 5)
# Rayo: ACTIVA (5 >= 5)`,
  keyPoints: [
    '<code>for pocion in lista</code> funciona porque <code>pocion</code> es una referencia al diccionario real (mutabilidad)',
    'La función recibe la lista como parámetro y modifica cada diccionario — <strong>no necesita return</strong>',
    'La regla se aplica a TODOS: si cumple la condición → <code>True</code>, si no → <code>False</code>',
    'No es solo "poner True a los que cumplen" — también debe poner <code>False</code> a los que no cumplen'
  ]
};

const nivel6Tf = [
  {
    title: 'Mutabilidad en acción',
    code: `def actualizar(lista):
    for p in lista:
        p["activa"] = True

pociones = [{"nombre": "A", "poder": 1, "activa": False}]
actualizar(pociones)
print(pociones[0]["activa"])`,
    question: '¿Este código imprime <code>True</code>?',
    correct: true,
    explanation: '<strong>Verdadero.</strong> Los diccionarios son <strong>mutables</strong>. Cuando haces <code>for p in lista</code>, <code>p</code> es una referencia al diccionario original. Al modificar <code>p["activa"]</code>, estás modificando el diccionario real de la lista.'
  },
  {
    title: 'Se necesita return',
    code: `def actualizar_activacion(lista):
    for p in lista:
        if p["poder"] >= 5:
            p["activa"] = True
        else:
            p["activa"] = False`,
    question: '¿Esta función necesita <code>return lista</code> al final para que los cambios se mantengan?',
    correct: false,
    explanation: '<strong>Falso.</strong> Como los diccionarios son mutables, los cambios hechos dentro de la función ya se reflejan en la lista original. No necesita <code>return</code>.'
  },
  {
    title: 'Solo True, nunca False',
    code: `def activar_poderosas(lista):
    for p in lista:
        if p["poder"] >= 5:
            p["activa"] = True`,
    question: '¿Esta función es correcta para actualizar el estado de TODAS las pociones?',
    correct: false,
    explanation: '<strong>Falso.</strong> Esta función solo pone <code>True</code> a las que cumplen, pero NUNCA pone <code>False</code> a las que no cumplen. Si una poción tenía <code>"activa": True</code> de antes y su poder baja de 5, seguiría como <code>True</code>. Necesita un <code>else: p["activa"] = False</code>.'
  }
];

const nivel6Choice = [
  {
    title: '¿Por qué funciona sin return?',
    question: '¿Por qué <code>for p in lista: p["campo"] = valor</code> modifica la lista original sin necesidad de <code>return</code>?',
    options: [
      'Porque Python copia la lista automáticamente.',
      'Porque los diccionarios son <strong>mutables</strong> — <code>p</code> es una referencia al diccionario real, no una copia.',
      'Porque <code>for</code> siempre modifica la variable original.',
      'Porque la función tiene acceso a variables globales.'
    ],
    correct: 1,
    explanation: 'Los diccionarios son objetos <strong>mutables</strong>. Cuando iteras con <code>for p in lista</code>, cada <code>p</code> apunta al diccionario real dentro de la lista. Al modificar <code>p["campo"]</code>, estás modificando el original.'
  },
  {
    title: '¿Cuántas quedan activas?',
    code: `pociones = [
    {"nombre": "A", "poder": 7, "activa": False},
    {"nombre": "B", "poder": 3, "activa": False},
    {"nombre": "C", "poder": 5, "activa": False},
    {"nombre": "D", "poder": 2, "activa": False}
]
# Regla: si poder >= 5 → activa = True, si no → False
actualizar_activacion(pociones)`,
    question: '¿Cuántas pociones quedan con <code>"activa": True</code>?',
    options: ['<code>1</code>', '<code>2</code>', '<code>3</code>', '<code>4</code>'],
    correct: 1,
    explanation: 'A (poder 7 ≥ 5) → True. B (poder 3 < 5) → False. C (poder 5 ≥ 5) → True. D (poder 2 < 5) → False. Total: <strong>2 pociones activas</strong> (A y C).'
  }
];

const nivel6Trace = [
  {
    title: 'Trazar actualización completa',
    code: `def actualizar_activacion(lista):
    for p in lista:
        if p["poder"] >= 5:
            p["activa"] = True
        else:
            p["activa"] = False

pociones = [
    {"nombre": "X", "poder": 10, "activa": False},
    {"nombre": "Y", "poder": 2,  "activa": True},
    {"nombre": "Z", "poder": 5,  "activa": False}
]

actualizar_activacion(pociones)
for p in pociones:
    print(p["nombre"], p["activa"])`,
    question: '¿Qué imprime este código?',
    options: [
      '<code>X True</code>, <code>Y True</code>, <code>Z False</code>',
      '<code>X True</code>, <code>Y False</code>, <code>Z True</code>',
      '<code>X False</code>, <code>Y True</code>, <code>Z True</code>',
      '<code>X True</code>, <code>Y True</code>, <code>Z True</code>'
    ],
    correct: 1,
    explanation: 'X (poder 10 ≥ 5) → True. Y (poder 2 < 5) → False (¡aunque antes era True, se ACTUALIZA!). Z (poder 5 ≥ 5) → True. La función aplica la regla a TODOS sin excepción.'
  },
  {
    title: 'Completar actualización',
    code: `def actualizar_activacion(lista):
    for _____ in _____:
        if _____["poder"] >= 5:
            _____["activa"] = True
        else:
            _____["activa"] = False`,
    question: '¿Qué va en los cuatro <code>_____</code>?',
    options: [
      '<code>i</code>, <code>range(len(lista))</code>, <code>lista[i]</code>, <code>lista[i]</code>',
      '<code>pocion</code>, <code>lista</code>, <code>pocion</code>, <code>pocion</code>',
      '<code>lista</code>, <code>pocion</code>, <code>lista</code>, <code>lista</code>',
      '<code>p</code>, <code>pociones</code>, <code>p</code>, <code>p</code>'
    ],
    correct: 1,
    explanation: '<code>for pocion in lista</code> recorre cada diccionario. Luego <code>pocion["poder"]</code> y <code>pocion["activa"]</code> acceden/modifican los campos de ese diccionario. Funciona porque los diccionarios son mutables.'
  }
];


// ── NIVEL 7 — Menú while True + break + dispatcher ─────────

const nivel7Lesson = {
  title: 'Menú completo',
  emoji: '📋',
  intro: 'El menú es el <strong>corazón del programa</strong>. Se repite con <code>while True</code> hasta que el usuario elige salir. Cada opción llama a la función correspondiente.',
  code: `# Función 1: MOSTRAR el menú (solo imprime)
def mostrar_menu():
    print("=" * 30)
    print("1. Agregar poción")
    print("2. Buscar poción")
    print("3. Eliminar poción")
    print("4. Activar pociones")
    print("5. Mostrar pociones")
    print("6. Salir")
    print("=" * 30)

# Función 2: LEER la opción (retorna número validado)
def leer_opcion():
    while True:
        texto = input("Opción: ")
        if texto.isdigit() and 1 <= int(texto) <= 6:
            return int(texto)
        print("Opción inválida. Elige entre 1 y 6.")

# Programa principal — el dispatcher
pociones = []

while True:
    mostrar_menu()            # muestra opciones
    opcion = leer_opcion()    # lee y valida

    if opcion == 1:
        agregar_pocion(pociones)
    elif opcion == 2:
        nombre = input("Nombre a buscar: ")
        pos = buscar_pocion(pociones, nombre)
        if pos != -1:
            print(pociones[pos])
        else:
            print("No encontrada")
    elif opcion == 3:
        nombre = input("Nombre a eliminar: ")
        pos = buscar_pocion(pociones, nombre)
        if pos != -1:
            pociones.pop(pos)
            print("Eliminada")
        else:
            print(f"La poción '{nombre}' no se encuentra registrada.")
    elif opcion == 4:
        actualizar_activacion(pociones)
        print("Activación actualizada.")
    elif opcion == 5:
        actualizar_activacion(pociones)  # primero actualizar
        mostrar_pociones(pociones)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto")
        break  # ROMPE el while True`,
  keyPoints: [
    '<code>mostrar_menu()</code> solo imprime — no recibe nada ni retorna nada',
    '<code>leer_opcion()</code> no recibe nada, pero SÍ retorna el número validado',
    'Ambas funciones se llaman en CADA vuelta del <code>while True</code>',
    'El <code>break</code> va en la opción de salir — rompe el <code>while True</code>',
    'El dispatcher (<code>if/elif</code>) conecta cada opción con su función'
  ]
};

const nivel7Tf = [
  {
    title: 'while True sin break',
    question: '¿Un ciclo <code>while True</code> sin <code>break</code> se ejecuta infinitamente?',
    correct: true,
    explanation: '<strong>Verdadero.</strong> <code>while True</code> siempre evalúa la condición como verdadera. Si no hay un <code>break</code> (o un <code>return</code> dentro de una función), el ciclo nunca termina.'
  },
  {
    title: 'Una sola función para menú',
    question: '¿El menú debe implementarse con UNA sola función que muestre las opciones Y lea la opción elegida?',
    correct: false,
    explanation: '<strong>Falso.</strong> Deben ser <strong>dos funciones separadas</strong>: una que muestre el menú (sin recibir ni retornar nada) y otra que lea y retorne la opción validada (sin recibir nada, retornando el número). Separación de responsabilidades.'
  },
  {
    title: 'Break en la opción correcta',
    code: `while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        agregar(lista)
    elif opcion == 6:
        print("Adiós")
        break`,
    question: '¿El <code>break</code> está en el lugar correcto para salir del programa?',
    correct: true,
    explanation: '<strong>Verdadero.</strong> El <code>break</code> está dentro del <code>elif opcion == 6</code>, que es la opción de salir. Cuando el usuario elige 6, se imprime el mensaje de despedida y <code>break</code> rompe el <code>while True</code>, finalizando el programa.'
  }
];

const nivel7Choice = [
  {
    title: 'mostrar_menu() vs leer_opcion()',
    question: '¿Cuál es la diferencia clave entre <code>mostrar_menu()</code> y <code>leer_opcion()</code>?',
    options: [
      '<code>mostrar_menu()</code> retorna un número y <code>leer_opcion()</code> no retorna nada.',
      '<code>mostrar_menu()</code> no recibe ni retorna nada (solo imprime). <code>leer_opcion()</code> no recibe nada pero SÍ retorna el número validado.',
      'Son la misma función con nombres diferentes.',
      '<code>leer_opcion()</code> recibe la lista como parámetro.'
    ],
    correct: 1,
    explanation: '<code>mostrar_menu()</code> es un "procedimiento puro": solo imprime en pantalla, no recibe parámetros ni retorna nada. <code>leer_opcion()</code> sí retorna: el número de opción validado. Son dos responsabilidades distintas.'
  },
  {
    title: '¿Dónde va el break?',
    question: '¿Dónde debe ir el <code>break</code> para salir del menú?',
    options: [
      'Al inicio del <code>while True</code>, antes de <code>mostrar_menu()</code>.',
      'Dentro del <code>if/elif</code> correspondiente a la opción de salir, después del mensaje de despedida.',
      'Al final del <code>while True</code>, siempre.',
      'Dentro de la función <code>leer_opcion()</code>.'
    ],
    correct: 1,
    explanation: 'El <code>break</code> va dentro del bloque de la opción de salir (ej: <code>elif opcion == 6:</code>). Primero se muestra el mensaje de despedida y luego <code>break</code> rompe el ciclo.'
  },
  {
    title: 'Opción 5: Mostrar con actualización',
    question: 'La opción "Mostrar pociones" debe primero llamar a <code>actualizar_activacion()</code> y luego mostrar. ¿Por qué?',
    options: [
      'Porque <code>actualizar_activacion()</code> imprime la lista.',
      'Para asegurarse de que el campo "activa" esté al día con el poder actual antes de mostrar los datos.',
      'Porque sin eso la lista estaría vacía.',
      'Para ordenar la lista alfabéticamente.'
    ],
    correct: 1,
    explanation: 'El campo "activa" depende del poder de cada poción. Si se agregaron o modificaron pociones desde la última actualización, los estados podrían estar desactualizados. Llamar a <code>actualizar_activacion()</code> primero garantiza datos frescos.'
  }
];

const nivel7Trace = [
  {
    title: 'Trazar el dispatcher',
    code: `# Supongamos que leer_opcion() retorna estos valores en orden:
# Primera vuelta: 1 (agregar)
# Segunda vuelta: 5 (mostrar)
# Tercera vuelta: 6 (salir)

vuelta = 0
while True:
    vuelta += 1
    # mostrar_menu() se ejecuta aquí
    # opcion = leer_opcion() retorna el valor de arriba
    
    if vuelta == 3:  # simula opción 6
        print("Adiós")
        break
    print(f"Vuelta {vuelta}")

print(f"Total de vueltas: {vuelta}")`,
    question: '¿Qué imprime este código?',
    options: [
      '<code>Vuelta 1</code>, <code>Vuelta 2</code>, <code>Adiós</code>, <code>Total de vueltas: 3</code>',
      '<code>Vuelta 1</code>, <code>Vuelta 2</code>, <code>Vuelta 3</code>, <code>Adiós</code>',
      '<code>Adiós</code>, <code>Total de vueltas: 1</code>',
      'Ciclo infinito'
    ],
    correct: 0,
    explanation: 'Vuelta 1: no es 3, imprime "Vuelta 1". Vuelta 2: no es 3, imprime "Vuelta 2". Vuelta 3: sí es 3, imprime "Adiós" y break sale del while. Después del while: imprime "Total de vueltas: 3".'
  },
  {
    title: 'Completar el programa principal',
    code: `pociones = []

while _____:
    mostrar_menu()
    opcion = _____()
    
    if opcion == 1:
        agregar_pocion(pociones)
    elif opcion == 6:
        print("Gracias por usar el sistema.")
        _____`,
    question: '¿Qué va en los tres <code>_____</code>?',
    options: [
      '<code>True</code>, <code>leer_opcion</code>, <code>break</code>',
      '<code>opcion != 6</code>, <code>input</code>, <code>exit()</code>',
      '<code>True</code>, <code>mostrar_menu</code>, <code>continue</code>',
      '<code>True</code>, <code>leer_opcion</code>, <code>return</code>'
    ],
    correct: 0,
    explanation: '<code>while True</code> crea el ciclo infinito del menú. <code>leer_opcion()</code> lee y valida la opción del usuario. <code>break</code> rompe el ciclo cuando el usuario elige salir. Este es el patrón estándar de menú.'
  }
];


// ═══════════════════════════════════════════════════════════════
//  Exportar todo en un objeto organizado por niveles
// ═══════════════════════════════════════════════════════════════

const entrenamientoPatronesData = {
  niveles: [
    {
      id: 1, title: 'Lista vacía + Diccionarios', emoji: '📦', color: '#3b82f6',
      lesson: nivel1Lesson, tf: nivel1Tf, choice: nivel1Choice, trace: nivel1Trace
    },
    {
      id: 2, title: 'Validar Nombre', emoji: '✍️', color: '#8b5cf6',
      lesson: nivel2Lesson, tf: nivel2Tf, choice: nivel2Choice, trace: nivel2Trace
    },
    {
      id: 3, title: 'Validar Entero Positivo', emoji: '🔢', color: '#f59e0b',
      lesson: nivel3Lesson, tf: nivel3Tf, choice: nivel3Choice, trace: nivel3Trace
    },
    {
      id: 4, title: 'Búsqueda (posición o -1)', emoji: '🔍', color: '#10b981',
      lesson: nivel4Lesson, tf: nivel4Tf, choice: nivel4Choice, trace: nivel4Trace
    },
    {
      id: 5, title: 'Reutilizar Búsqueda para Eliminar', emoji: '🗑️', color: '#ef4444',
      lesson: nivel5Lesson, tf: nivel5Tf, choice: nivel5Choice, trace: nivel5Trace
    },
    {
      id: 6, title: 'Recorrer y Actualizar Todos', emoji: '🔄', color: '#06b6d4',
      lesson: nivel6Lesson, tf: nivel6Tf, choice: nivel6Choice, trace: nivel6Trace
    },
    {
      id: 7, title: 'Menú Completo', emoji: '📋', color: '#ec4899',
      lesson: nivel7Lesson, tf: nivel7Tf, choice: nivel7Choice, trace: nivel7Trace
    }
  ]
};
