def agregar_a_lista(list, elem):
    list.append(elem)       #NO ES NECESARIO QUE DEVUELVA UN RETURN EN ESTE CASO POR QUE LAS LISTAS SON MUTABLES
def agregar_a_lista2(list, elem):
    list += [elem]
mi_lista = ["a", "b"]
mi_segunda_lista = ["a", "b"]
agregar_a_lista(mi_lista, "c")
print(mi_lista)
agregar_a_lista2(mi_segunda_lista, "c")
print(mi_segunda_lista)