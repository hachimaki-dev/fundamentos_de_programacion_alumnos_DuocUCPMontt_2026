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
        especie=input('Por favor ingrese la especie del bicho a registrar: \n')
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
    #tamaño
    tamano = validacionTamano()
    #nivel de peligrosidad
    peligrosidad = validacionPeligrosidad()
    
    print ('Bicho registrado')

    lista.append({"especie": especie, "tamaño":tamano, "peligrosidad": peligrosidad, "peligroso" : False})       
#OPCION 2 (opcion 3 utiliza esta misma funcion)
def buscarBicho(texto,lista):
    buscar= input(texto)
    bichoEncontrado= False
    for i in lista:
        if buscar in i['especie']:
            print ('Bicho encontrado')
            bichoEncontrado= True
            index= lista.index(i)
    if bichoEncontrado:
        return index
    else:
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
def main():
    lista_bichos=[]
    while True:
        menuOpciones()
        opcion=selecionOpcion("Seleccione una opción: ")
        if opcion == 1:
            agregarBicho(lista_bichos)
        if opcion == 2:
            buscar=buscarBicho("Ingrese la especie a buscar \n",lista_bichos)
            if buscar != -1:
                mostrarEspecie(lista_bichos,buscar)
            else:
                print ('Bicho no existe')    
        if opcion == 3:
            eliminacion=buscarBicho("Ingrese la especie a eliminar \n",lista_bichos)
            if eliminacion == -1:
                print ('Bicho no existe')
            else:
                lista_bichos.remove(eliminacion)
        if opcion == 4:
            actualizarEstados(lista_bichos)
            print('Datos actualizados')
        if opcion ==5:
            actualizarEstados(lista_bichos)
            listaBonita(lista_bichos)         

            
        if opcion == 6:
            break


main()

    