libros = []

#"titulo" Título del libro No vacío ni solo espacios en blanco
def validar_titulo_libro():
    while True:
            titulo_ingresado_usuario = input("ingresa el titulo del libro : \n").strip()
            if " " in titulo_ingresado_usuario or len(titulo_ingresado_usuario) <= 0:
                print("ingresa el titulo del libro sin espacios ni vacio ")
            else:
                return titulo_ingresado_usuario
                


#"autor" Nombre del autor No vacío ni solo espacios en blanco
def validar_nombre_autor():
     while True:
        nombre_autor_usuario = input("ingresa el nombre del autor :\n").strip()
        if " " in nombre_autor_usuario or len(nombre_autor_usuario) <=0:
           print("ingresa el nombre del autor sin espacios ni vacio ")
        else:
            return nombre_autor_usuario

 

#ejemplares" Cantidad de copias disponibles Entero mayor o igual a cero
def validar_cantidad_ejemplares():
    while True:
            try:
                numero_ejemplares_usuario = int(input("ingresa la cantidad de ejemplares : \n"))
                if numero_ejemplares_usuario >=0 :
                    return numero_ejemplares_usuario
                else:
                    print("ingresa un numero de ejemplares valido")
            except ValueError:
                print("ingresa un numero para los ejemplares")



def agregar_libro_a_la_lista():
    titulo_libro_validado = validar_titulo_libro()
    nombre_autor_validado = validar_nombre_autor()
    numero_ejemplares_validado = validar_cantidad_ejemplares()

    datos_libro = {
        "titulo_libro" : titulo_libro_validado,
        "autor" : nombre_autor_validado,
        "ejemplares": numero_ejemplares_validado
}
    libros.append(datos_libro)

agregar_libro_a_la_lista()
print(libros)

