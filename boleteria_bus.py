paradas = {
    "Parada 1" : {
        "Lugar" : "Frutillar",
        "Precio" : 5000
    },
    "Parada 2" : {
        "Lugar" : "Puerto Varas",
        "Precio" : 3000
    },
    "Parada 3" : {
        "Lugar" : "Osorno",
        "Precio" : 7000
    }
}


print("== Bienvenido a la boleteria Juan Buses ==")
print("Porfavor ingrese su destino")

i = 0

for key, obj in paradas.items():
    print(key)
    for info in paradas[key]:
        print(info, ":", paradas[key][info])

destino_seleccionado = input("[]: ")
