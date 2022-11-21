import re
import pandas as pd


def armado_html(archivo):
    home = open('home.html', "w", encoding='utf-8')
    home.write('<!DOCTYPE html> \n <html> \n <head> <title>Prode mundial</title> \n </head> \n <body> \n <h1>Resultados del prode mundial</h1> \n <p></p>\n')
    home.write('<table>\n<tr>\n<th>Participante</th>\n<th>Puntaje</th>\n</tr>')
    data = pd.read_csv(archivo)
    df = pd.DataFrame(data)
#    print(df)
    df2 = df.sort_values('Puntaje', ascending=False)
    for index, row in df2.iterrows():
        home.write('<tr>\n<th>'+str(row[0])+'</th>\n<th>'+str(row[1])+'</th>\n</tr>')
    home.write('</table>\n')
    puntaje_ganador = df2.iloc[0,1]
    ganador = [str(df2.iloc[0,0])]
    for index, row in df2.iterrows():
        if index != 0 and df2.iloc[index,1] == df2.iloc[0,1]:
            ganador.append(str(df2.iloc[index,0]))
        else:
            ganador = ganador
    if len(ganador) == 1:
        home.write('<p>Ganó el prode nada más ni nada menos que '+str(df2.iloc[0,0])+' con '+str(puntaje_ganador)+' puntos</p>\n')
    else:
        prefijo = ganador[0:-1]
        sufijo = ganador[-1]
        print(sufijo)
        ganadores = ''
        for item in prefijo:
            if item != prefijo[-1]:
                ganadores = ganadores+str(item)+', '
            else:
                ganadores = ganadores+str(item)
        ganadores = ganadores+' y '+str(sufijo)
        home.write('<p>Ganaron el prode nada más ni nada menos que '+ganadores+' con '+str(puntaje_ganador)+' puntos</p>\n') 
    data2 = pd.read_csv('rondasypesos.csv', header=None)
    df3 = pd.DataFrame(data2)
    home.write('<p>Los puntos que se usaron para calcular estos puntajes fueron los siguientes</p>\n<table>\n')
    for index, row in df3.iterrows():
        home.write('<tr>\n<th>'+str(row[0])+'</th>\n<th>'+str(row[1])+'</th>\n<th>'+str(row[2])+'</th>\n<th>'+str(row[3])+'</th>\n<th>'+str(row[4])+'</th>\n</tr>')
    home.write('</table>\n')
    home.write('</body> \n </html>')
    home.close()
 
#armado_html('puntajes.csv')
