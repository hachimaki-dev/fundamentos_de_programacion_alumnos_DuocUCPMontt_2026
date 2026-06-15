# LISTA: el cambio SÍ se mantiene afuera
def agregar_fruta(lista_frutas):
    lista_frutas.append("manzana")  # sin return
mis_frutas = ["pera", "uva"]
agregar_fruta(mis_frutas)
print(mis_frutas)  # ['pera', 'uva', 'manzana'] ✅

# NÚMERO: el cambio NO se mantiene afuera
def intentar_cambiar(numero):
    numero = numero + 100
x = 5
intentar_cambiar(x)
print(x)  # sigue siendo 5 ❌