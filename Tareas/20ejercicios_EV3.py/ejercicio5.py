while True:
    codigo = input('Igresa el codigo: ')
    if len(codigo) >= 6 and ' ' not in codigo:
        break
    else:
        print('codigo invalido debeter almenos 6 caracter')
print('Producto registrado con el codigo: ', codigo)        