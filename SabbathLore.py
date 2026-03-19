import sys
import time

print("Hola, el día de hoy serás partícipe de una novela gráfica interactiva en la cuál TÚ seras el protagonista.")

nombre_protagonista = input("----¿Con qué nombre quieres que se te llame?---- ")

print("Espléndido, entonces " + nombre_protagonista + " espero que disfrutes de esta novela, recuerda que algunas de tus desiciones (qué seleccionaras por medio de el número de la opción que elijas)tomarán un rol importante en esta historia, así que piensa bien en cada acción que tomes")

comenzar = input("Entonces, ya teniendo esto en cuenta, ¿Estás listo para comenzar? Si/No ") 

if comenzar == "Si":
    print("¡Excelente! Comencemos entonces")
else:
    print("Bueno, no hay problema, tómate tu tiempo, cuando estés listo solo vuelve a ejecutar el programa")
    sys.exit()

print("-Estás en una vieja cabaña alejada de cualquier zona urbana, en medio del bosque de una inmensa montaña, en una noche fría y lluviosa")
time.sleep(2)
print("Esta cabaña es tu hogar, heredada por tu padre luego de su defunción hace 3 años por razones que jamas fueron resueltas. Una media agua anticuada, paredes de madera, una rústica chimenea de piedra la cuál es tu única fuente de luz y calor. Sin embargo esta se está quedando sin leña por lo que se está extinguiendo")
time.sleep(1)
decision_n1 = input("Que harás? | 1. Ir por leña | 2. Dejar que el fuego se extinga e irte a dormir ")

if decision_n1 == "1":
    print("Decides salir a buscar leña a la bodega, la cuál esta a unos metros de la cabaña pero por la llvuia torrencial y los fuertes vientos no puedes ver casi nada")
    decision_n2 = input("Qué harás? | 1. Volver adentro y simplemente irte a dormir| 2. Seguir hasta encontrar la bodega")
    
    if decision_n2 == "1":
        print("Decides simplemente volver adentro ya que no sientes que valga la pena arriesgarte a salir con este clima, pero sientes que algo no está bien.")
    
    if decision_n2 == "2":
        print("Decides seguir adelante, sientes que está noche será larga por lo que no te improta mojarte un poco, así que sigues adelant hasta hallar la bodega, la cuál encuentras y te pones bajo techo inmediatamente")
        aire_tibio = input("Al entrar te quedas un tiempo apreciando la vista de la lluvia viajando casi completamente horizontal por el viento, pero de pronto sientes una corriente de aire más bien tibia pasando por tu cuello. | 1. Ignorarlo | 2. Voltear")
        
        if aire_tibio == "1":
            print("Decides ignorar la corriente que sentiste y no pasa nada, así que solo tomas la leña y vuelves adentro a la cabaña antes de que el clima empeore")
        
        if aire_tibio == "2":
            print("Decides darte vuelta con algo de temor... y solo resulta ser un gato negro salvaje que se refugiaba de la tormenta en tu bodega, lo acaricias y ves como se va y desaparece en la densa y oscura lluvia, procedes a entrar a tu hogar")
            print("Al entrar, cierras la puerta y dejas la leña en el suelo, te quitas la ropa mojada con la que saliste")
if decision_n1 == "2": 
    print("Decides dejar que el fuego se consuma, te quedas observandolo casi hipnotizado hasta que se apaga por completo para luego ir a tu habitación")
print("Ya en tu habitación escuchas algo extraño como raspando tu ventana pero decides ignorarlo pensando que habra sido el viento")
time.sleep(2)
if decision_n1 == "2":
    print("Sin embargo, vuelves  a escuchar la ventana y esta vez como si la estuvieran tocando con un dedo, haciendo un patrón de 3 toques suaves.")
    time.sleep(2)
    print("*Toc* *Toc* *Toc*")

