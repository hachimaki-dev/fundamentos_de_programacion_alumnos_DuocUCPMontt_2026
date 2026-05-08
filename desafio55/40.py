#Ejercicio 40: Ges#tión de Inventario (Minecraft#)
#El Mini-Boss: Haz# que el jugador no pueda recoger más cosa#s si su mochila está llena.##

#Datos Iniciales: Tu mochila ya tiene `['mapa', 'espada']`. Solo puedes llevar 4 cosas máximo. 
# En el piso encontraste `['#madera', 'piedra', 'oro']`.##

#Reglas de Negocio: El juego in#tenta recoger las cosas del piso una por una. 
# Pero si en algún momento la mochila llega a 4 objetos, se llena, salta la alerta 'Lleno' 
# y no puedes seguir re#cogiendo NADA MÁS del piso.#

#Restricciones: Recorre las cosas del piso con un `for`. Agrégalas a tu mochila. 
# Justo después de agregar, revisa si el largo (`len()`) de tu mochila es igual a 4. Si es así, 
# imprime 'Lleno' y corta el ciclo con `br#eak`. Al final, imp#rime cómo quedó tu mochila.

#Resultado esperado# en consola#:
#Lleno\n['mapa', '#espada', 'madera', 'piedra']

mochila = ['mapa', 'espada']
piso = ['madera', 'piedra', 'oro']

for objeto in piso:
    mochila.append(objeto)
    if len(mochila) == 4:
        print("lleno") 
        break 
print(mochila)      
    
        
        
        
    
    