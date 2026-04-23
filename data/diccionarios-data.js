// ═══════════════════════════════════════════════════════════════
//  📚 Datos de Ejercicios — Diccionarios en Python
//  ─────────────────────────────────────────────────────────────
//  Variables globales consumidas por diccionarios.html
// ═══════════════════════════════════════════════════════════════

// ── SELECCIÓN MÚLTIPLE ──
const dictChoiceExercises = [
  {
    title: "¿Qué es un diccionario?",
    question: "¿Cuál de las siguientes opciones define MEJOR a un diccionario en Python?",
    options: [
      "Una lista ordenada de elementos que se acceden por índice numérico.",
      "Una colección de pares clave:valor donde cada clave es única e irrepetible.",
      "Un tipo de dato que solo almacena texto en formato JSON.",
      "Una variable especial que solo puede guardar números enteros."
    ],
    correct: 1,
    explanation: "¡Exacto! Un diccionario es una colección de pares <code>clave: valor</code>. Cada clave actúa como una 'etiqueta única' para acceder rápidamente a su valor asociado, sin usar índices numéricos."
  },
  {
    title: "Acceso a valores",
    question: "Dado <code>persona = {'nombre': 'Ash', 'edad': 10}</code>, ¿cómo obtenemos el valor <code>10</code>?",
    options: [
      "persona[1]",
      "persona['edad']",
      "persona.edad",
      "persona(edad)"
    ],
    correct: 1,
    explanation: "En un diccionario usamos la <strong>clave</strong> entre corchetes: <code>persona['edad']</code>. No usamos índices numéricos como en las listas. La notación con punto (<code>persona.edad</code>) es de otros lenguajes, no de Python puro."
  },
  {
    title: "Agregar un par nuevo",
    question: "Tengo <code>pokedex = {'Pikachu': 'Eléctrico'}</code>. ¿Cómo agrego a Charmander de tipo Fuego?",
    options: [
      "pokedex.append('Charmander', 'Fuego')",
      "pokedex.insert('Charmander', 'Fuego')",
      "pokedex['Charmander'] = 'Fuego'",
      "pokedex.add('Charmander': 'Fuego')"
    ],
    correct: 2,
    explanation: "Para agregar un par nuevo, simplemente asignas: <code>diccionario['nueva_clave'] = valor</code>. Los diccionarios NO usan .append() ni .insert() — esos son métodos exclusivos de las listas."
  },
  {
    title: "Claves duplicadas",
    question: "¿Qué ocurre si en un diccionario defines dos veces la misma clave?",
    options: [
      "Python lanza un KeyError inmediatamente y el programa se detiene.",
      "Se guardan ambos valores en una lista interna automáticamente.",
      "La segunda definición sobrescribe silenciosamente a la primera.",
      "Python ignora la segunda y conserva la primera intacta."
    ],
    correct: 2,
    explanation: "¡Cuidado! Si repites una clave, Python NO te avisa. Simplemente el último valor asignado aplasta al anterior. Las claves en un diccionario son <strong>únicas</strong>; no puede haber dos llaves idénticas coexistiendo."
  },
  {
    title: "Recorrido con .items()",
    question: "¿Qué método del diccionario me permite recorrer SIMULTÁNEAMENTE las claves y los valores en un ciclo for?",
    options: [
      ".keys()",
      ".values()",
      ".items()",
      ".pairs()"
    ],
    correct: 2,
    explanation: "El método <code>.items()</code> devuelve pares (clave, valor) en cada iteración: <code>for clave, valor in diccionario.items():</code>. Con .keys() solo obtienes claves, con .values() solo valores."
  },
  {
    title: "Verificar existencia",
    question: "¿Cuál es la forma correcta de verificar si la clave <code>'vida'</code> existe en un diccionario llamado <code>stats</code>?",
    options: [
      "if stats.has('vida'):",
      "if 'vida' in stats:",
      "if stats.contains('vida'):",
      "if stats.exists('vida'):"
    ],
    correct: 1,
    explanation: "En Python usamos el operador <code>in</code> para verificar si una clave existe: <code>if 'vida' in stats:</code>. Los métodos .has(), .contains() y .exists() NO existen en diccionarios de Python."
  }
];

// ── VERDADERO O FALSO ──
const dictTfExercises = [
  {
    title: "Llaves vs Índices",
    statement: "En un diccionario, para acceder a un valor usamos su <strong>clave</strong> (ej: <code>persona['nombre']</code>), mientras que en una lista usamos un <strong>índice numérico</strong> (ej: <code>lista[0]</code>).",
    correct: true,
    explanation: "¡Verdadero! Esa es LA diferencia fundamental. Los diccionarios usan claves descriptivas (strings, números, etc.), las listas usan posiciones numéricas secuenciales."
  },
  {
    title: "Orden garantizado",
    statement: "Desde Python 3.7+, los diccionarios mantienen el orden de inserción de sus elementos. Si agregas 'a' primero y 'b' después, al recorrerlo aparecerá 'a' antes que 'b'.",
    correct: true,
    explanation: "¡Verdadero! A partir de Python 3.7, los diccionarios preservan oficialmente el orden de inserción. Esto no era garantizado en versiones anteriores."
  },
  {
    title: "Valores repetidos",
    statement: "En un diccionario, tanto las claves como los valores deben ser únicos. No puedo tener dos valores iguales.",
    correct: false,
    explanation: "¡Falso! Solo las <strong>claves</strong> deben ser únicas. Los <strong>valores</strong> pueden repetirse sin problema. Ejemplo: <code>{'Ash': 'Fuego', 'Misty': 'Agua', 'Brock': 'Fuego'}</code> — dos personas con tipo 'Fuego' es perfectamente válido."
  },
  {
    title: "Listas como claves",
    statement: "Puedo usar una lista como clave de un diccionario sin problema: <code>{[1,2]: 'hola'}</code>.",
    correct: false,
    explanation: "¡Falso! Las claves deben ser de un tipo <strong>inmutable</strong> (hashable). Las listas son mutables, así que Python lanza un <code>TypeError: unhashable type: 'list'</code>. Puedes usar strings, números, tuplas, pero NUNCA listas como claves."
  },
  {
    title: "KeyError fatal",
    statement: "Si intento acceder a una clave que no existe con <code>diccionario['clave_fantasma']</code>, Python no da error y simplemente devuelve <code>None</code>.",
    correct: false,
    explanation: "¡Falso! Acceder a una clave inexistente con corchetes lanza un <code>KeyError</code> fatal. Para evitarlo, usa el método seguro <code>.get('clave', valor_por_defecto)</code> que sí devuelve None (o un valor personalizado) si la clave no existe."
  },
  {
    title: "Iteración por defecto",
    statement: "Si hago <code>for x in mi_diccionario:</code> sin usar .items(), .keys() ni .values(), la variable <code>x</code> tomará solo las <strong>claves</strong> del diccionario.",
    correct: true,
    explanation: "¡Verdadero! Por defecto, iterar sobre un diccionario recorre sus claves. Es equivalente a escribir <code>for x in mi_diccionario.keys():</code>."
  }
];

// ── UNIR CONCEPTOS (MATCHING) ──
const dictMatchExercises = [
  {
    title: "Anatomía del Diccionario",
    pairs: [
      { id: "dm1", left: "<code>dict['clave']</code>", right: "Acceder al valor de una clave" },
      { id: "dm2", left: "<code>.get(clave, default)</code>", right: "Acceso seguro sin KeyError" },
      { id: "dm3", left: "<code>.keys()</code>", right: "Devuelve solo las claves" },
      { id: "dm4", left: "<code>.values()</code>", right: "Devuelve solo los valores" },
      { id: "dm5", left: "<code>.items()</code>", right: "Devuelve pares (clave, valor)" },
      { id: "dm6", left: "<code>del dict['x']</code>", right: "Elimina un par clave:valor" }
    ]
  }
];

// ── ENCONTRAR EL ERROR ──
const dictErrorExercises = [
  {
    title: "El fantasma del KeyError",
    question: "El alumno quiere mostrar la región del personaje, pero Python colapsa con un KeyError. ¿Dónde está el error?",
    code: `personaje = {"nombre": "Link", "juego": "Zelda"}

print(personaje["region"])`,
    options: [
      "Los diccionarios no funcionan con print()",
      "Falta un punto y coma al final de la línea",
      "La clave 'region' no existe en el diccionario y se accede con corchetes sin protección.",
      "Debería usarse paréntesis en vez de corchetes"
    ],
    correct: 2,
    explanation: "Acceder con <code>diccionario['clave']</code> a una clave que no existe lanza <code>KeyError</code>. Solución segura: usar <code>.get('region', 'Desconocida')</code> o verificar con <code>if 'region' in personaje:</code>."
  },
  {
    title: "Append fantasma",
    question: "El código intenta agregar un nuevo héroe al diccionario, pero Python lanza un AttributeError. ¿Por qué?",
    code: `heroes = {"Iron Man": "Tecnología", "Thor": "Rayo"}

heroes.append("Hulk", "Fuerza")`,
    options: [
      "Los diccionarios no aceptan strings como valores",
      "El método .append() NO existe en diccionarios; se agrega con heroes['Hulk'] = 'Fuerza'.",
      "Faltan las llaves de cierre del diccionario",
      "Python no permite más de 2 elementos en un diccionario"
    ],
    correct: 1,
    explanation: "Los diccionarios no tienen <code>.append()</code>: ese es un método exclusivo de listas. Para agregar un par nuevo: <code>heroes['Hulk'] = 'Fuerza'</code>."
  },
  {
    title: "Desempaquetado incorrecto",
    question: "El alumno quiere imprimir cada héroe con su poder pero obtiene un ValueError: too many values to unpack. ¿Cuál es el error?",
    code: `poderes = {"Goku": "Kamehameha", "Naruto": "Rasengan"}

for heroe in poderes.items():
    print(f"{heroe} usa {poder}")`,
    options: [
      "El método .items() no existe para diccionarios",
      "Se necesitan dos variables en el for (heroe, poder) para desempaquetar los pares que devuelve .items().",
      "El f-string está mal escrito",
      "Los diccionarios no se pueden recorrer con for"
    ],
    correct: 1,
    explanation: "El método <code>.items()</code> devuelve tuplas de (clave, valor). Para desempaquetarlas necesitas dos variables: <code>for heroe, poder in poderes.items():</code>."
  },
  {
    title: "La clave mutable prohibida",
    question: "Este código lanza un TypeError al momento de crear el diccionario. ¿Cuál es la razón?",
    code: `inventario = {
    ["espada", "escudo"]: 2,
    "pociones": 5
}`,
    options: [
      "No se pueden mezclar tipos de claves distintos",
      "La lista ['espada', 'escudo'] es mutable y no puede servir como clave de diccionario.",
      "El número 2 debería ir entre comillas",
      "Falta una coma después del último elemento"
    ],
    correct: 1,
    explanation: "Las claves de un diccionario deben ser de tipo <strong>inmutable</strong> (hashable). Las listas son mutables → <code>TypeError: unhashable type: 'list'</code>. Si necesitas usar una secuencia como clave, convierte la lista en tupla."
  }
];

// ── COMPLETAR CÓDIGO ──
const dictCompleteExercises = [
  {
    title: "Creando tu primer diccionario",
    question: "Completa el código para crear un diccionario con datos de un estudiante y luego imprimir su nombre.",
    code: `estudiante = ____"nombre": "María", "carrera": "Informática"____

print(estudiante____"nombre"____)`,
    options: [
      "[ / ] / [ / ]",
      "{ / } / [ / ]",
      "( / ) / { / }",
      "{ / } / ( / )"
    ],
    correct: 1,
    explanation: "Los diccionarios se crean con <strong>llaves { }</strong> y se acceden con <strong>corchetes [ ]</strong>: <code>{'nombre': 'María'}</code> y luego <code>estudiante['nombre']</code>."
  },
  {
    title: "Recorrido doble",
    question: "Queremos imprimir cada pokémon con su tipo. Completa los huecos del ciclo for.",
    code: `pokedex = {"Pikachu": "Eléctrico", "Squirtle": "Agua"}

for ____, ____ in pokedex.items():
    print(f"{pokemon} es de tipo {tipo}")`,
    options: [
      "pokemon / tipo",
      "key / val",
      "i / pokedex[i]",
      "clave / pokedex"
    ],
    correct: 0,
    explanation: "El <code>.items()</code> entrega pares (clave, valor). Usamos dos variables descriptivas: <code>for pokemon, tipo in pokedex.items():</code> que se mapean automáticamente."
  },
  {
    title: "Acceso seguro con .get()",
    question: "El programa debe mostrar el nivel del jugador o 'Nivel 1' si no tiene nivel asignado. Completa.",
    code: `jugador = {"nombre": "Steve", "mundo": "Survival"}

nivel = jugador.____("nivel", ____)
print(f"Tu nivel es: {nivel}")`,
    options: [
      "find / 0",
      "get / 'Nivel 1'",
      "search / None",
      "access / 'Nivel 1'"
    ],
    correct: 1,
    explanation: "El método <code>.get(clave, valor_por_defecto)</code> busca la clave sin riesgo de KeyError. Si 'nivel' no existe, devuelve el respaldo: <code>'Nivel 1'</code>."
  },
  {
    title: "Contando con diccionarios",
    question: "Queremos contar cuántas veces aparece cada fruta. Completa la lógica del contador.",
    code: `frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
contador = {}

for fruta in frutas:
    if fruta ____ contador:
        contador[fruta] ____ 1
    else:
        contador[fruta] = 1`,
    options: [
      "== / +=",
      "in / +=",
      "not in / -=",
      "is / ="
    ],
    correct: 1,
    explanation: "Usamos <code>in</code> para verificar si la clave ya existe, y <code>+=</code> para sumarle 1 al valor actual. Este es el patrón clásico de <strong>contador con diccionarios</strong>."
  }
];

// ── TRAZAR CÓDIGO ──
const dictTraceExercises = [
  {
    title: "Lectura básica de diccionario",
    question: "¿Qué imprime este código en la consola?",
    code: `mascota = {"nombre": "Luna", "tipo": "Gato", "edad": 3}

print(mascota["tipo"])
print(mascota["edad"] + 1)`,
    options: [
      "Luna / 4",
      "Gato / 4",
      "Gato / 3",
      "tipo / edad"
    ],
    correct: 1,
    explanation: "Primer print: <code>mascota['tipo']</code> → 'Gato'. Segundo print: <code>mascota['edad']</code> es 3, le sumamos 1 → imprime 4. Resultado: Gato y 4."
  },
  {
    title: "Sobrescritura silenciosa",
    question: "¿Qué valor tendrá la clave 'poder' al final del programa?",
    code: `heroe = {"nombre": "Goku", "poder": 9000}

heroe["poder"] = heroe["poder"] + 1000
heroe["poder"] = 15000

print(heroe["poder"])`,
    options: [
      "9000",
      "10000",
      "15000",
      "25000"
    ],
    correct: 2,
    explanation: "Línea 1: poder = 9000. Línea 2: poder = 9000 + 1000 = 10000. Línea 3: poder = 15000 (sobrescritura total). El último valor asignado gana. Imprime <strong>15000</strong>."
  },
  {
    title: "Recorrido con for y acumulador",
    question: "¿Qué imprime este programa al ejecutarse?",
    code: `precios = {"pan": 1500, "leche": 1200, "queso": 3000}
total = 0

for producto, precio in precios.items():
    total += precio

print("Total:", total)`,
    options: [
      "Total: 1500",
      "Total: 3000",
      "Total: 5700",
      "Total: 0"
    ],
    correct: 2,
    explanation: "El for recorre los 3 pares. Acumula: 0 + 1500 = 1500, luego 1500 + 1200 = 2700, luego 2700 + 3000 = 5700. Imprime <strong>Total: 5700</strong>."
  },
  {
    title: "Combo Épico: if + diccionario + lista",
    question: "¿Qué contendrá la lista 'aprobados' al final?",
    code: `alumnos = {
    "Ana": 6.5,
    "Luis": 3.8,
    "Marta": 5.0,
    "Pedro": 2.9
}
aprobados = []

for nombre, nota in alumnos.items():
    if nota >= 4.0:
        aprobados.append(nombre)

print(aprobados)`,
    options: [
      "['Ana', 'Luis', 'Marta', 'Pedro']",
      "['Ana', 'Marta']",
      "['Ana', 'Luis', 'Marta']",
      "['Ana']"
    ],
    correct: 1,
    explanation: "Ana (6.5 ≥ 4.0) ✅, Luis (3.8 < 4.0) ❌, Marta (5.0 ≥ 4.0) ✅, Pedro (2.9 < 4.0) ❌. Resultado: <code>['Ana', 'Marta']</code>."
  }
];
