import pandas as pd
from os import listdir


def definir_puntajes():
    print('Si querés usar los puntajes estándar, ingresá s; si querés ingresar tus propios puntajes ingresa n')
    respuesta1 = input()
    if respuesta1 == 's':
        exacto = 10 # coincidencia goles ambos equipos
        gpe = 5 # coincidencia ganador, perdedor o empate
        goles = 2 # coincidencia goles de un equipo
        armar_puntajes(exacto, gpe, goles)
    elif respuesta1 == 'n':
        print('¿Cuál es el valor si se le pega a los goles de ambos equipos en un partido?')
        respuesta2 = input()
        exacto = respuesta2
        print('¿Cuál es el valor si se le pega quién gana o si hay empate en un partido?')
        respuesta3 = input()
        gpe = respuesta3
        print('¿Cuál es el valor si se le pega a los goles de uno de los equipos?')
        respuesta4 = input()
        goles = respuesta4
        armar_puntajes(exacto, gpe, goles)
    else:
        print('esa no es una respuesta correcta')
        definir_puntajes()

def cargar_resultados():
    print('Indicá en qué carpeta están alojados los resultados')
    ruta = input()
    resultados = cargar_datos(ruta)
    for file in resultados:
        ruta_entera = ruta + file
        data = pd.read_csv(ruta_entera)
        print(data)
    
    
def cargar_datos(path):
    filenames = listdir(path)
    return [ filename for filename in filenames if filename.endswith( ".csv" ) ]

def armar_puntajes(exacto, gpe, goles):
    print('si se le pega a los goles de ambos equipos en un partido son ' + str(exacto) + ' puntos')
    print('si se le pega quién gana o si hay empate en un partido? son ' + str(gpe) + ' puntos')
    print('Si se le pega a los goles de uno de los equipos son '+str(goles)+ ' puntos')

#definir_puntajes()
cargar_resultados()
