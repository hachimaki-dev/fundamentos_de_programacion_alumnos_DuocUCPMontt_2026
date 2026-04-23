favoritos = ["Bohemian Rhapsody - Queen", "Imagine - John Lennon", "Billie Jean - Michael Jackson",
    "Stayin' Alive - Bee Gees", "Like a Rolling Stone - Bob Dylan", "Hey Jude - The Beatles",
    "Wonderwall - Oasis", "Smells Like Teen Spirit - Nirvana", "Hotel California - Eagles",
    "Sweet Child O' Mine - Guns N' Roses", "One - U2", "Back in Black - AC/DC",
    "Creep - Radiohead", "Lose Yourself - Eminem", "Rolling in the Deep - Adele",
    "Uptown Funk - Mark Ronson ft. Bruno Mars", "Shape of You - Ed Sheeran", "Blinding Lights - The Weeknd",
    "Despacito - Luis Fonsi", "La Camisa Negra - Juanes", "Rayando el Sol - Maná",
    "Musica Ligera - Soda Stereo", "Lamento Boliviano - Enanitos Verdes", "Matador - Los Fabulosos Cadillacs",
    "La Flaca - Jarabe de Palo", "Eres - Café Tacvba", "A Dios le Pido - Juanes",
    "Bailando - Enrique Iglesias", "Gasolina - Daddy Yankee", "Hips Don't Lie - Shakira",
    "Livin' la Vida Loca - Ricky Martin", "Corazón Partío - Alejandro Sanz", "Thriller - Michael Jackson",
    "Purple Rain - Prince", "Every Breath You Take - The Police", "Under the Bridge - Red Hot Chili Peppers",
    "Clocks - Coldplay", "Mr. Brightside - The Killers", "Seven Nation Army - The White Stripes",
    "Take on Me - a-ha", "Girls Just Want to Have Fun - Cyndi Lauper", "Material Girl - Madonna",
    "Superstition - Stevie Wonder", "Let's Get It On - Marvin Gaye", "Respect - Aretha Franklin",
    "Bridge Over Troubled Water - Simon & Garfunkel", "Dreams - Fleetwood Mac", "Go Your Own Way - Fleetwood Mac",
    "Heroes - David Bowie", "Space Oddity - David Bowie", "Rocket Man - Elton John",
    "Tiny Dancer - Elton John", "Piano Man - Billy Joel", "Born to Run - Bruce Springsteen",
    "Thunder Road - Bruce Springsteen", "The Sound of Silence - Simon & Garfunkel", "Yesterday - The Beatles",
    "Something - The Beatles", "God Only Knows - The Beach Boys", "Good Vibrations - The Beach Boys",
    "California Dreamin' - The Mamas & the Papas", "Paranoid - Black Sabbath", "Iron Man - Black Sabbath",
    "Highway to Hell - AC/DC", "T.N.T. - AC/DC", "Start Me Up - The Rolling Stones",
    "Paint It Black - The Rolling Stones", "Satisfaction - The Rolling Stones", "Wish You Were Here - Pink Floyd",
    "Comfortably Numb - Pink Floyd", "Another Brick in the Wall - Pink Floyd", "Roxanne - The Police",
    "Message in a Bottle - The Police", "Radio Ga Ga - Queen", "Don't Stop Me Now - Queen",
    "Under Pressure - Queen & David Bowie", "Sultans of Swing - Dire Straits", "Walk of Life - Dire Straits",
    "Money for Nothing - Dire Straits", "Pride (In the Name of Love) - U2", "With or Without You - U2",
    "Beautiful Day - U2", "In the End - Linkin Park", "Numb - Linkin Park",
    "Bring Me to Life - Evanescence", "Zombie - The Cranberries", "Bad Romance - Lady Gaga",
    "Poker Face - Lady Gaga", "Flowers - Miley Cyrus", "Anti-Hero - Taylor Swift"]


favoritos.append("Congelao - Cachureos")
favoritos.append("Mi gran noche - Rafael")

favoritos.pop()
favoritos.pop()
favoritos.pop()
favoritos.pop()

contador = 0

for cancion in favoritos :
    print(f"El nombre de la cancion es: {contador} es: {cancion} ")
    contador = contador + 1


