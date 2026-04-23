// ═══════════════════════════════════════════════════════════════
//  🗄️ EA2 — Clase 1: Introducción al RA2 y DML Básico
//  ─────────────────────────────────────────────────────────────
//  Datos de ejercicios interactivos para Oracle SQL DML
//  INSERT, UPDATE, DELETE, WHERE, Claves PK/FK
// ═══════════════════════════════════════════════════════════════

// ── Selección Múltiple ──
const ea2Clase1ChoiceExercises = [
  {
    title: '🔮 Predice el Resultado del UPDATE',
    question: 'Dada la tabla ALUMNOS con 5 filas (RUTs: 101, 102, 103, 104, 105), ¿cuántas filas modifica esta sentencia?\n\nUPDATE ALUMNOS SET carrera = \'Informática\' WHERE rut IN (101, 103, 105);',
    code: "UPDATE ALUMNOS\nSET carrera = 'Informática'\nWHERE rut IN (101, 103, 105);",
    options: [
      'Modifica 1 fila (solo la primera coincidencia)',
      'Modifica 3 filas (las que cumplen la condición IN)',
      'Modifica 5 filas (todas las de la tabla)',
      'Error ORA: la cláusula IN no es válida en UPDATE'
    ],
    correct: 1,
    explanation: '<strong>✅ Correcto: Modifica 3 filas.</strong> La cláusula <code>WHERE rut IN (101, 103, 105)</code> filtra exactamente las 3 filas cuyos RUT coinciden. El operador <code>IN</code> es totalmente válido en UPDATE y actúa como un <code>OR</code> múltiple: <code>rut = 101 OR rut = 103 OR rut = 105</code>. Cada fila que cumpla la condición será actualizada.'
  },
  {
    title: '⚡ Elige la Sentencia Correcta',
    question: 'Necesitas cambiar la nota del alumno con RUT 20345678 en la asignatura "Base de Datos" a 6.5. ¿Cuál sentencia es la correcta?',
    code: "-- Tabla NOTAS(id_nota, rut_alumno, asignatura, nota)\n-- Objetivo: cambiar nota a 6.5 para RUT 20345678 en 'Base de Datos'",
    options: [
      "UPDATE NOTAS SET nota = 6.5 WHERE rut_alumno = 20345678;",
      "UPDATE NOTAS SET nota = 6.5 WHERE rut_alumno = 20345678 AND asignatura = 'Base de Datos';",
      "UPDATE nota = 6.5 FROM NOTAS WHERE rut_alumno = 20345678 AND asignatura = 'Base de Datos';",
      "MODIFY NOTAS SET nota = 6.5 WHERE rut_alumno = 20345678 AND asignatura = 'Base de Datos';"
    ],
    correct: 1,
    explanation: '<strong>✅ Opción B es la correcta.</strong> Necesitamos filtrar por <em>dos</em> condiciones: el RUT <strong>y</strong> la asignatura. La opción A solo filtra por RUT, lo que modificaría <em>todas</em> las notas de ese alumno (¡peligroso!). La opción C usa una sintaxis incorrecta (<code>FROM</code> no va en UPDATE). La opción D inventa el comando <code>MODIFY</code>, que no existe en SQL estándar.'
  },
  {
    title: '💀 El DELETE sin WHERE',
    question: '¿Qué ocurre si ejecutas esta sentencia en producción?\n\nDELETE FROM NOTAS;',
    code: "DELETE FROM NOTAS;",
    options: [
      'Oracle muestra una advertencia y te pide confirmación antes de borrar',
      'Elimina solo la primera fila de la tabla NOTAS',
      'Elimina TODAS las filas de la tabla NOTAS sin pedir confirmación',
      'Error ORA: DELETE requiere obligatoriamente una cláusula WHERE'
    ],
    correct: 2,
    explanation: '<strong>⚠️ ¡PELIGRO MÁXIMO!</strong> Un <code>DELETE FROM tabla</code> sin <code>WHERE</code> elimina <strong>absolutamente TODAS las filas</strong> de la tabla, sin preguntar, sin advertencia, sin red de seguridad. Oracle <strong>no</strong> exige WHERE — es tu responsabilidad como desarrollador incluirlo. En un entorno profesional, esto podría ser un desastre catastrófico. <em>Regla de oro: SIEMPRE escribe el WHERE antes de ejecutar un DELETE.</em>'
  },
  {
    title: '🧩 ¿Qué va primero?',
    question: 'Tienes las tablas ALUMNOS(rut PK, nombre) y NOTAS(id_nota PK, rut_alumno FK→ALUMNOS, nota). ¿En qué orden debes insertar los datos?',
    code: "-- Tabla ALUMNOS: rut (PK), nombre, carrera\n-- Tabla NOTAS:   id_nota (PK), rut_alumno (FK → ALUMNOS), asignatura, nota\n\n-- ¿Qué insertas primero?",
    options: [
      'Primero las NOTAS y luego el ALUMNO, porque la nota necesita existir antes',
      'El orden no importa, Oracle resuelve las dependencias automáticamente',
      'Primero el ALUMNO y luego las NOTAS, porque la FK referencia al alumno',
      'Hay que insertar ambos en la misma sentencia INSERT'
    ],
    correct: 2,
    explanation: '<strong>✅ Primero el ALUMNO.</strong> La clave foránea (<code>FK</code>) en NOTAS apunta a ALUMNOS. Esto significa que Oracle verifica que el <code>rut_alumno</code> exista en ALUMNOS antes de aceptar la inserción en NOTAS. Si intentas insertar una nota para un alumno que no existe, Oracle lanzará: <strong>ORA-02291: integrity constraint violated — parent key not found</strong>. Es como intentar asignar una nota a un fantasma: primero debe existir el estudiante.'
  },
  {
    title: '🎯 Anatomía del INSERT',
    question: '¿Cuál de estos INSERT es sintácticamente correcto para Oracle SQL?',
    code: "-- Tabla ALUMNOS(rut NUMBER, nombre VARCHAR2(100), carrera VARCHAR2(50))",
    options: [
      "INSERT ALUMNOS VALUES (12345678, 'Ana López', 'Informática');",
      "INSERT INTO ALUMNOS VALUES (12345678, 'Ana López', 'Informática');",
      "INSERT INTO ALUMNOS SET rut=12345678, nombre='Ana López', carrera='Informática';",
      "INSERT INTO ALUMNOS (12345678, 'Ana López', 'Informática');"
    ],
    correct: 1,
    explanation: '<strong>✅ Opción B es correcta.</strong> La sintaxis de Oracle SQL requiere <code>INSERT INTO tabla VALUES (...)</code>. La opción A omite la palabra clave <code>INTO</code> (obligatoria en Oracle). La opción C usa sintaxis de MySQL (<code>SET</code>), que Oracle no admite. La opción D omite la palabra <code>VALUES</code>. <em>Recuerda: INSERT <strong>INTO</strong> tabla <strong>VALUES</strong> (...)</em>.'
  },
  {
    title: '🔍 WHERE como Guardián',
    question: '¿Cuál es la diferencia fundamental entre estas dos sentencias?',
    code: "-- Sentencia A:\nUPDATE ALUMNOS SET carrera = 'Diseño';\n\n-- Sentencia B:\nUPDATE ALUMNOS SET carrera = 'Diseño' WHERE rut = 101;",
    options: [
      'No hay diferencia, ambas actualizan la misma fila',
      'A actualiza TODAS las filas, B solo la fila con rut 101',
      'A genera error porque falta WHERE, B es la única válida',
      'A actualiza la primera fila, B actualiza la última'
    ],
    correct: 1,
    explanation: '<strong>✅ La clave es el WHERE.</strong> Sin <code>WHERE</code>, la sentencia A modifica <strong>todas</strong> las filas de la tabla — ¡cada alumno quedaría en carrera "Diseño"! Con <code>WHERE rut = 101</code>, la sentencia B solo toca la fila que cumple esa condición. <strong>WHERE es tu guardián:</strong> sin él, UPDATE y DELETE operan sobre TODA la tabla. Esta es la regla más importante que aprenderás en DML.'
  },
];

// ── Verdadero o Falso ──
const ea2Clase1TfExercises = [
  {
    title: '🔑 Clave Primaria y NULL',
    statement: 'Una columna definida como <strong>PRIMARY KEY</strong> puede contener valores <code>NULL</code>.',
    correct: false,
    explanation: '<strong>❌ Falso.</strong> La clave primaria (PK) tiene dos restricciones implícitas: <code>NOT NULL</code> (no acepta nulos) y <code>UNIQUE</code> (no acepta duplicados). Si intentas insertar NULL en una PK, Oracle lanzará <strong>ORA-01400: cannot insert NULL</strong>. La PK es el "documento de identidad" de cada fila: no puede estar vacío ni repetirse.'
  },
  {
    title: '🔗 Clave Foránea Huérfana',
    statement: 'Si insertas un registro en la tabla NOTAS con un <code>rut_alumno</code> que <strong>no existe</strong> en la tabla ALUMNOS, Oracle lo acepta sin problemas.',
    correct: false,
    explanation: '<strong>❌ Falso.</strong> La clave foránea (FK) garantiza la <em>integridad referencial</em>. Oracle verifica que el valor de <code>rut_alumno</code> exista como PK en ALUMNOS. Si no existe, lanza: <strong>ORA-02291: integrity constraint violated — parent key not found</strong>. Es una protección fundamental: no puedes crear una nota para un alumno que no está registrado.'
  },
  {
    title: '📝 DELETE vs DROP',
    statement: '<code>DELETE FROM ALUMNOS;</code> elimina las filas de la tabla, pero la tabla sigue existiendo y se puede volver a llenar con datos.',
    correct: true,
    explanation: '<strong>✅ Verdadero.</strong> <code>DELETE</code> es un comando <strong>DML</strong> que elimina filas (datos), pero conserva la estructura de la tabla (columnas, restricciones, índices). La tabla queda "vacía pero viva". En cambio, <code>DROP TABLE</code> es un comando <strong>DDL</strong> que destruye la tabla completa (estructura + datos). Son niveles muy diferentes de destrucción.'
  },
  {
    title: '⚙️ Orden de Columnas en INSERT',
    statement: 'Al usar <code>INSERT INTO tabla VALUES (...)</code> sin especificar columnas, los valores deben ir en el <strong>mismo orden</strong> en que se definieron las columnas al crear la tabla.',
    correct: true,
    explanation: '<strong>✅ Verdadero.</strong> Cuando omites la lista de columnas, Oracle espera los valores en el orden exacto de definición de la tabla. Si la tabla es <code>ALUMNOS(rut, nombre, carrera)</code>, debes poner <code>VALUES(rut, nombre, carrera)</code> en ese orden. Si los inviertes, podrías obtener errores de tipo de dato o, peor aún, datos cruzados sin error visible. <em>Buena práctica: siempre especifica las columnas explícitamente.</em>'
  },
  {
    title: '🔄 UPDATE sin SET',
    statement: 'La sentencia <code>UPDATE ALUMNOS WHERE rut = 101;</code> es válida en Oracle SQL.',
    correct: false,
    explanation: '<strong>❌ Falso.</strong> La cláusula <code>SET</code> es <strong>obligatoria</strong> en toda sentencia UPDATE. Sin ella, Oracle no sabe qué columna modificar ni a qué valor. La sintaxis correcta es: <code>UPDATE tabla <strong>SET</strong> columna = valor WHERE condición;</code>. Omitir SET genera un error de sintaxis inmediato: <strong>ORA-00971: missing SET keyword</strong>.'
  },
  {
    title: '🧱 DML vs DDL',
    statement: '<code>INSERT</code>, <code>UPDATE</code> y <code>DELETE</code> pertenecen al grupo de comandos <strong>DDL</strong> (Data Definition Language).',
    correct: false,
    explanation: '<strong>❌ Falso.</strong> INSERT, UPDATE y DELETE son comandos <strong>DML</strong> (Data Manipulation Language) — manipulan <em>datos</em> dentro de tablas existentes. Los comandos <strong>DDL</strong> (CREATE, ALTER, DROP) manipulan la <em>estructura</em> de la base de datos (tablas, vistas, índices). Es una distinción clave: DML toca datos, DDL toca estructura.'
  },
];

// ── Encontrar el Error ──
const ea2Clase1ErrorExercises = [
  {
    title: '🐛 Caza el Bug del INSERT',
    code: "INSERT INTO ALUMNOS (rut, nombre, carrera)\nVALUES ('Ana López', 12345678, 'Informática');",
    question: '¿Cuál es el error en esta sentencia INSERT?',
    options: [
      'Falta el punto y coma al final',
      'El orden de los valores no coincide con el orden de las columnas (nombre y rut están invertidos)',
      'No se puede usar VARCHAR2 en la columna rut',
      'Falta la palabra INTO después de INSERT'
    ],
    correct: 1,
    explanation: '<strong>🐛 ¡Bug encontrado!</strong> Las columnas dicen <code>(rut, nombre, carrera)</code> pero los valores son <code>(\'Ana López\', 12345678, \'Informática\')</code>. El primer valor <code>\'Ana López\'</code> se intenta guardar en <code>rut</code> (que es NUMBER) → <strong>ORA-01722: invalid number</strong>. La corrección es: <code>VALUES (12345678, \'Ana López\', \'Informática\')</code>. <em>Regla: el orden de VALUES debe coincidir exactamente con el orden de las columnas especificadas.</em>'
  },
  {
    title: '🐛 El UPDATE Traicionero',
    code: "UPDATE NOTAS\nSET nota = 7.0, asignatura = 'Redes'\nWHERE rut_alumno = 20345678;",
    question: 'Un profesor quiere SOLO cambiar la nota a 7.0 para el alumno 20345678 en "Base de Datos". ¿Qué problema tiene esta sentencia?',
    options: [
      'No se pueden actualizar dos columnas en un solo UPDATE',
      'Falta filtrar por asignatura Y además está cambiando la asignatura cuando solo debía cambiar la nota',
      'La sintaxis de la coma entre SET está mal',
      'WHERE debe ir antes de SET'
    ],
    correct: 1,
    explanation: '<strong>🐛 ¡Doble problema!</strong> Primero: falta <code>AND asignatura = \'Base de Datos\'</code> en el WHERE, así que modifica TODAS las notas de ese alumno. Segundo: también está cambiando la asignatura a \'Redes\', que no era la intención. La sentencia correcta sería: <code>UPDATE NOTAS SET nota = 7.0 WHERE rut_alumno = 20345678 AND asignatura = \'Base de Datos\';</code>. <em>Un UPDATE mal filtrado puede causar daños masivos silenciosos.</em>'
  },
  {
    title: '🐛 DELETE con FK Activa',
    code: "-- Tabla ALUMNOS(rut PK, nombre, carrera)\n-- Tabla NOTAS(id_nota PK, rut_alumno FK → ALUMNOS, nota)\n-- El alumno con rut 101 tiene 3 notas registradas.\n\nDELETE FROM ALUMNOS WHERE rut = 101;",
    question: '¿Qué ocurrirá al ejecutar esta sentencia?',
    options: [
      'Se elimina el alumno y sus 3 notas automáticamente',
      'Se elimina solo el alumno, las notas quedan huérfanas',
      'Oracle rechaza el DELETE con ORA-02292 porque hay registros hijos (notas) que dependen de ese alumno',
      'Oracle convierte las notas a NULL y luego elimina al alumno'
    ],
    correct: 2,
    explanation: '<strong>🛡️ La FK protege la integridad.</strong> Como existen notas que referencian al alumno 101, Oracle lanza <strong>ORA-02292: integrity constraint violated — child record found</strong>. No puedes eliminar un "padre" mientras tenga "hijos" dependientes. Primero debes eliminar las notas del alumno y luego eliminar al alumno. <em>(A menos que la FK tenga ON DELETE CASCADE, pero eso es otra historia.)</em>'
  },
  {
    title: '🐛 El INSERT Incompleto',
    code: "-- Tabla ALUMNOS(rut NUMBER NOT NULL, nombre VARCHAR2(100) NOT NULL, carrera VARCHAR2(50))\n\nINSERT INTO ALUMNOS (rut, carrera)\nVALUES (12345678, 'Informática');",
    question: '¿Qué error provocará esta sentencia?',
    options: [
      'Error: no se puede omitir la columna carrera',
      'Error: la columna nombre es NOT NULL y no se le asignó valor',
      'Se ejecuta correctamente, nombre queda como cadena vacía',
      'Error: faltan paréntesis en la cláusula VALUES'
    ],
    correct: 1,
    explanation: '<strong>🐛 ¡Violación de NOT NULL!</strong> La columna <code>nombre</code> está definida como <code>NOT NULL</code>, lo que significa que es obligatoria. Al omitirla en el INSERT, Oracle intenta asignarle <code>NULL</code> por defecto, pero la restricción lo impide: <strong>ORA-01400: cannot insert NULL into ("ALUMNOS"."NOMBRE")</strong>. <em>Regla: siempre verifica qué columnas son obligatorias antes de insertar.</em>'
  },
];

// ── Unir Conceptos (Match) ──
const ea2Clase1MatchExercises = [
  {
    title: '🔗 Conecta cada comando con su función',
    pairs: [
      { id: 'm1', left: '<code>INSERT INTO</code>', right: 'Agrega nuevas filas a una tabla' },
      { id: 'm2', left: '<code>UPDATE ... SET</code>', right: 'Modifica valores existentes en filas' },
      { id: 'm3', left: '<code>DELETE FROM</code>', right: 'Elimina filas de una tabla' },
      { id: 'm4', left: '<code>WHERE</code>', right: 'Filtra qué filas son afectadas' },
      { id: 'm5', left: '<code>PRIMARY KEY</code>', right: 'Identifica cada fila de forma única' },
      { id: 'm6', left: '<code>FOREIGN KEY</code>', right: 'Vincula una tabla con otra (integridad referencial)' },
    ]
  },
  {
    title: '🔗 Errores ORA y su significado',
    pairs: [
      { id: 'e1', left: '<code>ORA-01400</code>', right: 'Cannot insert NULL (columna NOT NULL)' },
      { id: 'e2', left: '<code>ORA-02291</code>', right: 'Parent key not found (FK violada al insertar)' },
      { id: 'e3', left: '<code>ORA-02292</code>', right: 'Child record found (FK violada al borrar padre)' },
      { id: 'e4', left: '<code>ORA-00001</code>', right: 'Unique constraint violated (PK duplicada)' },
      { id: 'e5', left: '<code>ORA-01722</code>', right: 'Invalid number (tipo de dato incorrecto)' },
    ]
  },
];
