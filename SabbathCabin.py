import sys
import time

print("Hola, el día de hoy serás partícipe de una novela gráfica interactiva en la cuál TÚ seras el protagonista.")
nombre_protagonista = input("----¿Con qué nombre quieres que se te llame?---- ")
print("Espléndido, entonces " + nombre_protagonista + " espero que disfrutes de esta novela...")

comenzar = input("¿Estás listo para comenzar? Si/No ") 

if comenzar == "Si" or comenzar == "si":
    print("¡Excelente! Comencemos entonces")
else:
    print("Bueno, no hay problema, tómate tu tiempo.")
    sys.exit()

print("-Estás en una vieja cabaña alejada de cualquier zona urbana, en medio del bosque de una inmensa montaña, en una noche fría y lluviosa")
time.sleep(2)
print("Esta cabaña es tu hogar, heredada por tu padre luego de su defunción hace 3 años por razones que jamas fueron resueltas. Una media agua anticuada, paredes de madera, una rústica chimenea de piedra la cuál es tu única fuente de luz y calor. Sin embargo esta se está quedando sin leña por lo que se está extinguiendo")
time.sleep(1)

decision_n1 = input("Que harás? | 1. Ir por leña | 2. Dejar que el fuego se extinga e irte a dormir ")

if decision_n1 == "1":
    print("Decides salir a buscar leña a la bodega, la cuál esta a unos metros de la cabaña pero por la llvuia torrencial y los fuertes vientos no puedes ver casi nada")
    decision_n2 = input("Qué harás? | 1. Volver adentro | 2. Seguir hasta la bodega ")
    
    if decision_n2 == "1":
        print("Decides simplemente volver adentro, pero sientes que algo no está bien.")
        time.sleep(2)
        print("Cierras la puerta para luego pararte sobre la llama ya extinguiendose para secarte los pies, sigues sintiendo una incomodidad pero no sabes por qué")
    
    if decision_n2 == "2":
        print("Llegas a la bodega y te pones bajo techo inmediatamente.")
        aire_tibio = input("Sientes una corriente de aire tibia en tu cuello. | 1. Ignorarlo | 2. Voltear ")
        
        if aire_tibio == "1":
            print("Decides ignorar la corriente y vuelves adentro antes de que el clima empeore.")
        if aire_tibio == "2":
            print("Decides darte vuelta con algo de temor... y solo resulta ser un gato negro salvaje que se refugiaba de la tormenta en tu bodega, lo acaricias y ves como se va y desaparece en la densa y oscura lluvia, procedes a entrar a tu hogar")
        
        print("Al entrar, cierras la puerta y dejas la leña en el suelo, te quitas la ropa mojada con la que saliste")
        print("Recoges la leña del piso para ponerla en la chimenea. Te encanta ver como el fuego toma vida, es casi hipnótico para ti.")

    print("La calma que tenías se acaba cuando notas que hay unas huellas en el suelo, sabes que no son tuyas pero las vas a limpiar porque te parece una locura pensar que pudo haber sido alguien mas, despues de todo... vives solo")
    time.sleep(3)
    print("Tras limpiarlas, te das cuenta de que la puerta está entreabierta, que raro, jurarías que la habías cerrado")
    time.sleep(5)
    print("En cuánto la cierras el fuego se apaga repentinamente.")
    time.sleep(3)
    print("La oscuridad te envuelve y sientes una presión sobre tu pecho. Ves una silueta en la esquina de la sala. Ya no puedes negar que algo extraño está sucediendo.")
    time.sleep(5)
    
    linterna = input("Tienes una linterna en un cajón cerca tuyo, ¿quieres ocuparla? | 1. Sí | 2. No ")
    
    if linterna == "1":
        print("Decides tomar la linterna, la enciendes y apuntas hacia la silueta, pero no ves nada, es como si la oscuridad se tragara toda la luz de tu linterna.")
        time.sleep(3)
        print("De repente, sientes un frío intenso y una voz susurra tu nombre al oído. La silueta se acerca lentamente hacia ti...")
        time.sleep(5)
        print("La oscuridad te envuelve por completo. Has presenciado tu lento fin.")
        time.sleep(3)
        print("Al parecer estuviste sentenciado desde el momento en que abriste esa puerta.")
        sys.exit()

    if linterna == "2":   
        print("Decides no ocupar la linterna, no estas seguro si es la mejor idea. No parece que la silueta se mueva, por lo que te acercas lentamente hasta casi tenerlo de frente.")
        time.sleep(3)
        print("Era simplemente el perchero de tu padre, el cual por tu páncio habías olvidado que siquiera existía, das un suspiro de relajo luego de porfin acabar con toda esa tensión... pero escuchas algo que hace que se te hiele la sangre.")
        time.sleep(6)
        print("Una voz susurra tu nombre tan cerca de tu oído que sientes su aliento frío como la muerte rozando tu piel, " + nombre_protagonista + "...")
        time.sleep(5)
        print("Te das vuelta tan rápido como puedes, para presenciar como una masa oscura y vibrante te abraza haciendo una simbiosis con tu cuerpo, escuchas los sollozos de tu padre dentro de esta entidad vacía y tenebrosa, te niegas a luchar y siemplemente te entregas a lo que sea que te esté consumiendo.")
        time.sleep(5)
        print("Has presenciado tu lento fin.")
        print("-----GAME OVER-----")
        sys.exit()

if decision_n1 == "2": 
    print("Decides dejar que el fuego se consuma, te quedas observandolo casi hipnotizado hasta que se apaga por completo para luego ir a tu habitación")
    print("Ya en tu habitación escuchas algo extraño como raspando tu ventana pero decides ignorarlo pensando que habra sido el viento")
    time.sleep(2)
    print("Sin embargo, vuelves a escuchar la ventana y esta vez como si la estuvieran tocando con un dedo, haciendo un patrón de 3 toques suaves.")
    time.sleep(2)
    print("*Toc* *Toc* *Toc*")
    
    abrir_ventana = input("Un escalofrío recorre toda tu columna vertebral, pero por alguna razón sientes que deberías abrir la ventana para quitarte esa sensación de incomodidad por la que estás pasando. ¿Qué harás? | 1. Abrir la ventana | 2. Fingir que no has escuchado nada e irte a dormir ")
    time.sleep(2)
    
    if abrir_ventana == "1":
        print("Decides abrir la ventana")
        print("Al abrir la ventana, un aire polar cruza por ella sacudiendo tus cortinas y haciendo que tu cabello se levante, observas hacia afuera y puedes ver como la tormenta sigue...")
        time.sleep(4)
        print("Pero... Un momento... No escuchas la tormenta, no siente el viento, estás presenciando algo que jamas pensarías ver, una tormenta gigante sin algun tipo de sonido, y ahi es cuando escuchas algo que te quita el alma del cuerpo")
        time.sleep(4)
        print("Sin darte vuelta escuchas algo desde tu espalda, una voz casi inhumana, con un tono tan grave y ronco que parece venir desde las fauces del infierno")
        time.sleep(2)
        print(" " + nombre_protagonista + "... D A T E  L A  V U E L T A...")
        time.sleep(2)
        
        darse_vuelta = input("¿Qué harás? | 1. Darte la vuelta | 2. Quedarte quieto sin mover ni un músculo ")
        
        if darse_vuelta == "1":
            print("Decides darte la vuelta lentamente, para ver en la pared de el fondo de tu habitación la silueta de hombre, o más bien su sombra, un negro tan oscuro como la misma noche, su cuerpo vibrando como si no perteneciera a este mundo")
            time.sleep(3)
            print("Ves como de dónde debería estar su rostro surge una macabra sonrisa con dientes amarillos y una lengua roja como un río de sangre")
            time.sleep(3)
            print("*parpadeas*")
            time.sleep(3)
            parpadear = input("El ente repentinamente esta cara a cara contigo " + nombre_protagonista + "!. No te atrevas a volver a parpadear.| 1.Parpadeas. | 2.Parpadeas. ") 
            print("Parpadeas, pero pareciera que no hubieras abierto los ojos, solo presencias oscuridad por todos lados, una oscuridad que te come lentamente a ti también")
            time.sleep(5) 
            print("Has presenciado tu lento fin")
            sys.exit()

        if darse_vuelta == "2":
            print("Intentas no moverte, pero una fuerza vibrante casi eléctrica obliga tu cuerpo a girar.")
            time.sleep(2)
            print("Ves a la entidad cara a cara. La oscuridad te consume por completo.")
            print("Has presenciado tu lento fin.")
            sys.exit()

    if abrir_ventana == "2":
        print("Finges demencia como si solo fueras alguien escuchando el viento, aun cuando sabes que no es así")
        time.sleep(3)
        print("Sigues escuchando los golpes en la ventana, pero solo los ignoras, piensas que si no le prestas atención se irá, te tapas los oídos y te escondes bajo tus sábanas hasta que te quedas dormido")
        time.sleep(5)
        print("Lo que sea que estuviera acechando ahi fuera se fue. Hiciste bien con no abrir la ventana ni la puerta, " + nombre_protagonista + ", has sobrevivido esta noche, felicidades")
        print("---GOOD ENDING---")
        sys.exit()