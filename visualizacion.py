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
#    print(df2)
    home.write('</body> \n </html>')
    home.close()
 
#armado_html('puntajes.csv')
