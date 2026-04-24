libro = {
    "Titulo": "La macarena",
    "Autor": "Don Juan",
    "Año": 1800
}
for claves, valores in libro.items():
    print(claves, valores)
libro["Año"] = 2023
libro["Editorial"] = "El barco de vapor"
for claves, valores in libro.items():
    print(claves, valores)
# coma para indicar que despues de ese viene otra clave : valor
# los diccionarios pueden cotenr otros tipos de datos escrucuturados ademas de datos primitivos