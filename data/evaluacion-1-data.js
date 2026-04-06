const EVALUACION_DATA = {
  header: {
    title: "Evaluación Formativa - Programación Básica",
    subtitle: "Simulador de Prueba Universitaria | Tiempo estimado: 2 a 3 horas",
    instructions: "Esta evaluación contiene una mezcla de preguntas teóricas, conceptos y 3 ejercicios prácticos de desarrollo. Lee atentamente cada enunciado."
  },
  alternativas: [
    {
      id: "alt1",
      question: "¿Cuál de las siguientes es una forma correcta de declarar una variable entera en Python?",
      options: ["entero x = 10", "int x = 10", "x = 10", "x := 10"],
      answer: 2,
      explanation: "En Python, la asignación de variables es dinámica y directa, no requiere declarar el tipo explícitamente."
    },
    {
      id: "alt2",
      question: "¿Qué operador se utiliza para calcular el residuo (resto) de una división?",
      options: ["/", "//", "%", "**"],
      answer: 2,
      explanation: "El operador % entrega el residuo de una división entera (módulo)."
    },
    {
      id: "alt3",
      question: "Si se ejecuta el código: if 5 > 2 and 4 < 1: ... ¿Se cumple la condición?",
      options: ["Sí, ambas son verdaderas.", "Sí, al menos una es verdadera.", "No, porque 4 < 1 es falso y se usa 'and'.", "Ocurrirá un error de sintaxis."],
      answer: 2,
      explanation: "Para que una condición con 'and' se cumpla, todas las subcondiciones deben ser verdaderas."
    },
    {
      id: "alt4",
      question: "¿Cuál es el propósito principal de un ciclo 'while'?",
      options: ["Ejecutar código un número fijo de veces conocido de antemano.", "Repetir un bloque de código mientras una condición siga siendo verdadera.", "Detener el programa inmediatamente si hay un error.", "Declarar variables repetitivas."],
      answer: 1,
      explanation: "El ciclo 'while' repite instrucciones bajo la evaluación de su condición en cada iteración."
    },
    {
      id: "alt5",
      question: "Si tengo la variable x = '10', y quiero sumarle 5, ¿qué debo hacer antes?",
      options: ["Nada, Python lo suma automáticamente.", "Convertir '10' a int usando int(x).", "Convertir 5 a string y sumarlos matemáticamente.", "Multiplicar por 1."],
      answer: 1,
      explanation: "La variable x es un string, debes castearla con int(x) para poder realizar una operación aritmética con el número 5."
    }
  ],
  verdaderoFalso: [
    {
      id: "vf1",
      statement: "En Python, la indentación (los espacios al inicio de la línea) es solo para que el código se vea ordenado y no afecta la ejecución.",
      answer: false,
      explanation: "Falso. La indentación en Python es obligatoria y define los bloques de código."
    },
    {
      id: "vf2",
      statement: "Un ciclo infinito ocurre comúnmente en un 'while' si olvidamos actualizar la variable que controla la condición.",
      answer: true,
      explanation: "Verdadero. Si la condición nunca cambia a Falsa, el ciclo no terminará jamás."
    },
    {
      id: "vf3",
      statement: "La función input() siempre devuelve el valor ingresado por el usuario en formato de texto (string).",
      answer: true,
      explanation: "Verdadero. Todo lo capturado mediante input() viene como cadena de texto."
    },
    {
      id: "vf4",
      statement: "No es posible colocar un 'if' dentro de otro 'if'.",
      answer: false,
      explanation: "Falso. Se pueden anidar múltiples niveles de 'if' y otras estructuras de control (if anidados)."
    },
    {
      id: "vf5",
      statement: "El operador '==' se usa para asignar un valor a una variable, mientras que '=' se utiliza para comparar.",
      answer: false,
      explanation: "Falso. Es al revés: '=' asigna valor y '==' compara igualdad."
    }
  ],
  terminosPareados: {
    itemsIzquierda: [
      { id: "A", text: "float()" },
      { id: "B", text: "break" },
      { id: "C", text: "elif" },
      { id: "D", text: "!= " },
      { id: "E", text: "print()" }
    ],
    itemsDerecha: [
      { id: "1", text: "Muestra información por pantalla." },
      { id: "2", text: "Detiene la ejecución del ciclo más interno, forzando la salida." },
      { id: "3", text: "Permite evaluar una condición adicional si el bloque 'if' no se cumple." },
      { id: "4", text: "Convierte un valor de texto o entero en un número con decimales." },
      { id: "5", text: "Operador lógico que verifica si dos valores son diferentes." }
    ],
    paresCorrectos: { "A": "4", "B": "2", "C": "3", "D": "5", "E": "1" }
  },
  diagramaFlujo: {
    description: "Analiza el siguiente código, que representa el funcionamiento lógico de un control de acceso para una montaña rusa. Traza el código asumiendo que los ingresos del usuario son: edad = 14, altura = 1.35.",
    code: `edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en metros: "))

if edad >= 18:
    print("Acceso total permitido.")
elif edad >= 12:
    if altura >= 1.40:
        print("Acceso permitido a todas las atracciones juveniles.")
    else:
        print("Acceso limitado a atracciones infantiles por altura.")
else:
    print("Acceso solo a zona kids.")`,
    question: "¿Qué mensaje se imprimirá en pantalla?",
    options: [
      "Acceso total permitido.",
      "Acceso permitido a todas las atracciones juveniles.",
      "Acceso limitado a atracciones infantiles por altura.",
      "Acceso solo a zona kids."
    ],
    answer: 2,
    explanation: "La edad es 14, así que entra al 'elif edad >= 12'. Luego, evalúa si 1.35 >= 1.40 (Falso), por lo que ejecuta el bloque 'else' interno."
  },
  ejerciciosPricipales: [
    {
      id: "ej1",
      dificultad: "Leve",
      titulo: "El Cálculo de Gastos Simples",
      enunciado: `Estás creando un pequeño sistema para que un estudiante universitario dimensione sus gastos semanales en la fotocopiadora y colaciones. \n\n**Requerimientos:**\n1. Solicitar al usuario cuánto dinero gasta diariamente en almuerzo (entero).\n2. Solicitar al usuario cuántas impresiones realiza al día (entero), sabiendo que cada impresión vale $50 pesos.\n3. Calcular el gasto total que se proyecta considerando una semana universitaria de Lunes a Viernes (5 días).\n4. Si el gasto semanal total supera los $20000, mostrar un mensaje: "Alerta: Presupuesto alto". Si no, mostrar: "Presupuesto moderado".`,
      puntos: 15
    },
    {
      id: "ej2",
      dificultad: "Intermedio",
      titulo: "Tienda de Suplementos (Con Ciclos)",
      enunciado: `Una tienda vende potes de proteína. El usuario puede agregar potes hasta que decida finalizar. \n\n**Requerimientos:**\n1. Utiliza un ciclo (while) para preguntar repetidamente al usuario el precio de un suplemento a agregar al carrito. Si ingresa "0" u otro número de salida que definas, el ciclo debe terminar.\n2. Lleva la cuenta del **total a pagar** y de la **cantidad de productos** ingresados.\n3. Si el usuario compró 3 o más productos **en total**, aplícale un descuento del 10% al total al finalizar.\n4. Imprime el total final a pagar y la cantidad de productos comprados.`,
      puntos: 25
    },
    {
      id: "ej3",
      dificultad: "Complejo",
      titulo: "Simulación de Banco Virtual (Ciclos IF Anidados)",
      enunciado: `Se requiere programar el menú de un cajero automático muy rudimentario. Tienes un saldo inicial de $50000. El cajero muestra un menú y operará repetidamente hasta que se elija 'Salir'. \n\n**Menú:**\n1) Ver Saldo\n2) Girar Dinero\n3) Inversión\n4) Salir\n\n**El comportamiento debe ser el siguiente:**\n- Si elige 1: Muestra el saldo actual.\n- Si elige 2: Pregunta cuánto girar. **A su vez**, debes verificar que el monto solicitado sea menor o igual al saldo, y que sea múltiplo de 5000. Si cumple esto, realiza el giro (resta el saldo); si no, muestra el motivo del error ('Saldo insuficiente' o 'Monto no aceptado').\n- Si elige 3: Te ofrece invertir tu dinero. Te solicita una cantidad. Si esa cantidad es menor que o igual a tu saldo, te la duplica y la añade al saldo final de retorno, sino, muestra 'Saldo insuficiente'.\n- Si elige 4: Termina el programa imprimiendo "Cajero apagado".\n- Cualquier otra opción muestra 'Opción inválida'.\n\n**Usa while y condicionales anidados (if dentro de if equivalentes) para este desafío.**`,
      puntos: 40
    },
    {
      id: "ej4",
      dificultad: "Experto",
      titulo: "Batalla por Turnos: RPG de Texto",
      enunciado: `Crea un simulador de combate de un juego de rol. El jugador tiene 100 de Vida y 20 de Maná. El Jefe Final tiene 150 de Vida.\n\n**Requerimientos:**\n1. El programa corre mientras ambos sigan vivos (Vida > 0).\n2. En cada turno, el jugador elige una opción:\n   - **Atacar:** Quita 20 de vida al Jefe.\n   - **Magia (Gasta 5 maná):** Quita 50 de vida al Jefe. Solo funciona si tienes maná suficiente.\n   - **Poción de Vida:** Te cura 30 de vida pero gasta todo tu Maná restante.\n3. Tras el turno del jugador, si el Jefe sigue vivo, este ataca quitándote 15 de vida.\n4. Al final, indica si ganaste o el Jefe te derrotó.`,
      puntos: 45
    },
    {
      id: "ej5",
      dificultad: "Experto",
      titulo: "Inventario del Alquimista (Crafting)",
      enunciado: `El jugador debe fabricar 'Pociones de Fuego'. Tienes un inventario inicial con 0 Hierbas y 0 Frascos, y cuentas con $500 monedas de oro.\n\n**Menú:**\n1) Comprar Hierba ($50 c/u)\n2) Comprar Frasco ($100 c/u)\n3) Fabricar Poción (Requiere: 2 Hierbas y 1 Frasco)\n4) Salir\n\n**Lógica:**\n- Para comprar, debes validar si tienes dinero suficiente. Si compras, suma al inventario y resta al oro.\n- Para fabricar, debes validar si tienes materiales suficientes. Si fabricas, resta los materiales y suma 1 a 'Pociones Totales'.\n- Al salir, muestra cuántas pociones lograste hacer y cuánto oro te quedó.`,
      puntos: 50
    },
    {
      id: "ej6",
      dificultad: "Leyenda",
      titulo: "El Calabozo de las 3 Puertas (Anidados Pro)",
      enunciado: `Simula una aventura donde debes atravesar 3 habitaciones consecutivas para ganar.\n\n**Requerimientos:**\n1. Usa un ciclo para las 3 habitaciones (for i in range(1, 4)).\n2. En cada habitación, hay una puerta cerrada. El jugador debe elegir: 'Forzar', 'Ganzúa' o 'Buscar Llave'.\n3. **Lógica de la habitación:**\n   - Si elige 'Buscar Llave', hay un 50% de probabilidad (puedes simularlo pidiendo un número y viendo si es par) de encontrarla. Si la tiene, puede abrir.\n   - Si elige 'Ganzúa', debe tener la habilidad (pregunta al inicio del juego si es Ladrón o Guerrero). Solo el Ladrón abre con ganzúa.\n   - Si elige 'Forzar', debe ser Guerrero. \n4. Si el jugador no logra abrir la puerta tras 3 intentos fallidos por habitación (ciclo while interno), pierde el juego completo.`,
      puntos: 60
    }
  ]
};
