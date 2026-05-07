#Ejercicio 40: Gestión de Inventario (Minecraft)
#El Mini-Boss: Haz que el jugador no pueda recoger más cosas si su mochila está llena.

#Datos Iniciales: Tu mochila ya tiene `['mapa', 'espada']`. Solo puedes llevar 4 cosas máximo. En el piso encontraste `['madera', 'piedra', 'oro']`.

#Reglas de Negocio: El juego intenta recoger las cosas del piso una por una. Pero si en algún momento la mochila llega a 4 objetos, se llena, salta la alerta 'Lleno' y no puedes seguir recogiendo NADA MÁS del piso.

#Restricciones: Recorre las cosas del piso con un `for`. Agrégalas a tu mochila. Justo después de agregar, revisa si el largo (`len()`) de tu mochila es igual a 4. Si es así, imprime 'Lleno' y corta el ciclo con `break`. Al final, imprime cómo quedó tu mochila.

mochila = ['mapa', 'espada']
piso = ['madera', 'piedra', 'oro']
maximo_objetos = 4

for material in piso:
    mochila.append(material)
    
    if len(mochila) == 4:
        print("Lleno")
        break

print(mochila)
