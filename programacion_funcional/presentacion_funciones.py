def saludar(nombre):
     print(f"que pasa {nombre}")
    

print(saludar("juan"))
print(saludar("maria"))
print(saludar("nanana"))
print(saludar("jejeje"))


#las funciones siempre tienen return , si no se les asigna , vale por defecto "none" y si imprimes algo  con print sale la imprecion pero el return sigue valiendo "none"

def datos_personaje(nombre , edad , poder):
    nombre = "ciborg"
    return f"tu heroe se llama : {nombre} , edad : {edad} , poder : {poder}"

print(datos_personaje("juaco","ni idea", "pelear"))