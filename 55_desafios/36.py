#Junta los usuarios de dos servidores distintos sin crear cuentas duplicadas.

Servidor_1 = ['U1', 'U2']
Servidor_2 = ['U2', 'U3']

#Reglas de Negocio: Tienes que pasar a los usuarios del Servidor 2 al Servidor 1. Pero OJO, el usuario 'U2' ya estaba en el Servidor 1. Si lo copias de nuevo, romperás el sistema. Solo copia a los que sean nuevos.

#Restricciones: Recorre el Servidor 2 con un `for`. Antes de agregar a un usuario, revisa si NO ESTÁ en el Servidor 1 usando la frase clave `not in`. Imprime cómo queda el Servidor 1 al final.

for i in Servidor_2:
    if i not in Servidor_1:
        Servidor_1.append(i)

print(Servidor_1)