-- ═══════════════════════════════════════════════════════════════
--  🗄️ EA2 — Clase 1: Script de Creación de Base de Datos
--  ─────────────────────────────────────────────────────────────
--  Mini-DB de ejemplo para practicar INSERT, UPDATE, DELETE
--  Compatible con Oracle SQL (SQL*Plus / SQL Developer / LiveSQL)
--
--  Ejecutar en orden: 1) DROP, 2) CREATE, 3) INSERT
-- ═══════════════════════════════════════════════════════════════

-- ── Limpieza (ejecutar solo si las tablas ya existen) ──
-- DROP TABLE NOTAS;
-- DROP TABLE ALUMNOS;

-- ═══ 1. CREAR TABLAS ═══

CREATE TABLE ALUMNOS (
    rut         NUMBER(10)      PRIMARY KEY,
    nombre      VARCHAR2(100)   NOT NULL,
    carrera     VARCHAR2(50)    NOT NULL
);

CREATE TABLE NOTAS (
    id_nota     NUMBER(10)      PRIMARY KEY,
    rut_alumno  NUMBER(10)      NOT NULL,
    asignatura  VARCHAR2(80)    NOT NULL,
    nota        NUMBER(3,1)     NOT NULL,
    CONSTRAINT fk_notas_alumnos 
        FOREIGN KEY (rut_alumno) REFERENCES ALUMNOS(rut)
);

-- ═══ 2. POBLAR TABLA ALUMNOS ═══

INSERT INTO ALUMNOS (rut, nombre, carrera) VALUES (20100001, 'Camila Rojas', 'Informática');
INSERT INTO ALUMNOS (rut, nombre, carrera) VALUES (20100002, 'Matías Soto', 'Informática');
INSERT INTO ALUMNOS (rut, nombre, carrera) VALUES (20100003, 'Valentina Díaz', 'Diseño');
INSERT INTO ALUMNOS (rut, nombre, carrera) VALUES (20100004, 'Benjamín Torres', 'Informática');
INSERT INTO ALUMNOS (rut, nombre, carrera) VALUES (20100005, 'Isidora Muñoz', 'Contabilidad');

-- ═══ 3. POBLAR TABLA NOTAS ═══

INSERT INTO NOTAS (id_nota, rut_alumno, asignatura, nota) VALUES (1, 20100001, 'Base de Datos', 6.2);
INSERT INTO NOTAS (id_nota, rut_alumno, asignatura, nota) VALUES (2, 20100001, 'Programación', 5.8);
INSERT INTO NOTAS (id_nota, rut_alumno, asignatura, nota) VALUES (3, 20100002, 'Base de Datos', 4.5);
INSERT INTO NOTAS (id_nota, rut_alumno, asignatura, nota) VALUES (4, 20100002, 'Programación', 3.9);
INSERT INTO NOTAS (id_nota, rut_alumno, asignatura, nota) VALUES (5, 20100003, 'Base de Datos', 5.0);
INSERT INTO NOTAS (id_nota, rut_alumno, asignatura, nota) VALUES (6, 20100003, 'Diseño Web', 6.8);
INSERT INTO NOTAS (id_nota, rut_alumno, asignatura, nota) VALUES (7, 20100004, 'Base de Datos', 3.2);
INSERT INTO NOTAS (id_nota, rut_alumno, asignatura, nota) VALUES (8, 20100004, 'Programación', 4.1);
INSERT INTO NOTAS (id_nota, rut_alumno, asignatura, nota) VALUES (9, 20100005, 'Contabilidad I', 5.5);
INSERT INTO NOTAS (id_nota, rut_alumno, asignatura, nota) VALUES (10, 20100005, 'Base de Datos', 6.0);

COMMIT;

-- ═══ VERIFICACIÓN ═══
-- SELECT * FROM ALUMNOS;
-- SELECT * FROM NOTAS;
-- SELECT a.nombre, n.asignatura, n.nota FROM ALUMNOS a JOIN NOTAS n ON a.rut = n.rut_alumno ORDER BY a.nombre;
