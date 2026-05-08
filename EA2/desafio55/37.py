'''Ejercicio 37: Multiplicador de Exp In-Place (RPG)
Aplica un evento de 'Doble Experiencia' a los puntajes de un jugador.

Datos Iniciales: El jugador ganó esta experiencia en sus partidas: `[100, 200, 300]`.

Reglas de Negocio: Es fin de semana de doble EXP. Tienes que tomar la lista original y multiplicar cada uno de sus números por 2, sobreescribiendo los valores antiguos.

Restricciones: Para cambiar un número directamente dentro de una lista, necesitas saber su 'dirección' (su índice). Usa un `for` combinado con `range(len(lista))` para recorrer las posiciones. Sobreescribe multiplicando por 2 e imprime la lista modificada.'''

xp = [100, 200, 300]
fin_semana = True

for experiencia in range(len(xp)):
    if fin_semana:
        xp[experiencia] *= 2

print(xp)