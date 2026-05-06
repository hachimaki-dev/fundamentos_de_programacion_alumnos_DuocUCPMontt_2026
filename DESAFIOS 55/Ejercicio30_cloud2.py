respuestasweb=[200, 404, 500, 200, 500]
reintento=1

for i in respuestasweb:
    if i == 200:
        print('OK')
    if i == 404:
        print('NOT FOUND')
    if i == 500:
        reintento -=1
        if reintento<0:
            print('SERVIDOR CAIDO')
            break
        print('Reintentando')        