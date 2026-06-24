// ═══════════════════════════════════════════════════════════════
//  📦 Datos de Ejercicios — Módulos, Librerías y Proyectos Multi-Archivo
//  ─────────────────────────────────────────────────────────────
//  Variables globales consumidas por modulos-y-proyectos.html
// ═══════════════════════════════════════════════════════════════

// ── SELECCIÓN MÚLTIPLE ──
var modChoiceExercises = [
  {
    title: "La Librería Estándar",
    question: "¿Qué significa que Python viene 'con pilas incluidas' (Librería Estándar)?",
    options: [
      "Que el instalador ocupa mucho espacio en el disco duro.",
      "Que ya trae incorporados muchos módulos (como math, random, os) listos para usar sin necesidad de instalarlos.",
      "Que no necesitas un cargador para la laptop.",
      "Que instala todas las librerías del mundo automáticamente."
    ],
    correct: 1,
    explanation: "¡Exacto! Python trae una colección gigante de código ya escrito por profesionales (la librería estándar) que puedes usar de inmediato con la palabra clave <code>import</code>."
  },
  {
    title: "Importando módulos",
    question: "¿Cuál es la forma correcta de importar SOLO la función `sqrt` del módulo `math`?",
    options: [
      "import sqrt from math",
      "import math.sqrt",
      "from math import sqrt",
      "include math.sqrt"
    ],
    correct: 2,
    explanation: "La sintaxis es <code>from [módulo] import [función]</code>. Al hacerlo así, puedes usar <code>sqrt()</code> directamente sin escribir <code>math.sqrt()</code>."
  },
  {
    title: "El módulo random",
    question: "¿Qué hace la función `random.randint(1, 10)`?",
    options: [
      "Genera un número decimal aleatorio entre 1 y 10.",
      "Elige un número al azar de una lista predefinida.",
      "Genera un número entero aleatorio entre 1 y 10 (ambos incluidos).",
      "Lanza un error porque falta el parámetro 'seed'."
    ],
    correct: 2,
    explanation: "<code>randint(a, b)</code> devuelve un entero aleatorio N tal que a &lt;= N &lt;= b. Es ideal para simular dados o elegir posiciones aleatorias."
  },
  {
    title: "Entornos Virtuales (venv)",
    question: "¿Por qué es crucial usar entornos virtuales al trabajar con librerías externas?",
    options: [
      "Porque hacen que Python corra más rápido en la RAM.",
      "Para jugar videojuegos en un emulador.",
      "Para aislar las librerías de cada proyecto y evitar que las versiones de un proyecto rompan a otro.",
      "Porque pip no funciona sin un entorno virtual."
    ],
    correct: 2,
    explanation: "Los entornos virtuales son como 'habitaciones separadas'. Si el Proyecto A necesita Django 3 y el Proyecto B necesita Django 4, el entorno virtual evita que colisionen."
  },
  {
    title: "El gestor de paquetes pip",
    question: "¿Para qué se utiliza el comando `pip list`?",
    options: [
      "Para listar todos los archivos Python en una carpeta.",
      "Para mostrar todas las librerías instaladas en el entorno actual y sus versiones.",
      "Para crear una lista de compras en un archivo txt.",
      "Para desinstalar todas las librerías de una vez."
    ],
    correct: 1,
    explanation: "<code>pip list</code> te muestra qué paquetes están instalados en el entorno donde lo ejecutas. Es muy útil para saber qué herramientas tienes disponibles."
  },
  {
    title: "Archivo requirements.txt",
    question: "¿Cuál es la utilidad principal del archivo `requirements.txt` en un proyecto Python?",
    options: [
      "Guardar los requerimientos de hardware del programa.",
      "Anotar los requisitos que pidió el profesor para la nota.",
      "Guardar las contraseñas de las bases de datos.",
      "Listar todas las librerías externas y sus versiones exactas para que otra persona pueda clonar el proyecto y hacerlo funcionar."
    ],
    correct: 3,
    explanation: "¡Exacto! Alguien más puede correr <code>pip install -r requirements.txt</code> y tendrá exactamente el mismo entorno que tú."
  },
  {
    title: "Proyectos Multi-Archivo",
    question: "Si tienes un archivo `utilidades.py` con una función `limpiar()`, ¿cómo la usas en `main.py`?",
    options: [
      "import limpiar de utilidades.py",
      "import utilidades.limpiar",
      "from utilidades import limpiar",
      "Ejecutando ambos archivos a la vez en la consola."
    ],
    correct: 2,
    explanation: "Los archivos `.py` en la misma carpeta actúan como módulos. Usas <code>from [nombre_archivo_sin_py] import [función]</code>."
  },
  {
    title: "El misterio de __name__",
    question: "¿Para qué sirve el patrón `if __name__ == '__main__':` al final de un archivo?",
    options: [
      "Para declarar la función principal del programa (es obligatorio en Python).",
      "Para evitar que cierto código se ejecute automáticamente si el archivo es importado por otro módulo.",
      "Para verificar si el usuario tiene permisos de administrador.",
      "Para importar todos los módulos de la carpeta 'main'."
    ],
    correct: 1,
    explanation: "¡Clave! Si tu archivo tiene código suelto, se ejecutará al importarlo. Al poner ese código dentro de <code>if __name__ == '__main__':</code>, solo se ejecuta si corres ESE archivo directamente."
  }
];

// ── VERDADERO O FALSO ──
var modTfExercises = [
  {
    title: "Descargar math",
    statement: "Para usar el módulo <code>math</code>, primero debes descargarlo usando <code>pip install math</code> en la terminal.",
    correct: false,
    explanation: "¡Falso! <code>math</code> es parte de la Librería Estándar de Python. Viene incluido desde la instalación, solo necesitas hacer <code>import math</code> en tu código."
  },
  {
    title: "Renombrar al importar",
    statement: "Puedes importar un módulo y ponerle un apodo (alias) usando la palabra clave <code>as</code>, por ejemplo: <code>import random as rnd</code>.",
    correct: true,
    explanation: "¡Verdadero! Esto es muy útil y común, especialmente para módulos con nombres largos (ej. <code>import pandas as pd</code>)."
  },
  {
    title: "Instalación global",
    statement: "Es una buena práctica instalar todas las librerías externas de forma global (sin usar venv) para así tenerlas siempre disponibles y ahorrar espacio en el disco duro.",
    correct: false,
    explanation: "¡Falso y peligroso! Instalar globalmente crea el temido 'Dependency Hell' (infierno de dependencias) donde actualizar un paquete rompe 5 proyectos antiguos. Usa <strong>SIEMPRE</strong> un entorno virtual."
  },
  {
    title: "Módulos propios",
    statement: "En Python, cualquier archivo que crees con extensión <code>.py</code> puede funcionar como un módulo y ser importado por otro archivo en la misma carpeta.",
    correct: true,
    explanation: "¡Verdadero! Tu archivo <code>calculos.py</code> es un módulo a los ojos de Python. Puedes hacer <code>import calculos</code> desde <code>main.py</code>."
  },
  {
    title: "El archivo requirements.txt",
    statement: "El comando <code>pip freeze > requirements.txt</code> captura todas las librerías instaladas en tu entorno actual y las guarda en un archivo de texto.",
    correct: true,
    explanation: "¡Verdadero! Es la forma estándar en Python de 'tomarle una foto' a tu entorno para poder compartir tu proyecto."
  },
  {
    title: "Variables entre archivos",
    statement: "Si creas una variable <code>puntos = 100</code> en el archivo <code>jugador.py</code>, no hay forma de leer ese valor desde <code>main.py</code>.",
    correct: false,
    explanation: "¡Falso! Puedes importarla igual que una función: <code>from jugador import puntos</code>. Aunque, cuidado, no es buena práctica importar variables globales mutables."
  },
  {
    title: "Módulo random y strings",
    statement: "El módulo <code>random</code> solo funciona con números. No puede elegir un elemento al azar de una lista de strings.",
    correct: false,
    explanation: "¡Falso! <code>random.choice(['rojo', 'azul', 'verde'])</code> elige un elemento aleatorio de la lista, sin importar si son strings."
  },
  {
    title: "Carpetas __pycache__",
    statement: "Cuando importas un archivo tuyo en otro archivo, Python crea automáticamente una carpeta misteriosa llamada <code>__pycache__</code>. No debes borrarla, ni debes subirla a GitHub.",
    correct: true,
    explanation: "¡Verdadero! Python pre-compila el código importado para que corra más rápido y lo guarda ahí. Es normal. Se ignora siempre en Git (poner en .gitignore)."
  }
];

// ── UNIR CONCEPTOS ──
var modMatchExercises = [
  {
    title: "Funciones Útiles de Módulos",
    pairs: [
      { id: "mm1", left: "<code>random.randint()</code>", right: "Genera entero al azar" },
      { id: "mm2", left: "<code>math.sqrt()</code>", right: "Calcula la raíz cuadrada" },
      { id: "mm3", left: "<code>random.choice()</code>", right: "Elige elemento al azar de lista" },
      { id: "mm4", left: "<code>random.shuffle()</code>", right: "Desordena una lista" },
      { id: "mm5", left: "<code>math.ceil()</code>", right: "Redondea hacia arriba" },
      { id: "mm6", left: "<code>math.pi</code>", right: "La constante 3.1415..." }
    ]
  },
  {
    title: "Terminal y Entornos (Mac/Linux/Windows)",
    pairs: [
      { id: "mm7", left: "<code>python -m venv .venv</code>", right: "Crea el entorno virtual" },
      { id: "mm8", left: "<code>source .venv/bin/activate</code>", right: "Activa el entorno (Mac/Linux)" },
      { id: "mm9", left: "<code>pip install requests</code>", right: "Descarga e instala una librería" },
      { id: "mm10", left: "<code>pip freeze</code>", right: "Muestra versiones instaladas" },
      { id: "mm11", left: "<code>.venv\\Scripts\\activate</code>", right: "Activa el entorno (Windows)" }
    ]
  }
];

// ── ENCONTRAR EL ERROR ──
var modErrorExercises = [
  {
    title: "Buscando fuera de la caja",
    question: "El alumno quiere una raíz cuadrada, pero Python se enoja. ¿Qué falta?",
    code: `numero = 25
resultado = sqrt(numero)
print("La raíz es:", resultado)`,
    options: [
      "sqrt solo funciona con números negativos.",
      "Falta importar el módulo: <code>from math import sqrt</code> en la línea 1.",
      "La función se llama raiz_cuadrada() en Python.",
      "Debe guardarlo en un diccionario primero."
    ],
    correct: 1,
    explanation: "<code>sqrt</code> vive dentro del módulo <code>math</code>. Python no la conoce por defecto. Debes decirle de dónde sacarla con un <code>import</code>."
  },
  {
    title: "Instalación misteriosa",
    question: "El estudiante intentó instalar una librería, pero la consola le escupió un 'SyntaxError'. ¿Por qué?",
    code: `# Dentro del archivo main.py
print("Iniciando mi programa...")
pip install colorama
print("Programa terminado")`,
    options: [
      "colorama ya no existe en PyPI.",
      "Debería ser 'install pip colorama'.",
      "pip install es un comando de la TERMINAL, no código Python. No se escribe dentro del archivo .py.",
      "Le falta el import pip antes de usarlo."
    ],
    correct: 2,
    explanation: "¡Error clásico! <code>pip</code> se ejecuta en la consola (terminal/bash/cmd) del sistema operativo, NO adentro de tu script de Python."
  },
  {
    title: "El import al revés",
    question: "Python dice 'SyntaxError: invalid syntax'. ¿Qué hizo mal?",
    code: `import randint from random

numero_magico = randint(1, 100)
print(numero_magico)`,
    options: [
      "randint no funciona con números grandes.",
      "La sintaxis es al revés: <code>from random import randint</code>.",
      "random es una librería externa, necesita pip install.",
      "randint lleva un solo parámetro."
    ],
    correct: 1,
    explanation: "La gramática de Python es estricta: <code>from [módulo] import [cosa]</code>. ¡Memoriza ese orden!"
  },
  {
    title: "El archivo ruidoso",
    question: "Alguien creó 'utilidades.py'. En 'main.py' hace <code>import utilidades</code>, e inmediatamente se imprime 'Limpiando base de datos...' sin que nadie lo pida. ¿Por qué?",
    code: `# utilidades.py
def limpiar_db():
    print("Base de datos limpia")

print("Limpiando base de datos...")`,
    options: [
      "main.py llamó a la función automáticamente.",
      "Al importar un archivo, Python EJECUTA todo el código suelto. Ese print() no estaba dentro de una función ni protegido por un <code>if __name__ == '__main__':</code>.",
      "utilidades.py es una palabra reservada.",
      "Es un virus en la carpeta del proyecto."
    ],
    correct: 1,
    explanation: "Cuando haces un import, Python lee el archivo de arriba a abajo y lo corre. Si tienes un <code>print()</code> (o peor, una eliminación de archivos) suelto, se ejecutará. Por eso protegemos el código principal con <code>if __name__ == '__main__':</code>."
  },
  {
    title: "Colisión de nombres",
    question: "El alumno creó un archivo genial llamado 'random.py' para probar cosas, pero ahora su programa se cae y dice 'module has no attribute randint'. ¿Qué pasó?",
    code: `# archivo: random.py (creado por el alumno)
import random

dado = random.randint(1, 6)
print(dado)`,
    options: [
      "El dado solo puede ir de 1 a 5.",
      "El alumno nombró su archivo 'random.py'. Cuando intenta importar 'random', Python importa el propio archivo del alumno en lugar de la librería estándar (Shadowing).",
      "Le falta el if __name__.",
      "random requiere internet."
    ],
    correct: 1,
    explanation: "¡Nunca nombres tus archivos igual que los módulos de la librería estándar (math.py, random.py, os.py)! Python busca primero en tu carpeta local. Le diste tu propio archivo y se confundió. Esto se llama 'Shadowing' (sombrear)."
  }
];

// ── COMPLETAR CÓDIGO ──
var modCompleteExercises = [
  {
    title: "Importar y usar",
    question: "Completa el código para generar un número entre 1 y 10 usando la librería estándar.",
    code: `import ____

num = ____.randint(1, 10)
print(num)`,
    options: [
      "math / math",
      "random / random",
      "os / os",
      "rand / rand"
    ],
    correct: 1,
    explanation: "Se importa el módulo <code>random</code> completo, y luego se accede a sus funciones con la notación de punto: <code>random.randint()</code>."
  },
  {
    title: "Importar función específica",
    question: "Completa para importar SOLO choice y usarlo sin el prefijo del módulo.",
    code: `from ____ import ____

colores = ["rojo", "azul", "verde"]
elegido = ____(colores)
print(elegido)`,
    options: [
      "random / choice / choice",
      "math / choice / random.choice",
      "math / randint / randint",
      "random / choice / random.choice"
    ],
    correct: 0,
    explanation: "<code>from random import choice</code> te permite usar <code>choice(colores)</code> directamente, lo cual hace el código más limpio si vas a usar esa función muchas veces."
  },
  {
    title: "Módulos Propios",
    question: "Tienes el archivo 'validacion.py'. En tu 'main.py' quieres usar su función 'es_valido'. Completa el import en main.py.",
    code: `# En main.py
____ validacion ____ es_valido

if ____("correo@test.com"):
    print("Acceso concedido")`,
    options: [
      "import / from / es_valido",
      "from / import / es_valido",
      "from / import / validacion.es_valido",
      "import / with / es_valido"
    ],
    correct: 1,
    explanation: "Tu propio archivo actúa como un módulo normal. <code>from validacion import es_valido</code> es perfecto."
  },
  {
    title: "Alias de módulos",
    question: "Completa para importar datetime y ponerle el apodo 'dt'.",
    code: `import datetime ____ dt

hoy = ____.datetime.now()
print(hoy)`,
    options: [
      "like / dt",
      "as / datetime",
      "as / dt",
      "is / dt"
    ],
    correct: 2,
    explanation: "Usamos la palabra <code>as</code> para dar un alias (apodo). Luego usamos ese apodo en lugar del nombre original."
  },
  {
    title: "El guardia de seguridad",
    question: "Completa el bloque de código para que el menú solo se ejecute si este archivo se corre directamente (no si es importado).",
    code: `def mostrar_menu():
    print("1. Jugar")

if ____ == ____:
    mostrar_menu()`,
    options: [
      "__main__ / '__name__'",
      "__name__ / '__main__'",
      "__file__ / '__main__'",
      "name / main"
    ],
    correct: 1,
    explanation: "El patrón exacto es <code>if __name__ == '__main__':</code>. Literalmente significa 'Si mi nombre interno es el archivo principal que arrancó, ejecuta esto'."
  }
];

// ── TRAZAR CÓDIGO ──
var modTraceExercises = [
  {
    title: "Trazar importaciones cruzadas",
    question: "Si ejecutas `main.py`, ¿qué imprime en la consola?",
    code: `# util.py
def duplicar(x):
    return x * 2

# main.py
from util import duplicar

valor = duplicar(5)
print(valor + 3)`,
    options: [
      "10",
      "5",
      "13",
      "Error"
    ],
    correct: 2,
    explanation: "main.py importa <code>duplicar</code>. Llama a duplicar(5) que devuelve 10. Luego imprime 10 + 3 = 13."
  },
  {
    title: "Trazar con __name__",
    question: "Si corres `main.py` en la terminal, ¿qué se imprime?",
    code: `# motor.py
print("A")
def arrancar():
    print("B")

if __name__ == '__main__':
    print("C")

# main.py
import motor
print("D")
motor.arrancar()`,
    options: [
      "D B",
      "A C D B",
      "A D B",
      "C D B"
    ],
    correct: 2,
    explanation: "1. main.py hace import motor. Python lee motor.py.\n2. Imprime 'A'.\n3. El if __name__ == '__main__' es FALSO (motor fue importado, no es el principal), así que NO imprime 'C'.\n4. Vuelve a main.py, imprime 'D'.\n5. Llama a motor.arrancar(), que imprime 'B'. \nResultado: A D B."
  },
  {
    title: "Trazar con random (Simulación)",
    question: "Asumiendo que random.randint(1, 10) casualmente devuelve 5, ¿qué imprime esto?",
    code: `import random
from math import sqrt

# supongamos que genera un 5
aleatorio = random.randint(1, 10) 
aleatorio = aleatorio + 4
resultado = sqrt(aleatorio)

print(int(resultado))`,
    options: [
      "9",
      "3",
      "5",
      "4"
    ],
    correct: 1,
    explanation: "aleatorio = 5. aleatorio = 5 + 4 = 9. sqrt(9) = 3.0. int(3.0) = 3."
  },
  {
    title: "Variables en otros módulos",
    question: "¿Qué imprime el programa al correr `juego.py`?",
    code: `# config.py
vidas = 3

# juego.py
import config

config.vidas -= 1
print(config.vidas)`,
    options: [
      "Error, config no es modificable",
      "3",
      "2",
      "-1"
    ],
    correct: 2,
    explanation: "Sí puedes acceder a variables de otro módulo y mutarlas usando <code>modulo.variable</code>. Imprime 2. (Aunque no se recomienda hacer esto sin getters/setters o clases, funciona)."
  },
  {
    title: "Alias de funciones",
    question: "¿Qué imprime este código?",
    code: `from math import floor as piso

numero = 4.8
resultado = piso(numero)
print(resultado)`,
    options: [
      "4",
      "5",
      "4.8",
      "Error de sintaxis"
    ],
    correct: 0,
    explanation: "Se importa la función <code>floor</code> (que redondea hacia abajo) y se le da el alias <code>piso</code>. Piso de 4.8 es 4."
  }
];

// ── TICKET DE ENTRADA ──
var modTicketEntradaData = [
  {
    title: "El Concepto de Función",
    question: "¿Para qué nos sirve empaquetar código dentro de un bloque <code>def mi_funcion():</code>?",
    options: [
      "Para que el código se ejecute automáticamente apenas abrimos el archivo.",
      "Para darle un nombre a un bloque de instrucciones y poder reutilizarlo muchas veces sin repetir código.",
      "Para que el computador corra más rápido porque ocupa menos memoria.",
      "Para crear variables que nunca cambien de valor."
    ],
    correct: 1,
    explanation: "¡Exacto! Las funciones son 'mini-programas' dentro de tu código. Escribes la receta una sola vez y la 'llamas' cada vez que tienes hambre."
  },
  {
    title: "La Entrega del Paquete",
    question: "Si una función hace un cálculo matemático, ¿cómo logramos que le entregue el resultado al resto del programa para seguir usándolo?",
    options: [
      "Usando un print() dentro de la función.",
      "Usando un ciclo while infinito.",
      "Usando la palabra mágica 'return' para devolver el valor.",
      "Las funciones no pueden devolver resultados, solo mostrar texto."
    ],
    correct: 2,
    explanation: "El 'return' es la forma en que una función 'escupe' el resultado hacia afuera. Un print() solo lo muestra en pantalla, pero no te deja guardar el valor en una variable."
  },
  {
    title: "Variables Atrapadas",
    question: "¿Qué pasa si creo una variable llamada <code>puntos_vida</code> DENTRO de una función, e intento leerla DESDE AFUERA de la función?",
    options: [
      "Funciona perfecto porque todas las variables en Python son públicas.",
      "Python me arrojará un error porque la variable 'nace y muere' dentro de la función (Scope local).",
      "El valor se borrará de inmediato del disco duro.",
      "Tengo que pagar una licencia premium de Python."
    ],
    correct: 1,
    explanation: "Las variables creadas dentro de un 'def' son privadas (locales). Lo que pasa en la función, se queda en la función... a menos que lo devuelvas con un return."
  },
  {
    title: "El Orden de las Cosas",
    question: "Si tengo el código: <br><code>saludar()</code><br><code>def saludar(): print('Hola')</code><br>¿Qué ocurrirá al ejecutarlo?",
    options: [
      "Imprimirá 'Hola' en la consola.",
      "Arrojará un error porque no puedo llamar a una función que aún no ha sido definida.",
      "Se quedará pensando para siempre.",
      "Ignorará el llamado y no hará nada."
    ],
    correct: 1,
    explanation: "Python lee el código de arriba hacia abajo. Debes 'enseñarle' (definir) la función primero antes de intentar llamarla (usarla)."
  }
];

// ── TICKET DE SALIDA ──
var modTicketSalidaQuestions = [
  "Si un compañero te dice: 'Quiero usar una función para sacar la raíz cuadrada, ¿tengo que hacer mi propia función matemática?', ¿qué le responderías sobre la Librería Estándar?",
  "Explica con tus propias palabras qué significa el archivo 'requirements.txt' y por qué un equipo de trabajo lo agradecería.",
  "¿Por qué es una mala idea llamar a un archivo de tu proyecto 'random.py' o 'math.py'?",
  "Reflexión: Ahora que puedes crear varios archivos .py y conectarlos con import... ¿cómo organizarías los archivos si tuvieras que programar un sistema de gestión para un Hospital?"
];
