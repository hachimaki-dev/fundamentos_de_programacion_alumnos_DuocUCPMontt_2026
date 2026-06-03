pacientes = [
    {"nombre" : "benjamin" , "edad" : 20 },
    {"nombre" : "franco" , "edad" : 22},
    {"nombre" : "matias" , "edad" : 21}
]

encontrado = False

while True:
    busqueda_usuario = input("Ingrese el nombre que esta buscando :   ").strip().lower()
    if len(busqueda_usuario) <= 0 :
        print("Ingrese un nombre , no puede dejar el espacio vacio") 
    else:
        break

for i in pacientes:

    if i["nombre"] == busqueda_usuario :
        print(f"Paciente encontrado : Nombre : {i["nombre"]} | Edad : {i["edad"]}")
        encontrado = True
    

if not encontrado:
    print("Paciente no Encontrado ")
