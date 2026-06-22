def menuOpciones():
    print("""
========== MENÚ PRINCIPAL ==========
1. Agregar bicho
2. Buscar bicho
3. Eliminar bicho
4. Actualizar estados
5. Mostrar bichos
6. Salir
=====================================
          """)

def selecionOpcion(texto=''):
    while True:
        try:
            opcion = int(input(texto))
            if opcion in [1,2,3,4,5,6]:
                return opcion
            else:
                print('Por favor ingrese una opcion del menu')
        except ValueError:
            print('Por favor ingrese un dato valido')

#OPCION 1
def validacionEspecie():
    while True:
        especie=input('Por favor ingrese la especie del bicho a registrar: \n').capitalize()
        valido=True
        if len(especie) == 0:
            print('La especie no puede estar vacia')
            valido = False
        if especie.isspace():
            print('La especie no puede contener solo espacios')
            valido = False
        if valido:
            return especie

def validacionTamano():
    while True:
        try:
            tamano=int(input('Ingrese el tamaño en cm del bicho a registrar: \n'))
            if tamano > 0:
                return tamano
            print('El tamaño no puede ser menor a 0')
        except ValueError:
            print('Ingrese un dato valido') 
def validacionPeligrosidad():
     while True:            
        try:
            peligrosidad=float(input('Ingrese el nivel de peligrosidad del bicho a registrar: (Utilize numeros entre 1.0 a 10.0) \n'))
            if 1.0 <= peligrosidad <= 10.0:
                return peligrosidad
            print('Por favor ingrese un numero dentro del rango')
        except ValueError:
            print('Ingrese un dato valido')
def agregarBicho(lista):
    #especie
    especie = validacionEspecie()
    key= especie.upper() #mismo nombre pero en mayuscula para facilitar la funcion busqueda
    
    #tamaño
    tamano = validacionTamano()
    #nivel de peligrosidad
    peligrosidad = validacionPeligrosidad()
    
    print ('Bicho registrado')

    lista.append({"key": key, "especie": especie, "tamaño":tamano, "peligrosidad": peligrosidad, "peligroso" : False})       
#OPCION 2 (opcion 3 utiliza esta misma funcion)
def buscarBicho(texto,lista):
    buscar= input(texto).upper()
    index=[]
    flag=False
    for i in lista:
        if buscar in i['key']:
            index.append(lista.index(i))
            flag=True
    if flag:
        if len(index) > 1:        
            print('Multiples especies encontradas')
            return index
        if len(index) == 1:
            return index[0]    
    return -1
def mostrarEspecie(lista,index):
    i = lista[index]
    print('')
    print (f'Especie: {i['especie']}')
    print (f'Tamaño: {i['tamaño']}')
    print (f'Nivel de peligrosidad: {i['peligrosidad']}')
    print (f'Posicion en la lista de bichos: {index}')            
#OPCION 4
def actualizarEstados(lista):
    for i in lista:
        if i["peligrosidad"] >= 7.0:
            i.update({"peligroso": True})
    print('Datos actualizados')        

#opcion 5
def listaBonita(lista):
    print('=== LISTA DE BICHOS ===')
    for i in lista:
        
        print (f'Especie: {i['especie']}')
        print (f'Tamaño: {i['tamaño']}')
        print (f'Nivel de peligrosidad: {i['peligrosidad']}')
        if i['peligroso']:
            print ('Estado: PELIGROSO')
        if not i['peligroso']:
            print ('Estado: NO PELIGROSO')
        print('********************************************') 
#adicionales, añadidas el miercoles aka dejar la main lo mas corta posible
def resultadoBusqueda(lista):
    dato=buscarBicho("Ingrese la especie a buscar \n",lista)
    if type(dato) is list:
        for i in dato:
            bicho=i
            mostrarEspecie(lista,bicho)
        print('Multiples bichos encontrados')    
    elif type(dato) is not list:

        if dato != -1:
            print('Bicho encontrado')
            mostrarEspecie(lista,dato)
   
        else:
            print ('Bicho no existe')       
def numeroEntero(texto):
    while True:
        try:
            numero = int(input(texto))
            if numero >= 0:
                return numero
                
            print('Por favor ingrese un entero positivo')
        except ValueError:
            print ('Por favor ingrese un dato valido')
def eliminacionBicho(lista):
    dato=buscarBicho("Ingrese la especie a eliminar \n",lista)
    if type(dato) is list:
        print ('Multiples especies encontradas')
        for i in dato:
            mostrarEspecie(lista,i)
        eliminar=numeroEntero('Seleccione al bicho a eliminar (Ingrese su posicion en la lista): ')
        
        if eliminar not in dato:
            print('Ese bicho no esta en las opciones de la busqueda.')
        elif eliminar in dato:
            lista.pop(eliminar)
            print('Bicho Eliminado')         
    else:
        if dato == -1:
            print ('Bicho no existe')
        else:
            lista.pop(dato)
        

def main():
    lista_bichos=[]
    while True:
        menuOpciones()
        opcion=selecionOpcion("Seleccione una opción: ")
        if opcion == 1:
            agregarBicho(lista_bichos)
        if opcion == 2:
            resultadoBusqueda(lista_bichos)    
        if opcion == 3:
            eliminacionBicho(lista_bichos)
        if opcion == 4:
            actualizarEstados(lista_bichos)   
        if opcion ==5:
            actualizarEstados(lista_bichos)
            listaBonita(lista_bichos)             
        if opcion == 6:
            break
        #debug
        #print(lista_bichos)


main()

    