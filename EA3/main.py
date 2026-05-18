
numero_ingresado = int(input("numero : "))

def elTripleDeUnNumero(numero_ingresado):
    resultado = numero_ingresado * 3
    print(f"El triple de {numero_ingresado} es {resultado}")
    return resultado


respuesta = elTripleDeUnNumero(numero_ingresado)

print(respuesta)