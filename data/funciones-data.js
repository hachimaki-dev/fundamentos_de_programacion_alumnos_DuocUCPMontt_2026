// ═══════════════════════════════════════════════════════════════
//  🔧 Datos de Ejercicios — Funciones en Python
//  ─────────────────────────────────────────────────────────────
//  Variables globales consumidas por funciones.html
// ═══════════════════════════════════════════════════════════════

// ── SELECCIÓN MÚLTIPLE ──
const funcChoiceExercises = [
  {
    title: "¿Qué es una función?",
    question: "¿Cuál de las siguientes opciones define MEJOR a una función en Python?",
    options: [
      "Una variable especial que almacena múltiples valores.",
      "Un bloque de código reutilizable que realiza una tarea específica y puede recibir datos y devolver resultados.",
      "Un tipo de dato que solo se usa dentro de los ciclos for.",
      "Un archivo externo que se importa para agregar colores a la consola."
    ],
    correct: 1,
    explanation: "¡Exacto! Una función es un <strong>bloque de código reutilizable</strong> que encapsula una tarea. Se define una vez con <code>def</code> y se puede invocar (llamar) cuantas veces necesites, evitando repetir código."
  },
  {
    title: "Palabra clave def",
    question: "¿Cuál es la sintaxis correcta para DEFINIR una función llamada <code>saludar</code> que recibe un <code>nombre</code>?",
    options: [
      "function saludar(nombre):",
      "def saludar(nombre):",
      "func saludar[nombre]:",
      "define saludar(nombre)"
    ],
    correct: 1,
    explanation: "En Python usamos <code>def</code> (abreviatura de 'define') seguido del nombre de la función, paréntesis con los parámetros y dos puntos <code>:</code>. El cuerpo va indentado debajo."
  },
  {
    title: "Parámetro vs Argumento",
    question: "¿Cuál es la diferencia entre un PARÁMETRO y un ARGUMENTO?",
    options: [
      "Son lo mismo, solo cambia el nombre según el profesor.",
      "El parámetro es la variable en la DEFINICIÓN de la función; el argumento es el valor REAL que le pasas al LLAMARLA.",
      "El argumento se usa solo en ciclos while y el parámetro en ciclos for.",
      "El parámetro siempre es un número y el argumento siempre es un string."
    ],
    correct: 1,
    explanation: "Distinción clave: <strong>Parámetro</strong> = variable placeholder en la definición (<code>def saludar(nombre)</code>). <strong>Argumento</strong> = valor concreto al llamar (<code>saludar('Ana')</code>). 'nombre' es parámetro, 'Ana' es argumento."
  },
  {
    title: "return vs print",
    question: "¿Cuál es la diferencia fundamental entre <code>return</code> y <code>print()</code> dentro de una función?",
    options: [
      "No hay diferencia, ambos muestran el resultado en pantalla.",
      "<code>return</code> envía el resultado DE VUELTA al código que llamó a la función (se puede guardar en variable); <code>print()</code> solo muestra en consola sin devolver nada útil.",
      "<code>print()</code> devuelve el valor y <code>return</code> lo muestra en pantalla.",
      "<code>return</code> solo funciona con números y <code>print()</code> solo con strings."
    ],
    correct: 1,
    explanation: "<code>return</code> ENTREGA el valor al punto donde se llamó la función — puedes guardarlo: <code>resultado = mi_funcion()</code>. <code>print()</code> solo muestra texto en la consola, pero no 'devuelve' nada que puedas reutilizar en tu código."
  },
  {
    title: "Función sin return",
    question: "¿Qué devuelve una función que NO tiene la instrucción <code>return</code>?",
    options: [
      "Devuelve 0 por defecto.",
      "Lanza un error SyntaxError.",
      "Devuelve <code>None</code> implícitamente.",
      "Devuelve una cadena vacía ''."
    ],
    correct: 2,
    explanation: "Si una función no tiene <code>return</code> (o tiene <code>return</code> sin valor), Python devuelve <code>None</code> automáticamente. Por eso si haces <code>x = print('hola')</code>, x vale <code>None</code>."
  },
  {
    title: "Valores por defecto",
    question: "Dada <code>def saludar(nombre, saludo='Hola'):</code>, ¿cuál llamada es VÁLIDA?",
    options: [
      "saludar() — sin argumentos",
      "saludar('Ana') — solo el nombre, porque saludo tiene valor por defecto",
      "saludar(saludo='Hey') — solo el saludo, sin nombre",
      "saludar('Ana', 'Hey', 'Extra') — tres argumentos"
    ],
    correct: 1,
    explanation: "<code>nombre</code> es <strong>obligatorio</strong> (no tiene valor por defecto). <code>saludo</code> es <strong>opcional</strong> (tiene default 'Hola'). Así que <code>saludar('Ana')</code> funciona perfecto: nombre='Ana', saludo='Hola'."
  },
  {
    title: "Scope (alcance) de variables",
    question: "Si defino una variable <code>x = 10</code> DENTRO de una función, ¿puedo usarla FUERA de esa función?",
    options: [
      "Sí, todas las variables son globales en Python.",
      "No, las variables definidas dentro de una función son LOCALES y solo existen mientras la función se ejecuta.",
      "Sí, pero solo si la función tiene return.",
      "Depende de si usamos while o for dentro de la función."
    ],
    correct: 1,
    explanation: "Las variables creadas dentro de una función tienen <strong>alcance local</strong>: nacen cuando la función se ejecuta y mueren cuando termina. Fuera de la función, esa variable <code>x</code> no existe. Esto se llama <strong>scope</strong>."
  },
  {
    title: "Múltiples returns",
    question: "¿Puede una función tener más de un <code>return</code>?",
    options: [
      "No, Python lanza un SyntaxError si hay más de un return.",
      "Sí, pero SOLO se ejecutará el primero que Python encuentre en el flujo de ejecución. Después de un return, la función TERMINA.",
      "Sí, y Python ejecuta todos los return en orden.",
      "Solo si están dentro de un ciclo for."
    ],
    correct: 1,
    explanation: "Puedes tener varios <code>return</code> (por ejemplo, dentro de un if/else), pero en cuanto Python ejecuta UNO, la función <strong>termina inmediatamente</strong>. Es como un 'break' definitivo de la función."
  }
];

// ── VERDADERO O FALSO ──
const funcTfExercises = [
  {
    title: "Llamar vs Definir",
    statement: "Definir una función con <code>def</code> NO ejecuta su código. El código dentro de la función solo se ejecuta cuando la <strong>llamas</strong> por su nombre con paréntesis, por ejemplo: <code>mi_funcion()</code>.",
    correct: true,
    explanation: "¡Verdadero! <code>def</code> solo 'registra' la función en memoria. Es como escribir una receta: no se cocina sola. Debes LLAMARLA con <code>mi_funcion()</code> para que se ejecute."
  },
  {
    title: "Orden de definición",
    statement: "Puedo llamar a una función ANTES de definirla en el código (es decir, usar <code>saludar()</code> en la línea 1 y definirla en la línea 5) y Python la encontrará sin problemas.",
    correct: false,
    explanation: "¡Falso! Python lee el código de arriba hacia abajo. Si llamas a una función antes de definirla, obtienes un <code>NameError: name 'saludar' is not defined</code>. Siempre define ANTES de llamar."
  },
  {
    title: "Parámetros obligatorios",
    statement: "Si una función se define como <code>def calcular(a, b):</code> con dos parámetros, puedo llamarla con un solo argumento: <code>calcular(5)</code>.",
    correct: false,
    explanation: "¡Falso! Si la función tiene 2 parámetros sin valor por defecto, DEBES pasar 2 argumentos. Llamar <code>calcular(5)</code> lanza <code>TypeError: calcular() missing 1 required positional argument: 'b'</code>."
  },
  {
    title: "Funciones que llaman funciones",
    statement: "Una función puede llamar a OTRA función dentro de su cuerpo. Por ejemplo, <code>funcion_a()</code> puede ejecutar <code>funcion_b()</code> internamente.",
    correct: true,
    explanation: "¡Verdadero! Es muy común y recomendado. Las funciones pueden llamar a otras funciones, creando una cadena de operaciones modulares. Esto es la base de la <strong>programación funcional</strong>."
  },
  {
    title: "return detiene la función",
    statement: "Cuando Python ejecuta un <code>return</code>, la función se detiene INMEDIATAMENTE. Cualquier código que esté DESPUÉS del return dentro de la misma función NO se ejecutará jamás.",
    correct: true,
    explanation: "¡Verdadero! <code>return</code> es como una puerta de salida inmediata. Todo código después de un return ejecutado es 'código muerto' (dead code) que nunca se alcanza."
  },
  {
    title: "Modificar listas dentro de funciones",
    statement: "Si paso una lista como argumento a una función y la modifico dentro (por ejemplo, con <code>.append()</code>), la lista original FUERA de la función también se modifica.",
    correct: true,
    explanation: "¡Verdadero! Las listas son <strong>mutables</strong> y se pasan por referencia. Modificar la lista dentro de la función afecta al original. Esto NO pasa con strings, números o tuplas (son inmutables)."
  },
  {
    title: "Nombre de funciones",
    statement: "Puedo nombrar una función igual que una variable existente (por ejemplo, tener <code>edad = 25</code> y luego <code>def edad():</code>) y Python mantendrá ambas sin conflicto.",
    correct: false,
    explanation: "¡Falso! Si defines <code>def edad():</code> después de <code>edad = 25</code>, la función <strong>sobrescribe</strong> la variable. Ahora <code>edad</code> apunta a la función, no al número 25. ¡Nunca reutilices nombres!"
  },
  {
    title: "Retornar múltiples valores",
    statement: "Una función en Python puede retornar MÚLTIPLES valores separados por coma: <code>return a, b, c</code>. Python los empaqueta automáticamente en una tupla.",
    correct: true,
    explanation: "¡Verdadero! <code>return x, y</code> devuelve la tupla <code>(x, y)</code>. Puedes desempaquetar: <code>resultado_a, resultado_b = mi_funcion()</code>. ¡Muy útil y pythónico!"
  }
];

// ── UNIR CONCEPTOS (MATCHING) ──
const funcMatchExercises = [
  {
    title: "Anatomía de una Función",
    pairs: [
      { id: "fm1", left: "<code>def</code>", right: "Palabra clave para definir una función" },
      { id: "fm2", left: "Parámetro", right: "Variable placeholder en la definición" },
      { id: "fm3", left: "Argumento", right: "Valor real pasado al llamar la función" },
      { id: "fm4", left: "<code>return</code>", right: "Devuelve un valor y termina la función" },
      { id: "fm5", left: "Scope local", right: "Variable que solo existe dentro de la función" },
      { id: "fm6", left: "<code>None</code>", right: "Lo que devuelve una función sin return" }
    ]
  },
  {
    title: "Tipos de Parámetros",
    pairs: [
      { id: "fm7", left: "<code>def f(a, b)</code>", right: "Dos parámetros obligatorios" },
      { id: "fm8", left: "<code>def f(a, b=10)</code>", right: "Un obligatorio y uno con valor por defecto" },
      { id: "fm9", left: "<code>f(5, b=20)</code>", right: "Uso de argumento con nombre (keyword)" },
      { id: "fm10", left: "<code>f(3, 7)</code>", right: "Argumentos posicionales (por orden)" }
    ]
  }
];

// ── ENCONTRAR EL ERROR ──
const funcErrorExercises = [
  {
    title: "El paréntesis olvidado",
    question: "El alumno definió una función pero Python no la ejecuta. ¿Dónde está el error?",
    code: `def saludar():
    print("¡Hola mundo!")

saludar`,
    options: [
      "Falta indentar el print() dentro de la función",
      "La función no tiene parámetros, eso causa el error",
      "Falta los paréntesis al LLAMAR a la función: debe ser <code>saludar()</code> con paréntesis.",
      "Debería usarse 'function' en vez de 'def'"
    ],
    correct: 2,
    explanation: "Sin paréntesis, <code>saludar</code> es solo una referencia al objeto función, NO una llamada. Para ejecutar la función DEBES agregar paréntesis: <code>saludar()</code>."
  },
  {
    title: "Argumento fantasma",
    question: "Este código lanza un TypeError al ejecutarse. ¿Por qué?",
    code: `def sumar(a, b):
    return a + b

resultado = sumar(5)
print(resultado)`,
    options: [
      "La función sumar no puede retornar valores numéricos",
      "Falta un argumento: la función espera 2 (a y b) pero solo recibió 1.",
      "El return debería ser print en su lugar",
      "No se puede guardar el resultado de una función en una variable"
    ],
    correct: 1,
    explanation: "<code>sumar(a, b)</code> requiere <strong>2 argumentos obligatorios</strong>. Al llamar <code>sumar(5)</code> solo pasamos uno → <code>TypeError: sumar() missing 1 required positional argument: 'b'</code>."
  },
  {
    title: "El return inalcanzable",
    question: "La función siempre devuelve None aunque tenga un return. ¿Cuál es el problema?",
    code: `def calcular_doble(numero):
    print(numero * 2)
    return numero * 2

resultado = calcular_doble(5)
# resultado es None... ¿por qué?`,
    options: [
      "No se puede multiplicar dentro de una función",
      "El truco: este código SÍ funciona correctamente. resultado vale 10, no None.",
      "Debería usar += en vez de * 2",
      "El print() antes del return absorbe el valor y lo anula"
    ],
    correct: 1,
    explanation: "¡Trampa! Este código <strong>SÍ funciona bien</strong>. <code>print()</code> muestra '10' en consola y luego <code>return</code> devuelve 10. <code>resultado</code> vale 10, no None. El comentario del código es engañoso a propósito. 🧠"
  },
  {
    title: "Variable local escapista",
    question: "El alumno quiere usar la variable 'mensaje' fuera de la función pero obtiene un NameError. ¿Por qué?",
    code: `def crear_saludo(nombre):
    mensaje = f"¡Hola {nombre}!"
    return mensaje

crear_saludo("Ana")
print(mensaje)`,
    options: [
      "Los f-strings no funcionan dentro de funciones",
      "La variable 'mensaje' es LOCAL a la función y no existe fuera de ella. Debería guardar el return: <code>msg = crear_saludo('Ana')</code>.",
      "Falta importar el módulo de strings",
      "La función debería usar print() en vez de return"
    ],
    correct: 1,
    explanation: "<code>mensaje</code> es una variable <strong>local</strong> que solo vive dentro de <code>crear_saludo</code>. Fuera, no existe. La solución: guardar lo que retorna → <code>msg = crear_saludo('Ana')</code> y luego <code>print(msg)</code>."
  },
  {
    title: "Parámetro por defecto mutable",
    question: "El alumno define el valor por defecto ANTES del obligatorio. ¿Qué pasa?",
    code: `def registrar(rol="estudiante", nombre):
    print(f"{nombre} es {rol}")

registrar("Ana")`,
    options: [
      "Python ejecuta todo sin problema porque el orden no importa",
      "Los parámetros con valor por defecto deben ir DESPUÉS de los obligatorios. Causa SyntaxError.",
      "El f-string tiene un error de formato",
      "No se puede usar strings como valores por defecto"
    ],
    correct: 1,
    explanation: "Regla de oro: los parámetros <strong>obligatorios primero</strong>, los opcionales (con default) <strong>después</strong>. <code>def registrar(nombre, rol='estudiante'):</code> es la forma correcta. Python lo exige por diseño."
  }
];

// ── COMPLETAR CÓDIGO ──
const funcCompleteExercises = [
  {
    title: "Tu primera función",
    question: "Completa el código para definir una función que reciba un nombre y muestre un saludo.",
    code: `____ saludar(nombre):
    print(f"¡Hola {nombre}!")

saludar____"Ana"____)`,
    options: [
      "function / [ / ]",
      "def / ( / )",
      "define / ( / )",
      "def / { / }"
    ],
    correct: 1,
    explanation: "Usamos <code>def</code> para definir y <strong>paréntesis ( )</strong> tanto en la definición como en la llamada: <code>def saludar(nombre):</code> y <code>saludar(\"Ana\")</code>."
  },
  {
    title: "Función con return",
    question: "Queremos una función que calcule el doble de un número y lo DEVUELVA (no lo imprima). Completa.",
    code: `def calcular_doble(numero):
    resultado = numero * 2
    ____ resultado

doble = calcular_doble(7)
print(f"El doble es: {____}")`,
    options: [
      "print / resultado",
      "return / doble",
      "send / doble",
      "give / resultado"
    ],
    correct: 1,
    explanation: "Usamos <code>return resultado</code> para DEVOLVER el valor. Luego, al llamar, guardamos: <code>doble = calcular_doble(7)</code>. La variable <code>doble</code> ahora vale 14."
  },
  {
    title: "Parámetro con valor por defecto",
    question: "La función debe saludar con 'Hola' por defecto, pero permitir cambiar el saludo. Completa.",
    code: `def saludar(nombre, saludo____"Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana")
saludar("Luis", "Hey")`,
    options: [
      " == ",
      " = ",
      " : ",
      " -> "
    ],
    correct: 1,
    explanation: "Para dar un valor por defecto usamos el signo <code>=</code> en la definición: <code>saludo=\"Hola\"</code>. Así, si no pasas ese argumento, usa 'Hola'. Si lo pasas, lo sobrescribe."
  },
  {
    title: "Función que procesa una lista",
    question: "Completa la función que recibe una lista de notas y retorna el promedio.",
    code: `def calcular_promedio(notas):
    total = ____(notas)
    cantidad = ____(notas)
    return total / cantidad

notas_alumno = [6.5, 7.0, 5.5, 6.0]
prom = calcular_promedio(notas_alumno)
print(f"Promedio: {prom}")`,
    options: [
      "sum / len",
      "add / count",
      "total / size",
      "sumar / contar"
    ],
    correct: 0,
    explanation: "<code>sum(notas)</code> suma todos los elementos de la lista y <code>len(notas)</code> cuenta cuántos hay. Dividir ambos da el promedio. Estas funciones built-in de Python son tus aliadas."
  },
  {
    title: "Llamar función dentro de otra",
    question: "Completa para que la función 'procesar' use internamente la función 'es_aprobado'.",
    code: `def es_aprobado(nota):
    return nota >= 4.0

def procesar(nombre, nota):
    if ____(nota):
        print(f"{nombre}: Aprobado")
    else:
        print(f"{nombre}: Reprobado")

procesar("Ana", 6.5)`,
    options: [
      "es_aprobado",
      "aprobado",
      "check",
      "nota >= 4.0"
    ],
    correct: 0,
    explanation: "Llamamos <code>es_aprobado(nota)</code> dentro de <code>procesar</code>. La función retorna True o False, que el if evalúa directamente. ¡Esto es modularización: cada función hace UNA cosa!"
  }
];

// ── TRAZAR CÓDIGO ──
const funcTraceExercises = [
  {
    title: "Función básica con return",
    question: "¿Qué imprime este código en la consola?",
    code: `def duplicar(n):
    return n * 2

resultado = duplicar(4)
print(resultado + 1)`,
    options: [
      "8",
      "9",
      "4",
      "Error"
    ],
    correct: 1,
    explanation: "<code>duplicar(4)</code> retorna 4 * 2 = 8. Se guarda en resultado = 8. Luego <code>print(8 + 1)</code> → imprime <strong>9</strong>."
  },
  {
    title: "Función con valor por defecto",
    question: "¿Qué imprime este código?",
    code: `def potencia(base, exponente=2):
    return base ** exponente

a = potencia(3)
b = potencia(2, 3)
print(a, b)`,
    options: [
      "3 2",
      "6 6",
      "9 8",
      "9 6"
    ],
    correct: 2,
    explanation: "<code>potencia(3)</code> usa exponente=2 por defecto → 3² = 9. <code>potencia(2, 3)</code> → 2³ = 8. Imprime <strong>9 8</strong>."
  },
  {
    title: "Scope y variables locales",
    question: "¿Qué imprime este código?",
    code: `x = 100

def modificar():
    x = 50
    return x

resultado = modificar()
print(x, resultado)`,
    options: [
      "50 50",
      "100 50",
      "50 100",
      "100 100"
    ],
    correct: 1,
    explanation: "La <code>x = 50</code> dentro de la función es <strong>local</strong> — no modifica la x global. La función retorna 50 (resultado=50). La x global sigue siendo 100. Imprime <strong>100 50</strong>."
  },
  {
    title: "Función que llama función",
    question: "¿Qué imprime este código?",
    code: `def doble(n):
    return n * 2

def sumar_dobles(a, b):
    return doble(a) + doble(b)

print(sumar_dobles(3, 4))`,
    options: [
      "7",
      "12",
      "14",
      "24"
    ],
    correct: 2,
    explanation: "<code>doble(3)</code> = 6, <code>doble(4)</code> = 8. <code>sumar_dobles</code> retorna 6 + 8 = <strong>14</strong>."
  },
  {
    title: "return temprano con if",
    question: "¿Qué imprime este código?",
    code: `def clasificar(nota):
    if nota >= 6.0:
        return "Excelente"
    if nota >= 4.0:
        return "Aprobado"
    return "Reprobado"

print(clasificar(6.5))
print(clasificar(3.0))`,
    options: [
      "Aprobado / Reprobado",
      "Excelente / Reprobado",
      "Excelente / Aprobado",
      "Reprobado / Reprobado"
    ],
    correct: 1,
    explanation: "6.5 >= 6.0 → retorna 'Excelente' (no sigue evaluando). 3.0: no cumple ningún if → llega al último return → 'Reprobado'. Imprime <strong>Excelente</strong> y <strong>Reprobado</strong>."
  },
  {
    title: "Acumulador funcional",
    question: "¿Qué imprime este programa?",
    code: `def sumar_lista(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

datos = [10, 20, 30]
resultado = sumar_lista(datos)
print(resultado * 2)`,
    options: [
      "60",
      "120",
      "30",
      "Error"
    ],
    correct: 1,
    explanation: "<code>sumar_lista([10,20,30])</code> acumula 10+20+30 = 60. Luego <code>resultado * 2</code> = 60 * 2 = <strong>120</strong>."
  }
];

// ── TICKET DE ENTRADA (CONTRARRELOJ) ──
const funcTicketEntradaData = [
  {
    title: "La Pizzería de Python",
    question: "Si tu programa fuera una pizzería, ¿qué representaría exactamente una <strong>'función'</strong>?",
    options: [
      "El horno donde se cocinan las cosas",
      "Un ingrediente secreto (como el pepperoni)",
      "El repartidor que lleva la pizza",
      "La receta escrita que puedes usar mil veces"
    ],
    correct: 3,
    explanation: "Una función es como una <strong>receta</strong>. La escribes una sola vez y luego cualquier cocinero (tu código) puede usarla mil veces para hacer exactamente la misma pizza sin tener que inventarla de nuevo."
  },
  {
    title: "El Secreto del Scope",
    question: "El 'Scope local' (las variables creadas <em>dentro</em> de una función) se comporta exactamente igual a...",
    options: [
      "Lo que pasa en Las Vegas, se queda en Las Vegas",
      "Un chisme: todos en el programa lo terminan sabiendo",
      "Una ley mundial que aplica en todas partes",
      "Un tatuaje permanente en el disco duro"
    ],
    correct: 0,
    explanation: "¡Lo que pasa en la función, se queda en la función! Las variables locales <strong>nacen y mueren</strong> dentro de la función. Fuera de ella, nadie sabe que existieron."
  },
  {
    title: "El Misterio del Return",
    question: "Si usas <code>print()</code> en lugar de <code>return</code> al final de tu función, es como si...",
    options: [
      "Te cobraran el doble por ejecutar el código",
      "Gritaras la respuesta al aire, pero no la guardaras",
      "Python se enojara y apagara tu computadora",
      "Mandaras un paquete por correo certificado"
    ],
    correct: 1,
    explanation: "<code>print()</code> solo 'habla' por el megáfono (la pantalla), pero al programa se le olvida. <code>return</code> empaca el dato y te lo <strong>entrega en la mano</strong> para que puedas seguir trabajando con él."
  },
  {
    title: "Moldes y Galletas",
    question: "¿Cuál es la diferencia entre un 'Parámetro' y un 'Argumento'?",
    options: [
      "Parámetro es texto y Argumento es número",
      "El parámetro es el molde vacío, el argumento es la masa",
      "Son exactamente lo mismo, solo cambia el país",
      "El argumento es un insulto en programación"
    ],
    correct: 1,
    explanation: "Al <strong>definir</strong> la función usas parámetros (moldes esperando ser llenados). Al <strong>llamar</strong> a la función le envías argumentos (la masa real que pones dentro del molde)."
  }
];

// ── TICKET DE SALIDA (METACOGNICIÓN) ──
const funcTicketSalidaQuestions = [
  "¿Cómo le explicarías la diferencia entre 'print' y 'return' a tu abuelita?",
  "¿En qué tipo de proyecto de la vida real crees que las funciones te salvarían la vida (frente a usar solo código lineal)?",
  "Piensa en el 'Scope'. ¿Por qué crees que los creadores de Python decidieron que las variables mueran cuando la función termina?",
  "Si tuvieras que explicarle a un compañero de clase qué es un 'parámetro' usando la analogía de una receta de cocina, ¿qué le dirías?"
];
