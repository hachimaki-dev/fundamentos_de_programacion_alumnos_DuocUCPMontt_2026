print("**********EL PARADIGMA: AVENTURA EN LAS CATACUMBAS**********")

nombre_jugador = input("\nAntes de comenzar la travesia, cual es tu nombre? ")

print(f"\nBienvenido, {nombre_jugador}. La historia esta por comenzar...")

print("\nEntre las catacumbas se encuentra un misterio que puede decifrar la clave del origen y sus capas de la realidad, quien lo encuentre estara destinado a revelar la verdad, pero quien se atrevera a ingresar al mismismo infierno y poder salir vivo?")

print(f"\nEn esos momentos, el viajero {nombre_jugador} ingresa al mercado de recompensas, por lo cual le dan un par de monedas, pero, el ya no se conforma con hazañas pequeñas, el quiere ser recordado por algo mas respetable, y es en ese entonces que se fija en el listado de las misiones.")

print(f"\nEs en ese entonces que te acercas a la barra del cantinero Charles, quien tiene una aspecto despojado y con cicatrices en la cara, ademas de una falta de un ojo. Mientras el limpia un vaso, {nombre_jugador} decide entablar una conversacion con el para saber mas sobre cierta mision en particular.")

print("\n====¿Como te acercas a el?====")

print("A. Golpeas la barra con una moneda para llamar su atencion")
print("B. Te quedas callado y esperas a que te diga algo")
print("C. Susurras la palabra **PARADIGMA**")

accion = ""

while accion not in["A", "B", "C"]:
    entrada = input("\nTu eleccion (A, B, C): ").strip().upper()

    if entrada in ["A", "B", "C"]:
        accion = entrada

    else:
        print("Opcion no valida. Porfavor elige A, B o C.") 

if accion == "A":
    print("\nNo se inmuta. Continua limpiando su vaso, y dice lo siguiente")
    print(f"\nEl dinero no compra la verdad en mi cantina {nombre_jugador}, Solo hace que tu muerte sea mas rapida")
    print("\nPero que es lo que me intentas decir, o solo quieres llamar la atencion eh?")

    mencion_mision = False
    while mencion_mision == False:
        pregunta = input("\nLe mencionas sobre la mision especial **PARADIGMA**? (si/no) ")

        if pregunta == "si":
            print(f"\nNo creo que quieras saber sobre eso {nombre_jugador}")
            mencion_mision = True

        elif pregunta == "no":
            print("\nCharles te ignora y sientes el silencio absoluto. Debes decidirte con firmeza!!")

if accion == "B":
    print("\nPasa un rato y Charles decide hablar")
    print("\nTe noto un poco callado, si vas a pedir algo hazlo ahora o largate de aqui")

    charles_habla = False

    while charles_habla == False:
        pregunta = input("\nDecides mencionarle sobre la mision **PARADIGMA**? (si/no) ")

        if pregunta == "si":
            print(f"\nNo esperaba que tuvieras la valentia de decir semejante cosa")
            charles_habla = True

        elif pregunta =="no":
            print(f"\nCharles te mira y dice lo siguiente: Porfavor {nombre_jugador}, se que tienes algo que decirme!!")

if accion == "C":
    print("\nCharles se queda quieto y deja el vaso en la mesa, se dirige hacia ti con lo siguiente:")
print("\nAcaso no sabes que los viajeros que han querido tomar ese camino terminan sus huesos como decoracion de mi cantina?")
print(f"\nJoven {nombre_jugador}, no creo que quiera tomar el riesgo, pues es muy improbable que no salga con vida de esas catacumbas")
print("\nCharles exhala un suspiro que suena como el viento entre tumbas.")
print("\nSi buscas **PARADIGMA**, buscas tu propia tumba. Pero veo que tu voluntad es tan terca como tu muerte.")
print(f"\nEscucha bien {nombre_jugador}, porque no lo diré dos veces...")

print("\nCharles saca de su bolsillo una llave oxidada")
print("\nPara entrar en a las catacumbas, debes bajar por la trampilla detras de la cueva ubicada al oeste de la ciudadela **Mortem**")
print("\nAlli abajo, el oxigeno es reducido y muy sofocante, asi que ni rezando dios te sacara de esa posilga. Veras varias criaturas que los mas probable sean efecto de tu imaginacion o no, nadie lo sabe con certeza.")
print("\nDicen que las catacumbas no te mata por lo que haya abajo, sino por tu propia mente, asi que no te dejes engañar joven viajero, mucha suerte")

descender_oscuridad = False

while descender_oscuridad == False:
    confirmacion = input("\n¿Estas listo para descender a la oscuridad? (si/no): ")

    if confirmacion == "no":
        print("\nCharles suelta carcajadas y dice lo siguiente:")
        print(f"\nVamos!! {nombre_jugador}, ven a beber hasta olvidarte de quien eres, o acaso si tienes el valor de bajar al mismisimo infierno?")

    if confirmacion == "si":
        print("\nLlegas a la cueva, abres la trampillas y bajas por las escaleras de mano")
        descender_oscuridad = True

        print("\nAl llegar abajo notas el silencio absoluto y sientes como la oscuridad se apodera de las paredes, hasta incluso presientes que el suelo algo te susurra. Lo ignoras y avanzas con antorcha en mano entre los pasillos estrechos, de repente escuchas crujidos de huesos provenientes de mas adelante, decides avanzar y ves en el fondo del pasillo una figura que se desvanecio rapidamente, al parecer llevaba una capa de color rojo")

        print("\nAl seguir avanzando y llegando al final del pasillo, se ve como el lugar se amplia a una escala gigantesca, entre columnas se logra apreciar una figura grande sentada en una silla de madera, pero mientras se da vuelta, se llega a ver una cara palida, con un aspecto de semejanza a un humano, pero que completamente no parece humano, al ver esto te genera nerviosismo y notas como rapidamente se te acelera el corazon a tal punto que empiezas a sentir cada latido como tu ultimo suspiro de vida")

        print("\nNotas que esta figura se levanta de la silla, y rapidamente se acerca hacia ti")

        print("\n¿Que haces?")
        print("1. Cierras los ojos y rezas a que no sea real")
        print("2. Intentas encontrar una salida para poder escapar de tal criatura")

        decision_final = input("\nTu eleccion (1 o 2): ")

        if decision_final == "1":
            print("\nDecides cerrar los ojos y sientes como esta criatura esta a centimentros de ti al frente tuyo, la respiracion acelerada tuya golpea la respiracion lenta de este espectro, quedas paralizado y escuchas como susurra algo en un lenguaje inentendible, se queda callado brevemente para lo cual el lentamente presiona de manera bruzca tu abdomen con sus manos, hasta que decides abrir los ojos y ves como te arranca tus intestinos y empieza a olerlos y a respirar de forma acelerada mirandote a los ojos, de tal manera de saborear el miedo que sentias antes de yacer bajo sus manos.")

            print("\n!!!!!!!!!!!!!!!BAD ENDING!!!!!!!!!!!!!!!!!")

        if decision_final == "2":
            print("\nDecides uir, al seguir corriendo y al entrar en una especie de laberinto de pasillos, te das cuenta de un patron que no te esperabas, las ubicaciones de la catacumba completa parece repetirse, como de un limbo se tratase, pero sin rastro alguno de la escalera de mano del por cual decendiste, al darte cuenta de esto en particular generas una interseccion entre el pasadiso ya recorrido y ves que hay otro camino, te escabulles por ahi y sientes como paso rapidamente esa figura al lado tuyo, decides apagar la antorcha y nisiquiera mover un solo musculo, y a los minutos despues notas silencio absoluto nuevamente")

            print("\nEstando totalmente a oscuras notas un reflejo de un vidrio de una seccion que estaba abierta, vas arrastrandote por el suelo sin hacer tanto ruido para llegar al resplandor de ese vidrio. Notas que a lo lejos de ese mismo pasillo se encuentra una zona llena de espejos mal posicionados, decides entrar y al estar rodeado de estos espejos te encuentras una hoja en una mesa que estaba puesta en ese lugar con varios gereoglificos y figuras satanicas. \nAl examinar la nota ves el siguiente mensaje: ***Yacera el valiente que enfrente a su cordura, pero prosperara el que ahogue sus pensamientos en su miedo***. Al principio no entiendes bien el mensaje, ya que no cobra mucho sentido en el momento, pero recapitulando y recordando que todo lo aprendido fue al revez de la logica misma, te das cuenta que nunca se trato de una verdad abosoluta que resolveria la duda del origen, sino la mentira que condujeria hacia aquella")

            print(f"\nAl notar que se trataba de un acertijo, intersectas todos los espejos de tal manera que se lo unico que refleje sea hacia ti, pero te ves en el espejo y notas que tienes un aspecto similir a la figura que te perseguia, al no creer lo que veias, cierras los ojos y gritas de forma deselantadora. \nA los segundos, sin todavia abrir los ojos, escuchas como alguien se rie, abres los ojos y apareces recostado mirando hacia arriba y te das percatas que es el cantinero Charles riendose, le cuentas lo que sucedio y te dice lo siguiente: \nFelicidades, {nombre_jugador} por ser el primer y unico sobreviviente de aquel macabro lugar, vamos!, te invito algo de tomar :) **FIN**.")

            print("\n=================GOOD ENDING===============")