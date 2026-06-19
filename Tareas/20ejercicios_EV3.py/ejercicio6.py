while True:
    patente = input('Ingresa la patente de tu auto: ').strip().upper()
    sin_espacios = patente.replace(' ', '')
    if len(patente) == 6 and len(patente) == len(sin_espacios):
        break
    else:
        print('Patente invalido, Ingresa exactamente 6 caracters sin espacio')
print('La patente de tu autoes es: ', patente)        
