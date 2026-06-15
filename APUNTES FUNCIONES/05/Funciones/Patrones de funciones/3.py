# LISTA: el cambio SÍ se mantiene afuera
def agregar_fruta(lista_frutas):
    lista_frutas.append("manzana")
    # no hay return, y no hace falta

mis_frutas = ["pera", "uva"]
agregar_fruta(mis_frutas)
print(mis_frutas)  # ['pera', 'uva', 'manzana'] -> ¡se modificó!

# NÚMERO: el cambio NO se mantiene afuera
def intentar_cambiar(numero):
    numero = numero + 100
    # esto NO afecta la variable original

x = 5
intentar_cambiar(x)
print(x)  # sigue siendo 5