#sin retorno

# def saludarCompi():
#     print("hola")

#con parametros
# def saludarCompiParametro(nombre_del_compi):
#     print(f"hola {nombre_del_compi}")

# while True:
#     contador = 0
#     saludarCompiParametro("pepito {contador}")
#     contador += 1


#con retorno
contador = 0
def saludarCompi():
    return "hola"

def saludarCompiParametro(nombre_del_compi):
    return nombre_del_compi

guardando_respuesta = saludarCompiParametro("gonza")

print(f"esta es la respuesta: {guardando_respuesta}")

