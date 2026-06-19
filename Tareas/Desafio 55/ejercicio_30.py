# Procesamiento Resiliente (AWS)
# El Mini-Boss: Haz un script que sepa qué hacer si se cae el servidor de tu página web.

web = [200, 404, 500, 200, 500]
reitento = 1

for servidor in web:
    
    if servidor == 200:
        print('Ok')

    elif servidor == 404:
        print('No encontrado')
    elif servidor == 500: 
        
        reitento -= 1
        
        if reitento < 0:
            print('Servidor Caído') 
            break 
        print('Reitentando')             