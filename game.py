print("Bienvenido aventurer@, ¿Estarás listo para el camino que te espera?")
nombre = input("¿Cuál es tu nombre? ")
print(f"Oh, con que {nombre}, sin duda un nombre para un heroe.")
print("¿Qué clase de aventurer@ quieres ser?")
Caballero = 1
Mago = 2
Asesino = 3
Arquero = 4
clase = int(input("1) Caballero, 2) Mago, 3) Asesino, 4) Arquero"))
if clase == 1:
    print("Has escogido ser un caballero, tus estadisticas son las siguientes: ")
    print("Vida: 100")
    print("Fuerza: 10")
    print("Defensa : 8")
    print("Agilidad: 5")
    print("Magia: 0")
elif clase == 2:
    print("Has escogido ser un mago, tus estadisticas son las siguientes: ")
    print("Vida: 70")
    print("Fuerza: 3")
    print("Defensa : 4")
    print("Agilidad: 6")
    print("Magia: 10")
elif clase == 3:
    print("Has escogido ser un asesino, tus estadisticas son las siguientes: ")
    print("Vida: 80")
    print("Fuerza: 15")
    print("Defensa : 5")
    print("Agilidad: 10")
    print("Magia: 0")
else:
    print("Has escogido ser un arquero, tus estadisticas son las siguientes: ")
    print("Vida: 90")
    print("Fuerza: 8")
    print("Defensa : 6")
    print("Agilidad: 12")
    print("Magia: 5")

print("Ya decisite que clase de aventurer@ quieres ser, ahora es momento de elegir tu primera ruta, ¿Qué camino quieres tomar?")
Bosque = 1
Montaña = 2
Cueva = 3
Ruta = int(input("1) Bosque, 2) Montaña, 3) Cueva"))
if Ruta == 1:
    print("Has elegido el bosque, puede ser tranquilo durante el día, pero se precavid@ en la noche, el peligro acecha en cada esquina.")
    print("Mientras caminas cerca de los arboles, sientes una presencia detras de ti, te das la vuelta y es un Golem, una criatura bastante resistente.")
    print("¡Rápido!, escoge tu acción: ")
    print("1) Atacar, 2) Defender, 3) Huir")
    Atacar = 1
    Defender = 2
    Huir = 3
    accion = int(input("¿Qué acción quieres realizar? "))
    if accion == 1:
        print("Decidiste atacar al Golem, tu destreza y fuerza son increibles, terminas derrotando al Golem en segundos")
    elif accion == 2:
        print("Decidiste defenderte y esperar a lograr un contraataque")
        print("No te esperabas la rapidez y fuerza del Golem, recibes el golpe pero logras lanzar un contraataque, ganas el combate con dificultad")
    else:
        print("Decidiste huir del Golem, consideras que es una perdida de tiempo enfrentarlo")
    
    print("Sigues tu camino por el bosque y te percatas de un escandalo, te decides acercar.")
    print("De lo poco que puedes ver entre los arbustos, aparentemente es un grupo de siete bandidos y también al parecer una entidad elfica")
    print("Decides intervenir, pero primero piensas como: ")
    print("1) Atacar de frente, 2) Planear un asalto, 3) Probar la negociación")
    Atacar = 1
    Planear = 2
    Negociar = 3
    accion = int(input("¿Qué acción quieres realizar? "))
    if accion == 1:
        print("Decidiste atacar de frente contra los siete bandidos, son habiles pero no más que tú")
        print("Tras una ardua pelea, logras vencer pero con varias heridas y apuñaladas")
        print("La entidad elfica se acerca hacia ti y como muestra de su gratitud te ofrece un poco de su sangre para curarte las heridas")
        print("¿Decides confiar en la elfica?")
        print("1)Decides confiar y aceptar su sanger, 2)Decides desconfiar y negarle su sangre")
        confiar =  1   
        desconfiar = 2
        accion = int(input("¿Decides confiar?"))
        if accion == 1:
            print("Decides confiar y aceptas su sangre, la bebes, sientes como regeneras energias y todo tu cuerpo se siente ligero.")
            print("Agradeces a la entidad elfica por su ayuda, se presenta como Lauma, una druida del bosque.")
        else:
            print("Decides desconfiar y rechazas coordial mente su regalo de gratitud ")
            print("La entidad elfica entiende tu desconfianza, pero te pide que la sigues mientras ella se presenta como Lauma, una druida del bosque.")
    elif accion == 2:
        print("Te ocultas entre las gruesas ramas de los árboles y embistes a dos bandidos que estaban separados del grupo")
        print("Consecutivamente obliteras a otros tres y quedas contra los ultimos dos de frente")
        print("Tus habilidades de combate llegan a ser superiores a manos desnudas y logras derrotar al grupo de bandidos")
        print("La entidad elfica se acerca hacia ti, muestra su gratitud, se presenta como Lauma, una druida del bosque.")
    else:
        print("Decides probar la negociación, pero te obligan a entregar tus pertenencias y todo lo de valor en tu posesión.")
        print("Los bandidos te menosprecian y te dejan ir junto con la elfa, la cuál te muestra su gratitud y se disculpa por lo ocurrido, se presenta como Lauma, una druida del bosque.")
    print("Lauma: Gracias por tu ayuda aventurero, estoy en deuda contigo.")
    print(f"{nombre}: No hay de que, estoy en mi primera aventura en estos lugares.")
    print("Lauma: Si es tu primera aventura, te regalaré la bendición del bosque y la sabiavida, te ayudará mucho con tus futuras aventuras.")
    print("Lauma: Sigueme aventurero, te indicaré que debes hacer.")
    print("Luego de un rato caminando por el bosque, llegan a una cascada gigante y al medio hay un banco de piedra.")
    print("Lauma: Aventurero, debes de sentarte en el banco y aguantar el peso del sufrimiento de la naturaleza, si logras aguantarlo durante 5 minutos habrás pasado la primera prueba.")
    Aceptar = 1
    Rechazar = 2
    accion = int(input("1) Aceptar desafío, 2) Rechazar"))
    if accion == 1:
        print("Te diriges hacia el banco de piedra decidido a completar el desafío, aguantas sin problema durante 5 minutos sentado.")
        print("Al levantarte sientes que tu cuerpo pesa muchisimo más que antes, ya notas el efecto de la prueba.")
        print("Lauma: Felicidades aventurero, has completado la primera prueba, ahora deberás mover la roca que carga con el peso de los antepasados de mi linaje.")
        print("Suspiras profundamente, te supera con creces la roca, pero realmente quieres obtener la bendición del bosque, asi que con todo tu esfuerzo empiezas a mover la roca.")
        print("La roca se mueve lentamente, hasta una tortuga iria el doble de rápido, despúes de dos horas sin parar, logras llegar a la meta con la roca, caes al suelo exhausto.")
        print("Lauma: Aventurero, has completado con exito todas las pruebas, acercate a mi.")
        print("Te arrastras hacia Lauma, no tienes fuerzas para pararte, Lauma vierte un liquido azulado luminoso en tu boca.")
        print("Tragas el liquido como agua, de repente tu cuerpo ya no pesa, ya no sientes fatiga, podrías pelear contra mil enemigos sin cansarte.")
        print("Lauma: La sabiavida es la sangre del árbol primigenio del bosque, el primer árbol del mundo, notó tu valía en las pruebas y te ha concedido su bendición.")
        print("Lauma: Ya no tendrás que preocuparte por tu resistencia, ni por las heridas de combate, puedes sobrevivir a cualquier enemigo existente.")
        print("Agradeces a Lauma por la bendición, sientes que ya no hay nada más que hacer asi que te despides de ella.")
        print("Lauma: Hasta luego aventurero, que la bendición del bosque te acompañe en tus futuras aventuras.")
        print("Luego de llegar al gremio de aventureros vas a tu habitación a la posada y sientes un dolor inmenso en el corazón.")
        print("Caes al suelo del dolor y miras hacia la puerta, es Lauma.")
        print("???: Tan ingenuo y confiado, aquella druida que viste y hablaste no es más que un vestigio del pasado, es una pena para ti, tu muerte es segura.")
        print("Aquella silueta de Lauma se deshace y cambia a una figura con cuernos, reconoces en un instante que es uno de los apostoles de Satanás.")
        print("Mueres con un profundo dolor, el fin de tu historia.")
    else:
        print("Decides no aceptar el desafío, no crees que sea necesario, te das la vuelta despidiendote de Lauma y continuas con tu viaje por el bosque.")
        print("Lauma te sigue, lo sabes pero decides ignorarla.")
        print("Presientes que algo malo sucederá, la situación está rara.")
        print("Rápidamente atacas a Lauma por instinto, su figura femenina se deforma y ves un ser grotesco con cuernos, es uno de los apostoles de Satanás.")
        print("Entre ambos de crea una batalla que dura tan solo minutos, al parecer no era para tanto un apostol.")
        print("Notas que su cuerpo empieza a crecer mucho más, ahora tiene una forma indescriptible, pero sin duda peligrosa.")
        print("No tienes más opción que rogar y esperar un milagro...")
        print("Oh, literalmente un milagro.")
        print("Del cielo cae una lanza de luz atravesando y borrando de la existencia al apostol, no puedes creer lo que tus ojos vieron.")
        print("Desciende un ser angelical hacia ti, no sabes como reaccionar.")
        print("Sariel: Querido aventurero, sé más precavido la próxima vez, no podré protegerte en cualquier momento, mi nombre es Sariel.")
        print("Agradeces enormemente a Sariel entre lágrimas por haberte salvado.")
        print("Sariel: Te otorgaré la bendición de los cielos, te ayudará a notar la presencia de los seres vivos de tu alrededor, asi evitas el engaño.")
        print("Recibes la bendición de los cielos, Sariel desaparece de un pestañeo, decides volver al gremio y dar por finalizada tu aventura.")
elif Ruta == 2:
        print("Has elegido la montaña, el camino es difícil y peligroso, pero las vistas son impresionantes, ten cuidado con los acantilados.")
        print("Mientras caminas por las montañas, te percatas de humo, signifiacado de bandidos cerca,")
        print("Decides seguir el humo, y mientras te vas acercando te percatas de cadaveres y huesos tirados por todos lados, ")
        print("Llegas a donde proviene el humo y ves un campamento bandido destruido y muchos muertos,")
        print("Te acercas para investigar, y de repente empieza a temblar el suelo, el terreno solido se empieza a agrietar, Detras de unas montañas, aparece una silueta oscura con ojos blancos brillantes, la silueta te mira mientras tu la observas,")
        print("un escalofrio recorre todo tu cuerpo y sientes un mal presentimiento, la silueta oscura se va acercando con lentitud hacia ti")
        print("¿Que acción quieres realizar?")
        print("1) Huir, 2) Huir, 3) HUIR, 4) Atacar")
        Huir = 1
        Huir2 = 2
        HUIR = 3
        Atacar = 4
        accion = int(input("¿Que acción quieres realizar?"))
        if accion ==1:
            print("Decides correr como una gallina, pero no te servira de nada ya que la silueta oscura se da cuenta de tu acción y empieza a preseguirte, la silueta ocura es más rapida y alcanza a agarrarte, te agarra con sus dos manos y meintras tu gritas de dolor, te parte en dos terminando con tu agonía.")
            print("Que lamentable final, deberías haberlo pensado mejor.")
        elif accion == 2:
            print("Decides correr como una gallina, pero no te servira de nada ya que la silueta oscura se da cuenta de tu acción y empieza a preseguirte, la silueta ocura es más rapida y alcanza a agarrarte, te agarra con sus dos manos y meintras tu gritas de dolor, te parte en dos terminando con tu agonía.")
        elif accion == 3:
            print("Al tener miedo extremo, te paralizas, solo puedes observar como la solueta oscura se va acercando poco a poco, deformando su cara y exponiendo si horrible rostro, te das cuenta de que es el mismmo satanás, la silueta oscura te agarra, y meintras tu no puedes hacer nada, te acerca para olfatearte, se burlta de ti y luego te va metiendo en su boca lentamente para luego masticarte, muriendo y terminando con tu existencia.")
            print("Tal vez hubieras escogido otra ruta...")
        else:
            print("Decides hacerte el valiente, corres hacia la silueta oscura, la silueta oscura te lanza arboles y rocas, tu con mucha facilidad esquivas todo lo que te lanza, subes una montaña y te lanzas de cara contra la criatura, confiado de que ganaras, no te percatas de sus cuernos y te atravieza con uno, cegado por la confianza y el ego, terminas empalado muriendo al instante.")
            print("¿Creiste que podías con literalmente Satanas? Estas enfermo amig@...")
else:
    print("Has elegido la cueva, es un lugar oscuro y húmedo, lleno de misterios y peligros, asegúrate de llevar una antorcha.")
    print(f"{nombre} se adentra en la oscuridad sin ninguna fuente de iluminación.")
    print(f"{nombre} tropieza y cae a una caverna subterránea.")
    print("A lo lejos se puede visualizar una luz muy tenue, decides acercarte hacia aquella luz, y al momento de entrar")
    print("te encuentras con una sala muy larga, extrañamente con cadaveres de anteriores aventureros, logras ver que al final de la sala")
    print("hay cofre gigante del cual emana la luz que viste desde lejos.")
    print("Analizas la situación y llegas a la conclusión de que tienes que pasar por trampas para poder llegar al cofre")
    print("¿Qué harás?")
    Puzzle = 1
    Salida = 2
    accion = int(input("1) Hacer el intento, 2) Buscar una salida alternativa"))
    if accion == 1:
        print(f"{nombre} decide prepararse para superar los obstaculos que logró identificar.")
        print("Primero esquivas múltiples flechas que salieron disparadas de la oscuridad.")
        print("Luego pasas sobre una plataforma encima de una fosa de lava con un poco de dificultad")
        print("Sientes como tiembla el piso, te das media vuelta y ves como se acerca una gigante bola de fuego a toda velocidad.")
        print("Pones tu máximo esfuerzo en poder llegar hasta el cofre y lo logras, de repente ves como la bola desaparece.")
        print("Abres el cofre y en un párpadeo estas en la entrada de la cueva, pero con una espada reluciente.")
        print("Felicidades, en tu aventura has conseguir la famosa espada Excalibur.")
        print("Despúes de tu exitosa expedición regresas al gremio de aventureros para reclamar tu recompensa, te aguardan más aventuras por delante.")
    else:
        print("Decides que es mejor buscar una manera para salir de la cueva y empiezas a explorar.")
        print("Guiandote con las piedras relucientes de las estrechas paredes de la cueva, logras encontrar otra sala pero hay algo raro.")
        print("Ves que hay muchos más cadaveres que en la sala anterior, te preparas para un encuentro si es el caso.")
        print("De repente se escucha un estruendo desde el final de la sala y es una hidra enorme.")
        print("No sabes si la podrás derrotar, es un gran riesgo.")
        Atacar = 1
        Atacar2 = 2
        accion = int(input("1) Atacar, 2) NO tienes otra opción."))
        if accion == 1:
            print("Decides ir de frente contra la hidra, la hidra se percata de tu presencia y se lanza contra ti.")
            print("Luego de varios minutos peleando contra la hidra, estas agotado y con varias heridas graves, crees que tu final está cerca.")
            print("La hidra decidida a matarte con su último ataque, simplemente esperas a que llegue tu final.")
            print("¿¿¡¡¡QUE ES ESO!!!???")
            print("En un instante aparece una luz frente a ti y se imbuye en tu cuerpo, cambiando la forma de tu arma y potenciandola a gran escala.")
            print("Sientes una cálidez en todas las partes de tu cuerpo, y una fuerza inconmensurable, decides dar inicio a la muerte de la hidra.")
            print("De un solo ataque logras cercenar varias cabezas de la hidra, te sientes en confianza de lograr derrotarla.")
            print("Luego de una hora de batalla contra la hidra logras vencerla, entre sus entrañas ves algo cegador.")
            print("Te acercas y metes tu mano para recoger aquel objeto, es un anillo con un rubí incrustado, debe valer una fortuna.")
            print("Te lo pones por curiosidad, al mismo momento piensas en volver al gremio de aventureros.")
            print("Al instante te encuentras en el mismisimo gremio, te das cuenta del poder del anillo pero decides que es mejor venderlo.")
            print(f"Has completado tu primera expedición con éxito, felicidades {nombre}.")
        else:
            print("Te preparas con miedo contra la hidra.")
            print("Tus manos están sudando, escuchas tu corazón latir, tiemblas y estas demasiado asustado.")
            print("La hidra sabe que estas con miedo, y se lanza contra ti despedazandote en el acto.")
            print("Pudiste haber tenido un mejor resultado si hubieras tenido más confianza.")
print("Gracias por jugar, espero que hayas disfrutado tu aventura, hasta la próxima.")