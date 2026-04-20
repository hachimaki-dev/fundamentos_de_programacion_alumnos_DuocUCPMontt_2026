const listasForChoiceExercises = [
  {
    title: "¿Para qué sirve principalmente un ciclo FOR?",
    question: "A diferencia del ciclo WHILE que repite mientras se cumpla una condición, ¿cuál es el objetivo central del FOR?",
    options: [
      "Repetir código infinitamente sin poder detenerse.",
      "Recorrer uno por uno los elementos de una colección (como una lista).",
      "Solo se usa para saltarse iteraciones con 'continue'.",
      "Validar contraseñas."
    ],
    correct: 1,
    explanation: "¡Exacto! El FOR brilla cuando necesitas procesar o recorrer elementos de una estructura de datos (como una lista o un rango) elemento por elemento."
  },
  {
    title: "Características de una Lista",
    question: "¿Cuáles de estas características definen mejor a una lista en Python?",
    options: [
      "Son desordenadas y no se pueden modificar.",
      "Solo pueden guardar números, nunca texto.",
      "Es una colección ordenada y modificable (mutable) de elementos.",
      "Una vez creada, es imposible agregarle más datos."
    ],
    correct: 2,
    explanation: "Las listas en Python son ordenadas (cada elemento tiene un índice de posición) y modificables (puedes agregar, borrar o cambiar elementos después de crearla)."
  },
  {
    title: "La función range()",
    question: "Si usas el ciclo `for i in range(3):`, ¿qué valores tomará 'i' en cada iteración?",
    options: [
      "1, 2, 3",
      "0, 1, 2, 3",
      "0, 1, 2",
      "3"
    ],
    correct: 2,
    explanation: "La función range() por defecto parte en 0 y termina un número antes del indicado. O sea: 0, 1 y 2 (tres iteraciones)."
  },
  {
    title: "Agregando elementos a una lista",
    question: "¿Qué método utilizamos para agregar un nuevo elemento al final de una lista ya existente?",
    options: [
      ".add()",
      ".append()",
      ".insert()",
      ".push()"
    ],
    correct: 1,
    explanation: "En Python, usamos el método `.append()` para anexar elementos al final de la lista de forma rápida y sencilla."
  },
  {
    title: "Removiendo a ciegas",
    question: "Si ejecutas `amigos.pop()` sin enviarle ningún argumento dentro de los paréntesis, ¿qué ocurrirá?",
    options: [
      "Elimina todos los elementos de la lista vaciándola.",
      "Elimina el primer elemento.",
      "Elimina el último elemento de la lista.",
      "Lanzará un error obligándote a pasar un número."
    ],
    correct: 2,
    explanation: "Por defecto, el método pop() funciona como una pila: expulsa y extrae siempre el último elemento agregado en el extremo derecho."
  },
  {
    title: "Inyecciones exactas",
    question: "Tengo mi_lista = ['A', 'C']. ¿Qué código debo ejecutar para que quede ['A', 'B', 'C']?",
    options: [
      "mi_lista.insert(1, 'B')",
      "mi_lista.append('B')",
      "mi_lista[1] = 'B'",
      "mi_lista.add(1, 'B')"
    ],
    correct: 0,
    explanation: "`.insert(indice, valor)` es tu bisturí. Insertar 'B' en el índice 1 hace que 'C' sea empujado al índice 2 pacíficamente salvando el orden."
  }
];

const listasForTfExercises = [
  {
    title: "Modificación de listas",
    statement: "Si tengo <code>notas = [5.0, 4.5, 6.0]</code>, ¿es válido hacer <code>notas[0] = 6.5</code> para cambiar el primer 5.0 a un 6.5?",
    correct: true,
    explanation: "Las listas son mutables, lo que significa que puedes acceder usando el índice y reescribir su valor en cualquier momento."
  },
  {
    title: "Combinando tipos de datos",
    statement: "En Python, una lista puede contener distintos tipos de datos, por ejemplo: <code>mezcla = ['Juan', 25, 4.5, True]</code>.",
    correct: true,
    explanation: "A diferencia de otros lenguajes, Python es muy flexible y permite mezclar strings, enteros, flotantes y booleanos en una sola lista."
  },
  {
    title: "Recorrido directo",
    statement: "Si hago <code>for color in ['Rojo', 'Azul']:</code>, la variable 'color' tomará los valores 0 y 1.",
    correct: false,
    explanation: "Falso. En el recorrido directo o por valor, la variable temporal 'color' toma el elemento en sí mismo (los textos 'Rojo' y 'Azul'), no la posición o índice."
  },
  {
    title: "Índice de inicio",
    statement: "Las posiciones (índices) en una lista comienzan siempre por el número 1.",
    correct: false,
    explanation: "Falso. ¡Cuidado con esto! En programación y en Python, la primera posición es el índice 0."
  },
  {
    title: "Doble uso de len()",
    statement: "La función <code>len()</code> solo sirve para saber la cantidad de elementos matemáticos de una lista completa, está prohibido usarlo sobre strings (cadenas de texto).",
    correct: false,
    explanation: "Para nada. El len() sirve transversalmente: mide la cantidad de bloques en una lista o la cantidad de letras en un string."
  },
  {
    title: "Peligros por la derecha",
    statement: "Usar un índice abusivo hacia atrás como <code>lista[-100]</code> en una lista de 3 elementos no arroja error, simplemente regresa el valor 0 de piso.",
    correct: false,
    explanation: "Error crítico. Al igual que irte hacia arriba causa un IndexError, irte hacia abajo buscando el infinito negativo también rompe la ejecución si sobrepasas los propios elementos."
  }
];

const listasForMatchExercises = [
  {
    title: "Conceptos Fundamentales de Listas y Ciclos",
    pairs: [
      { id: "m1", left: "<code>append()</code>", right: "Agrega elemento al final" },
      { id: "m2", left: "<code>len()</code>", right: "Obtiene cantidad de elementos" },
      { id: "m3", left: "Lista modificable", right: "Se pueden cambiar sus datos" },
      { id: "m4", left: "Índice", right: "Posición de un elemento (0, 1...)" },
      { id: "m5", left: "<code>range()</code>", right: "Genera secuencia de números" }
    ]
  }
];

const listasForErrorExercises = [
  {
    title: "Error accediendo a la lista",
    question: "Este programa intenta mostrar la última nota, pero la consola arroja IndexError. ¿Dónde está el error?",
    code: `notas = [5.5, 6.0, 4.0]
# Queremos imprimir la nota 4.0
print(notas[3])`,
    options: [
      "No existe la variable notas",
      "Los corchetes son para diccionarios, no para listas",
      "El índice máximo es 2, no 3, ya que empezamos a contar desde 0.",
      "print no puede imprimir números"
    ],
    correct: 2,
    explanation: "La lista tiene 3 elementos. Sus posiciones son 0 (5.5), 1 (6.0) y 2 (4.0). Intentar acceder al índice 3 genera un desbordamiento o IndexError."
  },
  {
    title: "Olvidar inicializar el acumulador",
    question: "El profe quiere sumar todas las donaciones de una lista. Hay un error conceptual importante, ¿cuál es?",
    code: `donaciones = [1000, 500, 2000]

for monto in donaciones:
    total = total + monto

print(f"Recolectado: {total}")`,
    options: [
      "Faltan los paréntesis en el for",
      "La variable 'total' no existe antes de usarse en la suma",
      "El for debe usar range() obligatoriamente",
      "Las listas no se pueden recorrer así"
    ],
    correct: 1,
    explanation: "¡Exacto! Debes inicializar 'total = 0' ANTES del for. Si Python lee 'total = total + monto' sin saber cuánto valía total antes, arroja NameError."
  },
  {
    title: "Sobredosis de argumentos",
    question: "Quieres agregar dos frutas juntas al final. ¿Por qué Python nos grita con un TypeError al correr esto?",
    code: `frutas = ["Manzana", "Pera"]
frutas.append("Kiwi", "Fresa")`,
    options: [
      "Las frutas deben agregarse obligatoriamente con .insert",
      "El método .append() solo acepta exactamente 1 argumento por vez.",
      "Faltan corchetes rodeando a 'Kiwi' y 'Fresa'",
      "El compilador en español lanza problemas de lectura"
    ],
    correct: 1,
    explanation: "El método append está construido nativamente para adherir estrictamente UNA entidad cada vez. Si le mandas dos cosas seguidas con coma romperá el protocolo."
  },
  {
    title: "Volátil o Permanente",
    question: "El alumno cree que está sumando 1 punto a todas las notas, pero al hacer print final se da cuenta que la lista original sigue intacta. ¿Por qué?",
    code: `notas = [4.0, 5.0, 3.5]

for nota in notas:
    nota = nota + 1.0

print(notas) # Sigue saliendo [4.0, 5.0, 3.5]`,
    options: [
      "El for debe tener la instrucción break en su cola.",
      "Agregó '1.0' en float, debe agregarse en string.",
      "Está modificando la copia 'nota', en lugar de usar índices para afectar a la raíz original (notas[i]).",
      "Está prohibido usar suma en listas procesadas."
    ],
    correct: 2,
    explanation: "El recorrido directo (for n in lista) otorga lecturas en copia sin vínculo. Todo lo que le sumes o cambies allí se pierde en el viento. Debió ser recorrido posicional con range."
  }
];

const listasForCompleteExercises = [
  {
    title: "Recorriendo y Mostrando Notas",
    question: "Completa el código para que el FOR extraiga cada valor real de la lista y lo imprima en consola.",
    code: `notas_taller = [6.5, 7.0, 5.8]

for ____ in notas_taller:
    print(f"Obtuviste un: {____}")`,
    options: [
      "i / i+1",
      "nota / nota",
      "0 / notas_taller",
      "len / len"
    ],
    correct: 1,
    explanation: "Usamos una variable descriptiva (como 'nota') para que tome el valor de cada elemento dentro de la lista 'notas_taller' en cada iteración."
  },
  {
    title: "Contando elementos bajo condición",
    question: "Queremos contar cuántos estudiantes superaron los 50 puntos. Rellena los huecos.",
    code: `puntajes = [45, 60, 30, 80, 55]
contador = 0

for p in ____:
    if p > 50:
        ____ += 1
        
print("Aprobados:", contador)`,
    options: [
      "range / p",
      "puntajes / contador",
      "listas / contador",
      "puntajes / p"
    ],
    correct: 1,
    explanation: "El for recorre 'puntajes' (p in puntajes). Si p es mayor a 50, sumamos 1 a nuestra variable acumuladora 'contador'."
  },
  {
    title: "El Recorrido Peligroso",
    question: "Modifiquemos agresivamente la raíz profunda de las notas utilizando la llave posicional i. Pega la combinación correcta.",
    code: `mis_notas = [4.5, 4.0, 3.0]

for i in range(____):
    mis_notas[____] = mis_notas[i] + 0.5`,
    options: [
      "3 / len(mis_notas)",
      "len(mis_notas) / i",
      "mis_notas / mis_notas[i]",
      "len() / mis_notas"
    ],
    correct: 1,
    explanation: "El rango limitador es la longitud abstracta (len(mis_notas)) de la lista original. Usamos dinámicamente nuestra llave corcheteadora [i] para fijar la escritura por vuelta."
  },
  {
    title: "Tubería de Filtrado",
    question: "Completa el embudo: Queremos ver una lista llena de números filtrando a los reprobados, extrayéndolos a una nueva sala VIP pasándoles por el filtro de aprobación.",
    code: `pool_alumnos = [3.0, 7.0, 2.0, 6.0]
sala_vip = []

for score in pool_alumnos:
    if score >= 4.0:
        sala_vip.____(____)`,
    options: [
      "insert / score",
      "add / score",
      "append / pool_alumnos",
      "append / score"
    ],
    correct: 3,
    explanation: "Por cada variable score clon extraída, si da como verdad mayor que 4.0 la lanzamos e inyectamos a las catacumbas finales de la sala_vip empleando astutamente .append(score)."
  }
];

const listasForTraceExercises = [
  {
    title: "Suma de Positivos",
    question: "¿Qué valor imprimirá la variable 'suma' al final del programa?",
    code: `numeros = [10, -5, 20, -1]
suma = 0

for num in numeros:
    if num > 0:
        suma += num

print(suma)`,
    options: [
      "24",
      "30",
      "10",
      "0"
    ],
    correct: 1,
    explanation: "Correcto. El if filtra y solo deja pasar a los mayores que cero. 10 es mayor a cero (suma=10). -5 no pasa. 20 es mayor a cero (suma=10+20=30). -1 no pasa. Total = 30."
  },
  {
    title: "Buscando Tesoros (Filtrado)",
    question: "¿Cuántas veces se imprimirá la palabra '¡Oro encontrado!'?",
    code: `cofres = ['Piedra', 'Oro', 'Madera', 'Oro', 'Tierra']
oro_count = 0

for item in cofres:
    if item == 'Oro':
        print('¡Oro encontrado!')
        oro_count += 1`,
    options: [
      "1",
      "2",
      "3",
      "5"
    ],
    correct: 1,
    explanation: "La lista tiene dos veces el string 'Oro' (índice 1 e índice 3). El condicional coincidirá exactamente 2 veces."
  },
  {
    title: "Trazo Ciego: Pop Art",
    question: "Trata de reconstruir matemáticamente en el vacío qué contendrá la imprenta final.",
    code: `baraja = ["As", "Rey", "Reina", "Jota"]
baraja.pop()
baraja.insert(1, "Comodin")

print(baraja[1])`,
    options: [
      "As",
      "Reina",
      "Comodin",
      "Rey"
    ],
    correct: 2,
    explanation: "1) pop elimina la pobre Jota del final. 2) insert coloca el Comodin ocupando el lugar 1 absoluto. La respuesta posicional del nuevo dictado es Comodin directo."
  },
  {
    title: "Trazo Extremo: El Buscador Máximo",
    question: "¿Qué rol secreto cumple la variable 'mayor' una vez acabado el proceso final impreso?",
    code: `vidas = [10, 80, 40, 20]
mayor = vidas[0]

for vel in vidas:
    if vel > mayor:
        mayor = vel

print(mayor)`,
    options: [
      "No hace nada, imprime 10 estático",
      "Suma todos calculando un promedio",
      "Imprime todos los números por turnos",
      "Escanea y memoriza quedándose con el valor más alto (80)"
    ],
    correct: 3,
    explanation: "El clásico algoritmo King of the Hill (Rey de la colina). Empezando desde el primer número como base supuesta, contrasta a ver si hay algo más potente rotando iterativamente. Al encontrarlo reemplaza su valor. Terminando es 80."
  }
];
