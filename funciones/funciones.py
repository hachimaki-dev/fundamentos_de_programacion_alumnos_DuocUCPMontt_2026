# Sin retor

# def saludrCompañero():
#     print(('Hola'))

# def saludarCompañeroParametro(nombre_del_compi):
#     print(f'Hoal {nombre_del_compi}')
    


# while True:
#     contador = 0
#     saludarCompañeroParametro(f'Pepito {contador}')
#     contador += 1


#Con retorno 
contador = 0
def saludarCompi():
    return 'Hola'

def saludarCompiParametro(nombre_del_compi):
    return nombre_del_compi

guardando_respuesta = saludarCompi('pepe')
print(f'Esta es la respuesta {guardando_respuesta}')