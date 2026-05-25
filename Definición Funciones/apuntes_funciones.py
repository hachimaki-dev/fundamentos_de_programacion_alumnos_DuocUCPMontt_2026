# PROGRAMACION FUNCIONAL
# ARGUMENTO -> PARAMETROS -> SALIDA
# snakecase, UPPER_SNAKE_CASE, camelCase
# codigo boilerplate
# SCOPE -> GLOBAL
#       -> LOCAL -> variable local solo esta definida dentro de la funcion 

def el_triple_de_un_numero(numero_ingresado): # () -> PARAMETRO
    resultado = numero_ingresado * 3
    return resultado # la variable 'resultado' es local
    # return numero_ingresado * 3

# numero_ingresado = int(input())
numero_ingresado = 10
el_triple_de_un_numero(numero_ingresado) # () -> ARGUMENTO