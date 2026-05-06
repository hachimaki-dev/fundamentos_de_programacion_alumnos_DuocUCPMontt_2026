chat=['hola','noob','genial','manco']

palabrasmalas=['noob','manco']

for i in chat:
    if i in palabrasmalas:
        print('[Censurado]')
    else:
        print(i)    