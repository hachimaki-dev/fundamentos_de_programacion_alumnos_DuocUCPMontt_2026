#Aplica un evento de 'Doble Experiencia' a los puntajes de un jugador.
#Datos Iniciales: El jugador ganó esta experiencia en sus partidas: `[100, 200, 300]`.
#Reglas de Negocio: Es fin de semana de doble EXP. Tienes que tomar la lista original y multiplicar cada uno de sus números por 2, sobreescribiendo los valores antiguos.
#Restricciones: Para cambiar un número directamente dentro de una lista, necesitas saber su 'dirección' (su índice). Usa un `for` combinado con `range(len(lista))` para recorrer las posiciones. Sobreescribe multiplicando por 2 e imprime la lista modificada.
experiencia = [100, 200, 300] 
for experiencia_doble in range(len(experiencia)):
    experiencia[experiencia_doble] = experiencia[experiencia_doble] *2
print(experiencia)