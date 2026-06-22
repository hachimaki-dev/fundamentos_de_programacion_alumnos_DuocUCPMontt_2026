def intentar_aumentar(numero):
    numero = numero + 10

x = 5

intentar_aumentar(x)

print(x)

# Resultado: 5.
# La variable global x no cambia porque los números (int) son inmutables.
# Dentro de la función se crea una variable local llamada numero,
# que primero recibe el valor 5 y luego se le asigna un nuevo valor 15.
# Ese cambio solo existe dentro de la función (local) y no modifica la variable x. (global)