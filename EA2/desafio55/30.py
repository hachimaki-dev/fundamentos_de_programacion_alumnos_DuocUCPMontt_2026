'''Ejercicio 30: Procesamiento Resiliente (AWS)
El Mini-Boss: Haz un script que sepa qué hacer si se cae el servidor de tu página web.

Datos Iniciales: Tienes una lista de códigos de respuesta web: `[200, 404, 500, 200, 500]`. Tienes solo 1 'reintento' salvavidas guardado en una variable.

Reglas de Negocio: Un 200 es bueno (imprime 'Ok'). Un 404 no es grave (imprime 'No encontrado'). Pero un 500 significa que el servidor falló. Si sale un 500, gastas tu 'reintento' salvavidas (réstale 1) e imprime 'Reintentando'. PERO si te sale otro 500 y ya te quedaste sin reintentos, el sistema muere: imprime 'Servidor Caído' y cierra todo.

Restricciones: Usa `for`. Usa un `if` para restarle a tus reintentos. Si el reintento es menor a 0, usa `break` para parar todo. Imprime cada mensaje en orden.'''

respuesta_web = [200, 404, 500, 200, 500]
reintento = 1

for respuesta in respuesta_web:
    if respuesta == 200:
        print("Ok")
    elif respuesta == 500:
        if reintento == 1:
            reintento -= 1
            print("Reintentando")
        else:
            print("Servidor caído")
            break
    else:
        print("NO encontrado")