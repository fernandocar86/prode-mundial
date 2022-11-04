import pandas as pd
import os
from os import listdir
import re
import shutil 

global dict_resultados
global dict_estimaciones

def iniciar():
    crear_carpeta('aux')
    definir_puntajes()
    cargar_resultados()
    reunir_puntajes()
    borrar_carpeta('aux')
    
    
def definir_puntajes():
    print('Los puntajes estándar son los siguientes: ')
    informar_puntajes(10, 5, 2)
    print('Si querés usar los puntajes estándar, ingresá s; si querés ingresar tus propios puntajes ingresa n')
    respuesta1 = input()
    if respuesta1 == 's':
        global exacto 
        exacto = 10 # coincidencia goles ambos equipos
        global gpe
        gpe = 5 # coincidencia ganador, perdedor o empate
        global goles
        goles = 2 # coincidencia goles de un equipo
        informar_puntajes(exacto, gpe, goles)
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
        informar_puntajes(exacto, gpe, goles)
    else:
        print('esa no es una respuesta correcta')
        definir_puntajes()

def informar_puntajes(exacto, gpe, goles):
    print('si se acierta a los goles de ambos equipos en un partido, son ' + str(exacto) + ' puntos')
    print('si se acierta quién gana o si hay empate en un partido, son ' + str(gpe) + ' puntos')
    print('Si se acierta a los goles de solo uno de los equipos, son '+str(goles)+ ' puntos')

def crear_carpeta(nombre):
    if not os.path.exists(nombre):
        os.makedirs(nombre)

def borrar_carpeta(nombre):
    shutil.rmtree(nombre)
    
def cargar_resultados():
    print('Los resultados se van a buscar en la carpeta resultados/. Si estás de acuerdo escribí s. Si no, escribí n.')
    respuesta3 = input()
    if respuesta3 == 's':
        global ruta
        ruta = 'resultados/'
    elif respuesta3 == 'n':
        print('Indicá en qué carpeta están alojados los resultados')
        ruta = input()
    else:
        print('La respuesta no es adecuada') 
    mensaje_resultados = 'resultados anotados'
    resultados = cargar_datos(ruta)
    for file in resultados:
        print('qué peso tiene los resultados en '+' '.join(re.sub(".csv", "", file).split()) + ' en este prode')
        peso = int(input()) 
        fase = file
        ruta_entera = ruta + file
        data = pd.read_csv(ruta_entera)
        df = pd.DataFrame(data)
        dict_resultados = []
        cargar_partidos(df, mensaje_resultados, dict_resultados)
        cargar_estimaciones(dict_resultados, peso, fase)

def cargar_datos(path):
    filenames = listdir(path)
    return [ filename for filename in filenames if filename.endswith( ".csv" ) ]

def cargar_partidos(df, mensaje, dict_partidos):
    lista_partidos = []
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
#    return dict_partidos    

def comparar_result_estim(dict_resultados, dict_estimaciones, file, est_indiv_fase, peso):
    puntaje = 0
    for item1 in dict_resultados:
        for item2 in dict_estimaciones:
                if item1[0] == item2[0] and item1[1] == item2[1] and item1[2] == item2[2]:
                    puntaje = puntaje + exacto * peso
                elif item1[0] == item2[0] and item1[1] == item2[1]:
                    puntaje = puntaje + goles * peso
                elif item1[0] == item2[0] and item1[2] == item2[2]:
                    puntaje = puntaje + goles * peso
                elif item1[0] == item2[0] and item1[1] == item1[2] and item2[1] == item2[2]:
                    puntaje = puntaje + gpe * peso
                elif item1[0] == item2[0] and item1[1] > item1[2] and item2[1] > item2[2]:
                    puntaje = puntaje + gpe * peso
                elif item1[0] == item2[0] and item1[1] < item1[2] and item2[1] < item2[2]:
                    puntaje = puntaje + gpe * peso
                else:
                    puntaje = puntaje
    print(puntaje)
    nombre = ' '.join(re.sub(".csv", "", file).split())
    est_indiv_fase.write(nombre+','+str(puntaje)+'\n')                 
        
def cargar_estimaciones(dict_resultados, peso, fase):
    print('Las estimaciones de quienes participan de este prode se van a buscar en la carpeta estimaciones-participantes/. Si estás de acuerdo escribí s. Si no, escribí n.') 
    respuesta4 = input()
    if respuesta4 == 's':
        ruta2 = 'estimaciones-participantes/'
    elif respuesta4 == 'n':
        print('Indicá en qué carpeta están alojadas las estimaciones de los participantes')
        ruta2 = input()
    else:
        print('La respuesta no es adecuada') 
    estimaciones = cargar_datos(ruta2)
    mensaje_estimaciones = 'estimaciones anotadas'
    for file in estimaciones:
        nombre_part = ' '.join(re.sub(".csv", "", file).split())
        nombre_est_indiv_fase = 'aux/'+nombre_part+'_puntajes.csv'
        est_indiv_fase = open(nombre_est_indiv_fase, "a", encoding='utf-8')
        ruta_entera2 = ruta2 + file
        data2 = pd.read_csv(ruta_entera2)
        df2 = pd.DataFrame(data2)
        dict_estimaciones = []
        cargar_partidos(df2, mensaje_estimaciones, dict_estimaciones)
        comparar_result_estim(dict_resultados, dict_estimaciones, file, est_indiv_fase, peso)

def reunir_puntajes():
    puntajes = open('puntajes.csv', "w", encoding='utf-8')
    puntajes.write('Participante,Puntaje\n')
    ruta2 = 'aux/'
    planillas_part = cargar_datos(ruta2)
    for file in planillas_part:
        ruta_entera2 = ruta2 + file
        nombre_part = ' '.join(re.sub("_puntajes.csv", "", file).split())
        data2 = pd.read_csv(ruta_entera2, header=None)
        df = pd.DataFrame(data2)
        valor = 0
        for index, row in df.iterrows():
            valor = valor + row[1]
        puntajes.write(nombre_part+','+str(valor)+'\n')
    puntajes.close()
        
#reunir_puntajes()
#cargar_resultados()
