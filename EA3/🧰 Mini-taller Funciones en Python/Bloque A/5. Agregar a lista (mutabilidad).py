def agregar_a_lista(lista, elemento):
    lista.append(elemento)

mi_lista = ["a", "b"]

agregar_a_lista(mi_lista, "C")

print(mi_lista)

# o con return

def agregar_a_lista_return(lista, elemento):
    return lista + [elemento]

mi_lista_con_return = ["D", "F"]

mi_lista_con_return = agregar_a_lista_return(mi_lista_con_return, "G")

print(mi_lista_con_return)