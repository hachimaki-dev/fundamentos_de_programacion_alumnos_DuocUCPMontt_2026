#El Mini-Boss: Haz un script que sepa qué hacer si se cae el servidor de tu página web.

web = [200, 404, 500, 200, 500]
reintento = 1

#Reglas de Negocio: Un 200 es bueno (imprime 'Ok'). Un 404 no es grave (imprime 'No encontrado'). Pero un 500 significa que el servidor falló. Si sale un 500, gastas tu 'reintento' salvavidas (réstale 1) e imprime 'Reintentando'. PERO si te sale otro 500 y ya te quedaste sin reintentos, el sistema muere: imprime 'Servidor Caído' y cierra todo.

#Restricciones: Usa `for`. Usa un `if` para restarle a tus reintentos. Si el reintento es menor a 0, usa `break` para parar todo. Imprime cada mensaje en orden.

for i in web:
    if i == 200:
        print("OK")
    elif i == 404:
        print("No encontrado")
    elif i == 500:
        reintento -= 1
        if reintento >= 0:
            print("Reintentando")
        else:
            print("Servidor Caído")
            break