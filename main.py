import pandas as pd
from os import listdir

def iniciar():
    definir_puntajes()
    cargar_resultados()
    cargar_estimaciones()

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

def armar_puntajes(exacto, gpe, goles):
    print('si se le pega a los goles de ambos equipos en un partido son ' + str(exacto) + ' puntos')
    print('si se le pega quién gana o si hay empate en un partido? son ' + str(gpe) + ' puntos')
    print('Si se le pega a los goles de uno de los equipos son '+str(goles)+ ' puntos')
    
def cargar_resultados():
    print('Indicá en qué carpeta están alojados los resultados')
    ruta = input()
    mensaje_resultados = 'resultados anotados'
    resultados = cargar_datos(ruta)
    for file in resultados:
        ruta_entera = ruta + file
        data = pd.read_csv(ruta_entera)
        df = pd.DataFrame(data)
        cargar_partidos(df, mensaje_resultados)

def cargar_datos(path):
    filenames = listdir(path)
    return [ filename for filename in filenames if filename.endswith( ".csv" ) ]

def cargar_partidos(df, mensaje):
    lista_partidos = []
    dict_partidos = []
    for index, row in df.iterrows():
        if not pd.isnull(row[3]): 
            part = row[0]+': '+row[1]+ " vs "+row[2]
            lista_partidos.append(part)
            valores_partido = [part, int(row[3]), int(row[4])]
            dict_partidos.append(valores_partido)
    print('los partidos para los que hay '+mensaje+' son los siguientes:')
    for item in lista_partidos:
        print(item)
    print(dict_partidos)        
        
def cargar_estimaciones():
    print('Indicá en qué carpeta están alojadas las estimaciones de los participantes')
    ruta2 = input()
    estimaciones = cargar_datos(ruta2)
    mensaje_estimaciones = 'estimaciones anotadas'
    for file in estimaciones:
        ruta_entera2 = ruta2 + file
        data2 = pd.read_csv(ruta_entera2)
        df2 = pd.DataFrame(data2)
        cargar_partidos(df2, mensaje_estimaciones)

iniciar()
#definir_puntajes()
#cargar_resultados()
