""" Ejercicio 28: Búsqueda del Sospechoso (Cámaras)
La policía está buscando un auto robado en la lista de cámaras del peaje.

Datos Iniciales: Las patentes que pasaron son: `['XY11', 'ZZ99', 'AB12', 'XX00']`. La policía busca la patente 'AB12'.

Reglas de Negocio: El programa revisa patente por patente y va avisando en pantalla qué patente está mirando ('Buscando en XY11...').
 Si encuentra la patente robada, dice 'Sospechoso encontrado' y DEJA DE BUSCAR (no tiene sentido mirar los autos que pasaron después).

Restricciones: Usa un ciclo `for`. Apenas encuentres el auto, usa `break` para apagar la búsqueda. Imprime todo paso a paso."""

patentes_paso = ['XY11', 'ZZ99', 'AB12', 'XX00']

policia_busca_policia = "AB12"

for patente in patentes_paso:
    print(f"buscando en {patente}")
    if patente == policia_busca_policia:
        print("sospechoso encontrado")
        break
