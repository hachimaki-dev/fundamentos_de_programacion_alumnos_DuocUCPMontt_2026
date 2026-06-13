def aplicar_descuento(lista_precios):
    for i in range(len(lista_precios)):
        lista_precios[i] = lista_precios[i] * 0.9  # 10% de descuento

# Con diccionarios: acceder y modificar un campo específico
def marcar_todos_revisados(lista_productos):
    for producto in lista_productos:
        producto["revisado"] = True