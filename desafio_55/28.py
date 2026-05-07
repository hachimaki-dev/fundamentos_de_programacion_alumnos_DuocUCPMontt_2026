#La policía está buscando un auto robado en la lista de cámaras del peaje.

#Datos Iniciales: Las patentes que pasaron son: `['XY11', 'ZZ99', 'AB12', 'XX00']`. La policía busca la patente 'AB12'.

#Reglas de Negocio: El programa revisa patente por patente y va avisando en pantalla qué patente está mirando ('Buscando en XY11...'). Si encuentra la patente robada, dice 'Sospechoso encontrado' y DEJA DE BUSCAR (no tiene sentido mirar los autos que pasaron después).

#Restricciones: Usa un ciclo `for`. Apenas encuentres el auto, usa `break` para apagar la búsqueda. Imprime todo paso a paso.
patentes = ["XY11", "ZZ99", "AB12", "XX00"] 
patente_buscada = "AB12"
for i in patentes:
    print(f"buscando en {i}")
    if i in patente_buscada:
        print(f"sospechoso encontrado {i}")
        break