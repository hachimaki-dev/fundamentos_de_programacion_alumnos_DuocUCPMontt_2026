# Ejercicio 28: Búsqueda del Sospechoso (Cámaras)

print("Sistema de búsqueda policial")

patentes = ['XY11', 'ZZ99', 'AB12', 'XX00']

sospechoso = 'AB12'

for patente in patentes:

    print("Buscando en", patente + "...")

    if patente == sospechoso:
        print("Sospechoso encontrado")
        break