Persona1 = {
    "Nombre": "Sebastian Cordero",
    "Edad": "de 19 años,",
    "Ciudad": "vive en Puerto Varas",
    "Ocupacion": "Y es estudiante"
}
print(Persona1["Nombre"], Persona1["Edad"], Persona1["Ciudad"], Persona1["Ocupacion"])

Lista1 = ["Manzana", "Pera", "Naranja", "Plátano", "Uva"]

for i in Lista1:
    print(i)
    if i == "Manzana":
        print("(La manzana tiene 3 colores, roja, verde y amarilla.) ")
    if i == "Pera":
        print("(La pera tiene 2 colores, verde y amarilla.) ")
    if i == "Naranja":
        print("(La naranja tiene 1 color, naranja.) ")
    if i == "Plátano":
        print("(El plátano tiene 1 color, amarillo.) ")
    if i == "Uva":
        print("(La uva tiene 2 colores, morada y verde.) ")
