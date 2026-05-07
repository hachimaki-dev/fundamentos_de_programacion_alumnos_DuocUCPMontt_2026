Datos_Sucios = ["Juan", None, "","Ana"," "]
lista_nombre = []

for i in Datos_Sucios :

    if i is not None and i.strip() != "" :
        lista_nombre.append(i)

        
print(lista_nombre)

        

